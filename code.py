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
                           range = "A2:A55").execute()

result2 = sheet.values().get(spreadsheetId = SPREADSHEET_ID,
                           range = "B2:D50").execute()

values1 = result1['values']
dirty = [item for sublist in values1 for item in sublist]
#print(dirty)

values2 = result2['values']
clean = [item for sublist in values2 for item in sublist]
#print(clean)

#вывод необработанных данных


def check(i):
    a = re.match('[[ЁёА-Яа-я\!\"\'\,\-\.\\\:\;\?]*([Ее][Бб]|[Ёё][Бб]|[Бб][Лл][Яя][ТтДд]?|[Хх][Уу][еёйяюлЕЁЙЯЮЛ]|[пП][иИ][зЗ][дД])[ЁёА-Яа-я\!\"\'\,\-\.\\\:\;\?]*', i)
    state = True
    if a != None:
        a = a.group(0)
        for j in dirty:
            e = re.findall(j, a)
            if e != []:
                print("Ваше сообщение было заблокировано.")
                state = False
        if state == True:
            for h in clean:
                f = re.findall(h, a)
                if f != []:
                    state = True
                    break
                else:
                    state = False
            if state == False:
                print("Ваше сообщение было отправлено на рассмотрение модератору.")
            #тут мы говорим о том что модератора никакого нет на самом деле и типа да у нас проект как бы в консоли только
    return state
def print_message(chat):
    state = True
    for i in chat.split(" "):
        if check(i) == True:
            continue
        else:
            state = False
            break
    if state == True:
        print(chat)
        return True
message = input("Введите свое сообщение: ")
if print_message(message) == True:
    moderator = input("Помогите нам развить нашу программу. Считаете ли Вы, что в Вашем сообщении присутствует какая-либо ненормативная лексика? Если да, пожалуйста, введите в поле слово 'clean'. Если нет, пожалуйста, введите в поле вызвавшее сомнения слово.")
    if moderator != 'clean':
        print("Спасибо! Ваше сообщение было отправлено на рассмотрение модератору.")
