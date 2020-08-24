from datetime import datetime


fromOneToThitry = {
    1:'минута {}',
    2: 'две минуты {}',
    3: 'три минуты {}',
    4: 'четыре минуты {}',
    5: 'пять минут {}',
    6: 'шесть минут {}',
    7: 'семь минут {}',
    8: 'восемь минут {}',
    9: 'девять минут {}',
    10: 'десять минут {}',
    11: 'одиннадцать минут {}',
    12: 'двенадцать минут {}',
    13: 'тринадцать минут {}',
    14: 'четырнадцать минут {}',
    15: 'пятнадцать минут {}',
    16: 'шестнадцать минут {}',
    17: 'семнадцать минут {}',
    18: 'восемнадцать минут {}',
    19: 'девятнадцать минут {}',
    20: 'двадцать минут {}',
    21: 'двадцать одна минута {}',
    22: 'двадцать две минуты {}',
    23: 'двадцать три минуты {}',
    24: 'двадцать четыре минуты {}',
    25: 'двадцать пять минут {}',
    26: 'двадцать шесть минут {}',
    27: 'двадцать семь минут {}',
    28: 'двадцать восемь минут {}',
    29: 'двадцать девять минут {}',
    30: 'половина {}'
}


from31To59 = {
    31: 'без двадцати девяти минут {}',
    32: 'без двадцати восьми минут {}',
    33: 'без двадцати семи минут {}',
    34: 'без двадцати шести минут {}',
    35: 'без двадцати пяти минут {}',
    36: 'без двадцати четырёх минут {}',
    37: 'без двадцати трех минут {}',
    38: 'без двадцати двух минут {}',
    39: 'без двадцати одной минуты {}',
    40: 'без двадцати минут {}',
    41: 'без девятнадцати минут {}',
    42: 'без восемнадцати минут {}',
    43: 'без семнадцати минут {}',
    44: 'без шестнадцати минут {}',
    45: 'без пятнадцати минут {}',
    46: 'без четырнадцати минут {}',
    47: 'без тринадцати минут {}',
    48: 'без двенадцати минут {}',
    49: 'без одиннадцати минут {}',
    50: 'без десяти минут {}',
    51: 'без девяти минут {}',
    52: 'без восьми минут {}',
    53: 'без семи минут {}',
    54: 'без шести минут {}',
    55: 'без пяти минут {}',
    56: 'без четырех минут {}',
    57: 'без трёх минут {}',
    58: 'без двух минут {}',
    59: 'без одной минуты {}',
}

hours1 = {
    1: 'первого',
    2: 'второго',
    3: 'третьего',
    4: 'четвертого',
    5: 'пятого',
    6: 'шестого',
    7: 'седьмого',
    8: 'восьмого',
    9: 'девятого',
    10: 'десятого',
    11: 'одиннадцатого',
    12: 'двенадцатого'
}

hours2 = {
    1: 'час',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать'
}

print('Hi! Do you want to enter your time (Y) or choose a systeam time (S) ?')
mode = input('Plese, choose and write short form here (Y/S): ')
while True: 

    if mode=='Y':
        timeStr = input('Ok, input your time here: ')
        if timeStr.find(':')==-1 or len(timeStr)!=5:
            print('You wrote strange time. Please, use this format XX:YY')
            continue
        timeStr = timeStr.split(':')
        hour = int(timeStr[0]) - 12 if int(timeStr[0]) > 12 else int(timeStr[0])
        minute = int(timeStr[1])
    elif mode=='S':
        currentTime = datetime.now()
        hour = currentTime.hour - 12 if currentTime.hour > 12 else currentTime.hour
        minute = currentTime.minute
    else:
        print('You input wrong mode! Try again...')
        mode = input('choose mode (Y/S): ')
        continue


    if fromOneToThitry.get(minute):
        print('Сейчас '+ fromOneToThitry[minute].format(hours1[hour + 1 if hour!=12 else hour-11 ]))
    elif from31To59.get(minute):
        print('Сейчас '+ from31To59[minute].format(hours2[hour + 1 if hour!=12 else hour-11 ]))
    else:
        print('Сейчас '+ hours2[hour if hour!=0 else 12] + ' часов ')

    act = input('If you wont to finish the program - write \'E\', to change mode - write \'M\', to continue - press ENTER: ')
    if act  == 'E':
        print('Bye-bye')
        break
    elif act == 'M':
        mode = input('choose mode (Y/S): ')