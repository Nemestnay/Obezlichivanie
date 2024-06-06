import csv
import xlsxwriter
import pandas as pd
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
        if line in mas:
            mas[line] += 1
        else:
            if i > 0:
                mas[line] = 1
        a = list(map(str, line[-1].split(",")))
        '''
        if i > 0:
            for j in range(int(a[-1]) + 1):
                worksheet.write(tek, 0, a[1])
                worksheet.write(tek, 1, a[2])
                worksheet.write(tek, 2, a[3])
                worksheet.write(tek, 3, a[4])
                worksheet.write(tek, 4, a[5])
                worksheet.write(tek, 5, a[6])
                worksheet.write(tek, 6, a[7])
                worksheet.write(tek, 7, a[8])
                worksheet.write(tek, 8, a[9])
                tek += 1
        #print(i, a[-1], a)
        '''
count = 0
for i in mas:
    count += mas[i]
print(i)
workbook.close()
