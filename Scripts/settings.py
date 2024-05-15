from dotenv import load_dotenv
import os
from datetime import datetime, time


# Get the full path of the current file
full_path = os.path.abspath(__file__)
# print("Full path:", full_path)

# Truncate the path to two folders up
project_folder_path = os.path.dirname(os.path.dirname(full_path))
# print("Two folders up:", PYAO_path)

csv_folder_path = os.path.join(project_folder_path,'CSVs',)

def load_env_var():
    load_dotenv(os.path.join(project_folder_path,'ENV.env'))
    # load_dotenv(r'C:\Script\PYAO-main\AutoOffer\PYAO.env')

load_env_var()



chromeDrivePath = os.path.join(project_folder_path, 'chromedriver.exe')
firefoxDrivePath = r'C:\Program Files\Mozilla Firefox\firefox.exe'

IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
GHL_USERNAME = os.getenv('GHL_USERNAME')
GHL_PASSWORD = os.getenv('GHL_PASSWORD')
FOLDER_NAME = 'GHL_Security_Code'
HAR_USERNAME = os.getenv('HAR_username')
HAR_PASSWORD = os.getenv('HAR_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_KEY')


db_host = 'localhost'
db_user = 'root'
db_password = os.getenv('DB_PASSWORD')
db_name = 'auto_offer'
db_table_name = 'property'


