# -*- coding: cp1251 -*-
import csv
import xlsxwriter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Высчитать k-Anonimity(1) или обезличить входной датасет(2)?")
print("Введите число:")
n = int(input())

center = [14,15,17,20,24,29,34,38,42,46,54,61,66,68,28,78,45]
sever = [86,87,11,55,19,27,41,47,49,58,40,]
sun = [79,82,26,83,85,91,90,96,30,7,12,60,]
volga = [80,88,89,92,94,97,33,22,53,56,57,48,36,63,73]
ural = [37,65,67,74,75]
sibir = [84,81,93,95,13,59,72,25,62,32,50,52,69,76,43]
west = [98,20,51,44,64,99,77]


def card(x):
    return x[0] + '*** **** **** ****'


def price(x):
    x = int(x[:-4])
    if x<=5000:
        return '<5000 руб.'
    elif x>5000 and x<=10000:
        return '5000-10000 руб.'
    elif x>10000 and x<=15000:
        return '10000-15000 руб.'
    elif x>15000 and x<=20000:
        return '15000-20000 руб.'
    else:
        return '>20000 руб.'


def place(x):
    if x[0] == "2" or x[0] == "3":
        return x[0] + "*"
    else:
        return "1*"


def region(x):
    x = int(x[:2])
    if x in center:
        return "Центральный федеральный округ"
    elif x in sever:
        return "Северо-Западный федеральный округ"
    elif x in sun:
        return "Южный федеральный округ"
    elif x in volga:
        return "Приволжский федеральный округ"
    elif x in ural:
        return "Уральский федеральный округ"
    elif x in sibir:
        return "Сибирский федеральный округ"
    elif x in west:
        return "Дальневосточный федеральный округ"
    return "Неопознанный регион"


pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

boolfio = 1
boolpassid = 1
boolplace = 1
boolprice = 1
boolcard = 1
boolpodavlenie = 0


df = pd.read_excel('txt2.xlsx', engine='openpyxl')
df.rename(columns=df.iloc[0])

if boolfio:
    df = df.drop(['ФИО'], axis='columns')
df = df.drop(['Вагон'], axis='columns')
df = df.drop(['место'], axis='columns')
if boolpassid:
    df['Паспортные данные'] = df["Паспортные данные"].apply(lambda x: region(x))
if boolprice:
    df['Стоимость'] = df['Стоимость'].apply(lambda x: price(x))
if boolplace:
    df['Тип вагона'] = df["Тип вагона"].apply(lambda x: place(x))

if boolcard:
    df['Карта'] = df['Карта'].apply(lambda x:card(x))



df.to_csv('filename.csv', index=False)

workbook = xlsxwriter.Workbook('kon.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'Паспортные данные')
worksheet.write(0, 1, 'Откуда')
worksheet.write(0, 2, 'Куда')
worksheet.write(0, 3, 'Дата отъезда')
worksheet.write(0, 4, 'Дата приезда')
worksheet.write(0, 5, 'Рейс')
worksheet.write(0, 6, 'Тип вагон')
worksheet.write(0, 7, 'Стоимость')
worksheet.write(0, 8, 'Карта')
tek = 1
mas = dict()
with open("filename.csv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        if line[0] in mas:
            mas[line[0]] += 1
        else:
            if i > 0:
                mas[line[0]] = 1
count = 0
minim = 100000
for i in mas:
    count += mas[i]
    minim = min(mas[i], minim)
plox_znach = set()
kanon = 7
tek = 1
with open("filename.csv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        a = list(map(str, line[-1].split(",")))
        if i > 0 and mas[line[0]] >= kanon:
            worksheet.write(tek, 0, a[0])
            worksheet.write(tek, 1, a[1])
            worksheet.write(tek, 2, a[2])
            worksheet.write(tek, 3, a[3])
            worksheet.write(tek, 4, a[4])
            worksheet.write(tek, 5, a[5])
            worksheet.write(tek, 6, a[6])
            worksheet.write(tek, 7, a[7])
            worksheet.write(tek, 8, a[8])
            tek += 1
        if i > 0 and mas[line[0]] <= 2:
            plox_znach.add((mas[line[0]], line[0]))
if n == 1:
    print("k-Anonimity =", minim)
else:
    print("k-Anonimity до подавления = ", minim, ", после подавления = ", kanon, sep="")
    print("Количество удаленных записей = ", count - tek + 1, " (", (count - tek + 1) / count * 100, "%)", sep="")
    print("Количество записей в новом датасете:", tek - 1)
    print("Плохие значения:")
    for i in plox_znach:
        print(i[0], i[1])
workbook.close()
