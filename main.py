from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import info

load_dotenv()
id_sheet = os.getenv("ID_SHEET")
range_sheet = os.getenv("RANGE_SHEET")

# Configuração de autorização. Permite ler e escrever na planilha.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# ID da planilha + Nome e células da tabela
SAMPLE_SPREADSHEET_ID = id_sheet
SAMPLE_RANGE_NAME = range_sheet


def main():
    # Leitura das credenciais da API
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Conexão com as informações da tabela
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Leitura das informações da planilha
        sheet = service.spreadsheets()
        leitura = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        
        # Escrita de informações na planilha
        add_values = info.list_email()
        sheet = service.spreadsheets()
        escrita = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME, 
                                valueInputOption="USER_ENTERED",
                                body={"values": add_values}).execute()
    except HttpError as err:
        print(err)
    
if __name__ == '__main__':
    main()