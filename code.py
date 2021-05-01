#код, который подключает данные из таблицы к консоли
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1fE_QFmx20-Ev21Al04JsqnTcwwQ-zyfcfb84L3vg72E'

service = build('sheets', 'v4', credentials = creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId = SPREADSHEET_ID,
                           range = "A1:B16").execute()

values = result.get('values', [])
#вывод необработанных данных
print(values)

##регулярное выражение, которое пока что не включено в работающий интерфейс, но работает при тестировании в блокноте
#[[ЁёА-Яа-я]*([Ее][Бб]|[Ёё][Бб]|[Бб][Лл][Яя][ТтДд]?|[Хх][Уу][еёйяюлЕЁЙЯЮЛ]|[пП][иИ][зЗ][джДЖ])[ЁёА-Яа-я]*
