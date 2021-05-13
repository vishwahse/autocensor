import re

dirty = ['блядь', 'бляди', 'блядью', 'блядей', 'блядям', 'блядями', 'блядях', 'блять', 'бля', 'хуй', 'хуя', 'хую', 'хуем', 'хуём', 'хуе', 'хуи', 'хуей', 'хуев', 'хуёв', 'хуям', 'хуями', 'хуях', 'пизда', 'пизды', 'пизде', 'пизду', 'пиздой', 'пезды', 'пёзды', 'пизд', 'пезд', 'пёзд', 'пиздам', 'пездам', 'пёздам', 'пиздами', 'пездами', 'пёздами', 'пиздах', 'пездах', 'пёздах', 'ебать', 'ебу', 'ебешь', 'ебёшь', 'ебет', 'ебёт', 'ебем', 'ебём', 'ебете', 'ебёте', 'ебут', 'ебал', 'ебала', 'ебало', 'ебали', 'пиздец', 'пиздеца', 'пиздецу', 'пиздецом', 'пиздеце', 'пиздецы', 'пиздецов', 'пиздецам', 'пиздецами', 'пиздецах', 'хуйня', 'хуйни', 'хуйне', 'хуйню', 'хуйней', 'хуйни', 'хуйней', 'хуйнь', 'хуйням', 'хуйнями', 'хуйнях', 'блядский', 'блядского', 'блядскому', 'блядским', 'блядском', 'блядская', 'блядской', 'блядскую', 'блядское', 'пиздить', 'пизжу', 'пиздишь', 'пиздит', 'пиздим', 'пиздите', 'пиздят', 'пиздел', 'пиздил', 'пиздела', 'пиздила', 'пиздело', 'пиздило', 'пиздели', 'пиздили', 'пиздеть', 'проебать', 'проебу', 'проебешь', 'проебёшь', 'проебет', 'проебёт', 'проебем', 'проебём', 'проебете', 'проебёте', 'проебут', 'проебал', 'проебала', 'проебало', 'проебали', 'еби', 'проеби', 'ебя', 'проебя', 'ебав', 'проебав', 'ебавший', 'ебаный', 'ебанный', 'ёбаный', 'ёбанный', 'проебавший', 'проебаный', 'проебанный', 'проёбаный', 'проёбанный', 'спиздить', 'спизжу', 'спиздишь', 'спиздит', 'спиздим', 'спиздите', 'спиздят', 'спиздел', 'спиздил', 'спиздела', 'спиздила', 'спиздело', 'спиздило', 'спиздели', 'спиздили', 'спиздеть', 'ебануть', 'ебану', 'ебанешь', 'ебанёшь', 'ебанет', 'ебанёт', 'ебанем', 'ебанём', 'ебанете', 'ебанёте', 'ебанут', 'ебанул', 'ебанула', 'ебануло', 'ебанули', 'ебануться', 'ебанусь', 'ебанешься', ' ебанёшься', 'ебанется', 'ебанётся', 'ебанемся', 'ебанёмся', 'ебанетесь', 'ебанётесь', 'ебанутся', 'ебанулся', 'ебанулась', 'ебанулось', 'ебанулись', 'ебанувший', 'ебанувшего', 'ебанувшему', 'ебанувшим', 'ебанувшем', 'ебанувшие', 'ебанувших', 'ебанувшим', 'ебанувшими', 'ебанувшая', 'ебанувшей', 'ебанувшей', 'ебанувшую', 'ебанувшее', 'ебанувшийся', 'ебанувшегося', 'ебанувшемуся', 'ебанувшимся', 'ебанувшемся', 'ебавшего', 'ебавшему', 'ебавшим', 'ебавшем', 'ебавшее', 'ебавшая', 'ебавшей', 'ебавшую', 'ебаного', 'ебанного', 'ёбаного', 'ёбанного', 'ебаному', 'ебанному', 'ёбаному', 'ёбанному', 'ебаным', 'ебанным', 'ёбаным', 'ёбанным', 'ебаном', 'ебанном', 'ёбанном', 'ёбаном', 'ебаное', 'ебанное', 'ёбаное', 'ёбанное', 'ебаная', 'ебанная', 'ёбанная', 'ёбаная', 'ебаной', 'ебанной', 'ёбаной', 'ёбанной', 'ебаную', 'ебанную', 'ёбаную', 'ёбанную', 'проебавшего', 'проебавшему', 'проебавшим', 'проебавшем', 'проебавшее', 'проебавшая', 'проебавшей', 'проебавшую', 'проебаного', 'проебанного', 'проёбаного', 'проёбанного', 'проебаному', 'проебанному', 'проёбаному', 'проёбанному', 'проебаным', 'проебанным', 'проёбаным', 'проёбанным', 'проебаном', 'проебанном', 'проёбанном', 'проёбаном', 'проебаное', 'проебанное', 'проёбаное', 'проёбанное', 'проебаная', 'проебанная', 'проёбанная', 'проёбаная', 'проебаной', 'проебанной', 'проёбаной', 'проёбанной', 'проебаную', 'проебанную', 'проёбаную', 'проёбанную', 'доебаться', 'доебусь', 'доебешься', 'доебёшься', 'доебется', 'доебётся', 'доебемся', 'доебёмся', 'доебетесь', 'доебётесь', 'доебутся', 'доебался', 'доебалась', 'доебалось', 'доебались', 'доебавшийся', 'доебавшегося', 'доебавшемуся', 'доебавшимся', 'доебавшемся', 'доебавшиеся', 'доебавшихся', 'доебавшимся', 'доебавшимися', 'доебавшаяся', 'доебавшейся', 'доебавшуюся', 'доебавшееся', 'ебало', 'ебалом', 'ебалу', 'ебала', 'ебале', 'ебло', 'ебле', 'еблу', 'еблом', 'ебла', 'ёбла ', 'ебашить ', 'ебашу', 'ебашит', 'ебашишь', 'ебашите', 'ебашат', 'ебашил', 'ебашила', 'ебашило', 'ебашили', 'ебавший', 'ебавшая', 'ебавшие', 'ебавшее', 'заебать ', 'заебало', 'заебал', 'заебала', 'заебали', 'заебавший', 'заебавшая', 'заебавшеее', 'заебавшие', 'заебись', 'изъебнуться', 'изъебнулся', 'изъебнулась', 'изъебнулись', 'наебашиться', 'наебашился', 'наебашилась', 'наебашились', 'наебашусь', 'наебашишься', 'наебашится', 'наебашимся', 'наебашатся', 'пиздабол', 'пиздабола', 'пиздаболу', 'пиздаболом', 'пиздаболе', 'пиздаболка', 'пиздаболки', 'пиздаболку', 'пиздаболкой', 'пиздаболке', 'пиздатый', 'пиздатая', 'пиздатое', 'пиздатого', 'пиздатую', 'пиздатой', 'пиздатому', 'пиздатым', 'пиздатой', 'пиздатом', 'пиздатые', 'пиздатым', 'пиздатыми', 'пиздатых']
clean = ['оскорблять', 'употреблять', 'обособлять', 'ослаблять', 'углублять', 'влюблять', 'расслаблять', 'потреблять', 'злоупотреблять', 'усугублять', 'уподоблять', 'пособлять', 'истреблять', 'подсоблять', 'огрублять', 'влюбляться', 'озноблять', 'озлоблять', 'послаблять', 'загублять', 'приспособлять', 'ущерблять', 'возлюблять', 'погублять', 'заглублять', 'пригублять', 'застолблять', 'угроблять', 'ограблять', 'раздроблять', 'поистреблять', 'блямба', 'блямбочка', 'бляшка', 'бляха', 'блям', 'бляхин', 'блямс', 'блямцать', 'хлеб', 'погреб', 'взахлеб', 'взахлёб', 'ястреб', 'погрёб', 'стёб', 'небоскреб', 'небоскрёб', 'ширпотреб', 'водохлеб', 'водохлёб', 'рубля', 'сабля', 'ассамбляж', 'ансамбля', 'гребля', 'дирижабля', 'дубляж', 'жабляк', 'коннетабля', 'обляпать', 'оглобля', 'теребля', 'аблятивный', 'абляция', 'корабля', 'констебля', 'себя', 'себе', 'ребенок', 'ребенка', 'требовать', 'требует', 'требуется', 'требования', 'небольшой', 'мебели', 'требований', 'мебель', 'требованиям', 'ребенку', 'требуют', 'потребителей', 'потребуется', 'ребята', 'небольшие', 'потребности', 'учебных', 'небольших', 'колебля', 'ребенком', 'потребления', 'ребёнка', 'пребывания', 'учебного', 'потребностей', 'потребность', 'ребят', 'небо', 'небольшая', 'требованиями', 'небольшое', 'небольшим', 'судебных', 'небольшого', 'требование', 'небольшую', 'потребителя', 'употребление', 'употребления', 'судебного', 'требовать', 'ребёнок', 'потребление', 'неба', 'небольшом', 'учебной', 'учебный', 'небе', 'учебные', 'судебной', 'небольшими', 'требуются', 'учебном', 'судебном', 'учебы', 'потребуется', 'колебания', 'серебра', 'требованию', 'лечебных', 'мебелью', 'колебаний', 'употреблении', 'судебные', 'небом', 'ребятам', 'пребывание', 'колеблется', 'востребованы', 'потребовать', 'потребностям', 'потребители', 'себестоимость', 'серебро', 'потребительских', 'потребителям', 'себестоимости', 'требовалось', 'ребёнку', 'свадебного', 'требуется', 'потребителю', 'потребовал', 'веб', 'потребительского', 'потребитель', 'служебных', 'учебу', 'востребованных', 'потребоваться', 'требующих', 'лечебные', 'учебное', 'неблагоприятных', 'свадебные', 'требовали', 'потребуются', 'лечебного', 'свадебных', 'лечебной', 'учебники', 'учебник', 'потребностями', 'учебника', 'учебника', 'употребляют', 'требующие', 'свадебный', 'учебников', 'потребовалось', 'требовал', 'судебный', 'судебное', 'ребёнком', 'волшебный', 'ребятами', 'учебе', 'потребителями', 'Роспотребнадзор', 'пребывает', 'востребованным', 'употребляется', 'пасодобля', 'приспособляемость', 'разграблять', 'скоблят', 'служебной', 'небес', 'учебным', 'свадебное', 'требуя', 'потребительские', 'потребовали', 'небу', 'востребована', 'требующий', 'лечебный', 'ребра', 'потребителем', 'хлебом', 'требованиях', 'употреблению', 'употреблением', 'служебного', 'стебли', 'судебная', 'ребенке', 'потребительской', 'волшебные', 'щебня', 'свадебной', 'востребованной', 'требуемых', 'волшебной', 'востребованными', 'хребта', 'дебиторской', 'серебряные', 'пренебрегать', 'востребован', 'потребительский', 'требуемой', 'потребляет', 'щебень', 'требовала', 'судебным', 'мебельных', 'требующая', 'вебинар', 'потреблять', 'мебельной', 'злоупотребления', 'учеба', 'серебряных', 'хребет', 'требуемого', 'лечебное', 'молебен', 'серебряный', 'пребывать', 'потребовала', 'служебные', 'учебнике', 'небесных', 'волшебство', 'учебниках', 'небесах', 'истребителей', 'востребованные', 'учебными', 'небесах', 'волшебных', 'учебная', 'судебную', 'серебром', 'небесной', 'потреблении', 'дебют', 'употребляет', 'злоупотребление', 'ребер', 'потребуют ', 'веб-сайта', 'бесперебойного', 'потребляют', 'потребностью', 'лечебная', 'учёбы', 'ребятишек', 'волшебное', 'волшебным', 'учебному', 'требуемые', 'неблагоприятные', 'колебаться', 'энергопотребления', 'серебряной', 'потреблением', 'роспотребнадзора']
dirty1 = ['*оскорбля* ', '*реб* ', '*собля* ', '*слабля* ', '*глубля*', '*любля* ', '*губля* ', '*подобля* ', '*грубля* ', '*знобля*', '*злобля* ', '*щербля* ', '*столбля* ', '*гробля* ', '*рабля* ', '*дробля* ', '*блям*', '*бляц*', '*бляш*', '*блях* (не -ер, не -уй, -уе, -ую, -уё, -уя)', '*обляпа*', '*аблятивн*', '*себ*', '*неб*', '*меб*', '*чеб*', '*леб*', '*деб*', '*веб*', '*жеб*', '*шеб*', '*скобля*', '*страху*', '*штриху*', '*впихуем*', '*психу*', '*ухую', '*тихую', '*ветхую', '*брюхую', '*верхую', '*теб*', '*щеб*', '*лёб*', '*рёб*', '*тёб*', '*рубля* не д', '*сабля* не д', '*самбля* не д', '*гребля* не д', '*жабля* не д', '*дубляж*', '*коннетабля*', '*оглобля*']
clean1 = ['*бляд*', 'блять', 'бля', 'хуй', 'хуя', 'хую', 'хуем', 'хуём', 'хуе', 'хуи', 'хуей', 'хуев', 'хуёв', 'хуям', 'хуями', 'хуях', '*пизд*', '*пезд*', '*пёзд*', 'еб*', 'ёб*', '*ъеб*', '*ъёб*', '*ьеб*', '*ьёб*', '*хуйн*', '*пизж*', '*долбоеб*', '*долбоёб*', '*долбаеб*', '*долбаёб*', '*поеб*', '*поёб*', '*проеб*', '*проёб*', '*доеб*', '*доёб*', '*заеб*', '*заёб*', '*наеб*', '*наёб*', '*перееб*', '*переёб*', '*уеб*', '*уёб*', '*выеб*', '*выёб*', '*приеб*', '*приёб*']

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
