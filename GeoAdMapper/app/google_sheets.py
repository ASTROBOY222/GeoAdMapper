from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

def get_coordinates():
    creds = Credentials.from_service_account_file(os.getenv("GOOGLE_SHEET_CREDENTIALS"))
    service = build('sheets', 'v4', credentials=creds, static_discovery=False)

    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    range_name = 'Sheet1!A2:D'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    coordinates = result.get('values', [])

    return [{"lat": float(row[1]), "lng": float(row[2])} for row in coordinates]
    # return [{"let": float(row[1]), "lng": float(row[2])} for row in coordinates]