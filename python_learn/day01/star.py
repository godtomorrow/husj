# -*- coding:utf-8 -*-

sdate=[21,20,21,21,22,22,23,24,24,24,23,22]
conts=['摩羯座','水瓶座','mo','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座']
signs=['☼','☽','♀','✔','卍','㉿','♑','♓','♉','♈','♊','☡','☽']

birth = input('请输入年月日').strip(' ')
cbir = birth.split('-')
cmonth = str(cbir[1])
cdate = str(cbir[2])
def sign(cmonth, cdate):
    if int(cdate)<sdate[int(cmonth)-1]:
        print(conts[int(cmonth)-1])
        print(signs[int(cmonth)-1])
    else:
        print(conts[int(cmonth)])
        print(signs[int(cmonth)])
sign(cmonth,cdate)