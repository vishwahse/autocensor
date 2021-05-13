import re
from pprint import pprint

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
result1 = sheet.values().get(spreadsheetId = SPREADSHEET_ID,
                           range = "A2:A392").execute()

result2 = sheet.values().get(spreadsheetId = SPREADSHEET_ID,
                           range = "B2:B392").execute()

values1 = result1['values']
dirty = [item for sublist in values1 for item in sublist]
#print(dirty)

values2 = result2['values']
clean = [item for sublist in values2 for item in sublist]
#print(clean)

#вывод необработанных данных


def check(i):
    a = re.match('[[ЁёА-Яа-я]*([Ее][Бб]|[Ёё][Бб]|[Бб][Лл][Яя][ТтДд]?|[Хх][Уу][еёйяюлЕЁЙЯЮЛ]|[пП][иИ][зЗ][дД])[ЁёА-Яа-я]*', i)
    state = True
    if a != None:
        a = a.group(0)
        if a in dirty:
            print("Ваше сообщение было зацензурено")
            state = False
        elif a in clean:
            state = True
        else:
            print("Ваше сообщение было отправлено на рассмотрение модератору")
            state = False
            #тут мы говорим о том что модератора никакого нет на самом деле и типа да у нас проект как бы в консоли только
    return state
def print_message(message):
    state = True
    for i in message.split(" "):
        if check(i) == True:
            continue
        else:
            state = False
            break
    if state == True:
        print("С вашим сообщением все хорошо!")
message = input("Введите свое сообщение: ")
print_message(message)
