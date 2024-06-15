# Waste Collection API

This repository contains a Python script that fetches Brush and Bulky waste collection dates for addresses in San Antonio, TX, and updates an Excel file with this information.

## Features
- Fetch Brush and Bulky waste collection dates using the San Antonio waste collection API.
- Read addresses from an Excel file.
- Write the fetched collection dates back to the Excel file.
- Log all requests and responses for debugging and verification purposes.

## Requirements
- Python 3.6+
- pandas library
- requests library
- openpyxl library

## Installation
1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/WasteCollectionScheduler.git
cd WasteCollectionScheduler
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install the required libraries:**

```bash
pip install pandas requests openpyxl
```

## Usage

1. **Prepate the Excel file:**
   The Excel file should be structured as follows:
   
| Address | City | Zip_Code | Bulky_Collection_Date | Brush_Collection_Date |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 123 Main Street | San Antonio | 78292 | Blank | Blank |

2. **Run the script:**

   ```bash
   python CollectionDateUpdater.py
   ```

3. **Check the output:**
   The script will create an updated Excel file named '**updated_address.xlsx**' with the fetch Brush and Bulky collection dates.

## Script Details 
### 'waste_collection_scheduler.py'
This script performs the following tasks:

1. **Read the Excel file:**
   ```python
   input_file = 'Address.xlsx'
   df = pd.read_excel(input_file)
   ```
2. **Fetches collection dates using the San Antonio waste collection API:**

   - **API Endpoint:**
     ```python
     https://gis.sanantonio.gov/swmd/mycollectionday/Request.aspx
     ```
   - **Headers:**
     ```python
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
      ```
3. **Extracts and updates Brush and Bulky dates in the DataFrame:**
   ```python
   df['Bulky_Collection_Date'] = df['Bulky_Collection_Date'].astype(str)
   df['Brush_Collection_Date'] = df['Brush_Collection_Date'].astype(str)

   for index, row in df.iterrows():
    address = row['Address']
    collection_data = get_collection_data(address)
    brush_and_bulky_data = extract_brush_and_bulky(collection_data)
    if brush_and_bulky_data:
        df.at[index, 'Bulky_Collection_Date'] = brush_and_bulky_data['Bulky']
        df.at[index, 'Brush_Collection_Date'] = brush_and_bulky_data['Brush']
   ```
4. **Saves the updated DataFrame to a new Excel file:**
   ```python
   output_file = 'updated_addresses.xlsx'
   df.to_excel(output_file, index=False)
   logging.info(f"Updated Excel file saved as {output_file}")
   ```
## Functions
### **'get_collection_data(address)'**
Fetches collection data from the API for a given address.

- **Parameters:**
  - **'address'** (str): The address to fetch collection data for.
- **Returns:**
  - **'dict'**: The JSON response from the API, or **'None'** if the request fails.
### **'extract_brush_and_bulky(data)'**
Extracts Brush and Bulky collection dates from the API response.
- **Parameters:**
   -**'data'**(dict): The JSON response from the API.
- **Returns:**
   -**'dict'**: A dictionary containing **'Brush'** and **'Bulky'** dates, or **'None'** if the data is not available.

## Logging

The script logs all requests, responses, and any error to **'collection_data.log'** for debugging and verification purposes.

## **'CollectionDayAPI.py'** Script
This script is provided for experimentation purposes, feel free to provide an address and configure the responses
