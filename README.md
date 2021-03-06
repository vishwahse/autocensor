ССЫЛКА НА ПАПКУ С ПРОЕКТОМ: https://drive.google.com/drive/u/1/folders/148aRqykcZvFC-0S_8svow7aszaHE2wAF
ССЫЛКА НА ТАБЛИЦУ: https://docs.google.com/spreadsheets/d/1fE_QFmx20-Ev21Al04JsqnTcwwQ-zyfcfb84L3vg72E/edit#gid=0

# Автоцензор

## Подробное описание

Наш проект будет представлять из себя консольную программу, которая работает следующим образом:
1) Принимается сообщение от пользователя;
2) Оно разбивается на отдельные слова (разбивка по пробельным символам);
3) Каждое слово проходит проверку специальным регулярным выражением, нацеленным на поиск обсценной лексики (выражение настроено исключительно на поиск одного из четырёх корней, признанных в русском языке максимально нецензурными);
4) В случае, если регулярное выражение не срабатывает — переход к следующему слову. Если ни одно из слов не подошло под регулярное выражение — сообщение печатается без изменений, переход к пункту 9.
5) В случае, если регулярное выражение срабатывает, слово отправляется на проверку в так называемый блэк-лист (список, где собраны некоторые регулярные выражения, кодирующие ненормативные словоформы из ресурсов словаря русского мата (http://www.russki-mat.net/e/mat_slovar.htm), а также репозиториев (https://github.com/text-machine-lab/sentimental/blob/..), точно являющиеся обсценной лексикой). В случае, если слово оказывается в блэк-листе — программа печатает текст «Ваше сообщение было заблокировано», переход к пункту 9.
6) Если слово не находится в блэк-листе, оно отправляется на проверку в уайт-лист (список, где с помощью написанного регулярного выражения собраны некоторые регулярные выражения, кодирующие найденные словоформы из корпуса Aranea (), подходящие под это регулярное выражение, но являющиеся обычными, не обсценными словами(напр. вислоухую, сухую, глухую -> ухую\b)).
7) Если слово находится в уайт-листе — см. пункт 4.
8) Если слово не находится в уайт-листе, то все сообщение вместе с выделенным словом отправляется на проверку модератору. Программа печатает текст «Ваше сообщение было отправлено на рассмотрение модератору». После проверки модератор вручную вносит спорное слово либо в уайт-лист, либо в блэк-лист.
9) Также в программе предусмотрена система репортов. После прохождения пунктов 1-8 программа задает пользователю вопрос, не считает ли он какое-либо слово в сообщении недопустимым. Если нет, пользователь вводит кодовое слово «clean». Если да, пользователь вводит слово из сообщения, которое он считает неподобающим. Это слово также отправляется на проверку модератору и впоследствии попадет либо в уайт-, либо в блэк-лист.

## Критерий завершенного проекта
1) Наличие охватывающего как можно большее количество неподходящих слов регулярного выражения.
2) Наличие как можно более полных по содержанию уайт- и блэк-листов.
3) Наличие работающего кода, связанного с этими листами и как можно более точно отыскивающего обсценную лексику.
4) Проверка этого кода на практике, на корпусах (https://www.kaggle.com/blackmoon/russian-language-tox.., https://www.kaggle.com/alexandersemiletov/toxic-russi..)

## Команда проекта

- Тушевская Ксения, БКЛ-201
- Давлеева Варвара, БКЛ-201
- Кумараге Вишва, БКЛ-201

## Таймлайн проекта

- Апрель 20 - полноценная идея
- Апрель 28 - работающее регулярное выражение
- Апрель 30 - законченный полноценный план
- Май 3 - полный блэк-лист
- Май 6 - полный уайт-лист
- Май 9 - законченный, работающий код
- Май 10 - проверка код на корпусе Toxic Russian Comments (https://www.kaggle.com/alexandersemiletov/toxic-russian-comments)
- Май 12 - подготовка презентации
- Май 15 - защита проекта

## Чего вам не хватает для реализации проекта
На данный момент мы не можем прикрепить наш проект к настоящему чату или форуму, ограничиваясь консольной программой. В связи с этим, пункт №9 из подробного описания нельзя реализовать с настоящим взаимодействием пользователей между собой, из-за чего он работает ограниченнее, чем мог бы. Также по очевидным причинам невозможно любое взаимодействие с модератором.

## Распределение обязанностей в команде

- Тушевская Ксения - подготовка идеи, регулярное выражение, написание блэк-листа, написание уайт-листа, редактура кода, презентация
- Давлеева Варвара - подготовка идеи, регулярное выражение, написание блэк-листа, написание уайт-листа, редактура кода, презентация
- Кумараге Вишва - подготовка идеи, написание уайт-листа, подготовка основного кода, презентация
