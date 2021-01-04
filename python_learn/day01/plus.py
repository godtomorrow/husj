# -*- coding:utf-8 -*-

all = 0.0
alladd = 0.0
indig = ''

def add(addin,data):
    addone = 0
    addone = addin + data
    return addone

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError,ValueError):
        pass

    return False

while True:
    indig = input('输入： ').strip('')
    if indig == 'q' or indig == 'Q':
        break
    elif is_number(indig) == True:
        alladd = add(float(all), float(indig))
        all = format(alladd, '.2f')
        print(all)
    else:
        print("输入数字不合法，请正确输入。")
