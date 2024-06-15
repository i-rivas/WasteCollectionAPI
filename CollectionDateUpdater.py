import pandas as pd
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='collection_data.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

# Define the API endpoint and the necessary headers
api_url = "https://gis.sanantonio.gov/swmd/mycollectionday/Request.aspx"
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'gis.sanantonio.gov',
    'Referer': 'https://gis.sanantonio.gov/swmd/mycollectionday/default.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# Function to get waste collection data
def get_collection_data(address):
    params = {
        'addr': address,
    }
    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for address {address}: {e}")
        return None

# Function to extract Brush and Bulky dates
def extract_brush_and_bulky(data):
    if data and len(data) > 0:
        attributes = data[0].get('attributes', {})
        brush = attributes.get('Brush')
        bulky = attributes.get('Bulky')
        return {'Brush': brush, 'Bulky': bulky}
    return None

# Read the Excel file
input_file = 'Addresses.xlsx'
df = pd.read_excel(input_file)

# Ensure the relevant columns are treated as strings
df['Bulky_Collection_Date'] = df['Bulky_Collection_Date'].astype(str)
df['Brush_Collection_Date'] = df['Brush_Collection_Date'].astype(str)

# Iterate through the DataFrame and get the collection dates
for index, row in df.iterrows():
    address = row['Address']
    collection_data = get_collection_data(address)
    brush_and_bulky_data = extract_brush_and_bulky(collection_data)
    if brush_and_bulky_data:
        df.at[index, 'Bulky_Collection_Date'] = brush_and_bulky_data['Bulky']
        df.at[index, 'Brush_Collection_Date'] = brush_and_bulky_data['Brush']
    else:
        logging.info(f"No data found for address {address}")

# Save the updated Excel file
output_file = 'updated_addresses.xlsx'
df.to_excel(output_file, index=False)
logging.info(f"Updated Excel file saved as {output_file}")
