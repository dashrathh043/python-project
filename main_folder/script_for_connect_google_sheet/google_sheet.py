from urllib.error import HTTPError
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import pathlib


parent_dir = pathlib.Path(__file__).parent.resolve()
SERVICE_ACCOUNT_FILE = os.path.join(parent_dir,'keys.json')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gOhIr0dM2qRzjw9evue-uh_vVsV78oIb-BNcQDePGwI'
#range of row and coloum
#SAMPLE_RANGE_NAME = "sales!A1:B5"
#complete sheet
SAMPLE_RANGE_NAME = "sales"

try:
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        
        #reading data
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        print("values = {}".format(values))
        
        #writing data in new sheet
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="demo", valueInputOption="USER_ENTERED", body={"values":values})
        response = request.execute()
        print(response)

        #appending data in existing sheet
        data = [["kkk","26"],["pp","24"]]
        request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="demo", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":data})
        response = request.execute()
        print(response)

        #delete data only(not row)
        request = sheet.values().batchClear(spreadsheetId=SAMPLE_SPREADSHEET_ID, body={"ranges":"demo!A11:B13"})
        response = request.execute()
        print(response)

except HTTPError as err:
        print(err)