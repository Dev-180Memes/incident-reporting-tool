import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database/incident_reports.db')
SECRET_KEY = "your-secret-key"
