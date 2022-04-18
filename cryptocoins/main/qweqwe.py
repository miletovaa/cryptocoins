import openpyxl
#
book = openpyxl.load_workbook('test.xlsx')
sheet = book.active
sheet['A1'].value = 12
sheet['B1'].value = 15
sheet['C1'].value = '=A1+B1'
book.save('test.xlsx')



# book = openpyxl.load_workbook('test.xlsx', data_only=True)
# sheet = book.active
#
# print(sheet['C1'].value)