import requests

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
    # Define the parameters
    params = {
        'addr': address,
    }

    # Send a GET request to the API
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to extract Brush and Bulky dates
def extract_brush_and_bulky(data):
    if data and len(data) > 0:
        attributes = data[0].get('attributes', {})
        brush = attributes.get('Brush')
        bulky = attributes.get('Bulky')
        return {'Brush': brush, 'Bulky': bulky}
    return None

# Example usage
address = "address_goes_here"  # Provide an address, only house number and street name
collection_data = get_collection_data(address)

# Extract and print Brush and Bulky dates
brush_and_bulky_data = extract_brush_and_bulky(collection_data)
if brush_and_bulky_data:
    print("Brush Collection Date:", brush_and_bulky_data['Brush'])
    print("Bulky Collection Date:", brush_and_bulky_data['Bulky'])
else:
    print("No Brush and Bulky data found.")
