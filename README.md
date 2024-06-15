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
  | Address goes here | City | Zip_code | Blank | Blank |


