import openpyxl
from xlsx_writer import save_xlsx_file


def saveTransactionValues(diction):
    swap = True
    workbook = openpyxl.load_workbook('result.xlsx')
    worksheet = workbook.active
    for el in diction:
        print(diction[el] if swap else diction[el][::-1])
        if swap:
            worksheet['EA4'] = diction[el][0][0]
            worksheet['EA5'] = diction[el][1][0]
            worksheet['EB3'] = el
            worksheet['EB4'] = diction[el][0][1]
            worksheet['EB5'] = diction[el][1][1]
        else:
            worksheet['EC3'] = el
            worksheet['EC4'] = diction[el][1][1]
            worksheet['EC5'] = diction[el][0][1]
        swap = False
    workbook.save('result.xlsx')
    workbook.close()

    save_xlsx_file()


# saveTransactionValues({'junoswap': [['ust', 0.05305], ['atom', 0.000651]], 'osmosis': [['atom', 0.001], ['ust', 124124]]})