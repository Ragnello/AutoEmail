import os
import re
from datetime import datetime
import pytz
from imap_tools import MailBox, AND
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
rem = os.getenv("FROM")
texto = os.getenv("TEXT")
fuso = pytz.timezone(os.getenv("FUSO"))
log_imap = os.getenv("LOG_IMAP")

def list_email():
    info = list()
    meu_email = MailBox(log_imap).login(user, password)
    list_emails = meu_email.fetch(AND(from_=rem, text=texto))
    
    for i, email in enumerate(list_emails):
        # Busca das informações Nome, Valor e Data
        match_name = re.search(r'Pix de <strong>(.*?)</strong>', email.html)
        nome = match_name.group(1)
        
        match_value = re.search(r'R\$(.*?)</strong></div>', email.html)
        valor = match_value.group(1).strip()
        
        aux_date = email.date
        aux_date = aux_date.astimezone(fuso)
        data = aux_date.strftime("%d/%m/%Y")
        
        registro = [nome.title(), data, valor]
        
        info.append(registro)
    #print(info)
    return info

if __name__ == '__main__':
    list_email()