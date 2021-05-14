import re

clean = ['реб', 'оскорбля', 'собля', 'слабля', 'глубля' ,'любля' ,'губля' ,'подобля' ,'грубля' ,'знобля' ,'злобля' ,'щербля' ,'столбля' ,'робля' ,'рабля' ,'блям', 'бляц', 'бляш' ,'блях' ,'обляпа' ,'аблятивн' ,'себ' ,'неб' ,'меб' ,'чеб' ,'леб' ,'деб' ,'веб' ,'жеб' ,'шеб' ,'скобля' ,'страху' ,'штриху' ,'впихуем' ,'психу' ,r'ухую\b' , r'тихую\b', r'ветхую\b', r'брюхую\b' ,r'верхую\b' ,'теб' ,'щеб' ,'лёб' ,'рёб' ,'тёб' ,'рубля' ,'сабля' ,'самбля' ,'гребля' ,'жабля' ,'дубляж' ,'коннетабля' ,'оглобля']
dirty = [r'\bблять\b', 'бляд', r'\bбля\b', r'\bхуй', r'\bхуя', r'\bхую', r'\bхуем', r'\bхуём', r'\bхуе', r'\bхуи', r'\bхуей', r'\bхуев', r'\bхуёв', r'\bхуям', r'\bхуями', r'\bхуях', 'пизд', 'пезд', 'пёзд', r'\bеб', r'\bёб', 'ъеб', 'ъёб', 'ьеб', 'ьёб', 'хуйн', 'пизж', 'бляхер', 'долбоеб', 'долбоёб', 'долбаеб', 'долбаёб', 'поеб', 'поёб', 'проеб', 'проёб', 'доеб', 'доёб', 'заеб', 'заёб', 'наеб', 'наёб', 'перееб', 'переёб', 'уеб', 'уёб', 'выеб', 'выёб', 'приеб', 'приёб']


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
a = input("Введите любую последовательность символов чтобы выйти: ")
