import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("SPREADSHEET_ID"), os.getenv("GOOGLE_SHEET_CREDENTIALS"))