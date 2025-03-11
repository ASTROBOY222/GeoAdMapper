## Setup

1. **Create a Service Account** in **Google Cloud Platform**, download credentials (`service_account.json`), and place it in `GEOADMAPPER/`.
2. **Enable APIs**:
   - Google Sheets API
   - Google Maps JavaScript API
3. **Configure `.env` file**:
   - GOOGLE_SHEET_CREDENTIALS=service_account.json
   - SPREADSHEET_ID=your_spreadsheet_id
   - GOOGLE_MAPS_API_KEY=your_google_maps_api_key

## Installation

pip install -r requirements.txt

## Usage

Run locally:
python main.py
