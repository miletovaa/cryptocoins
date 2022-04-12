import xlsxwriter
from printInfo import get_prices
import pickle


def write():
    workbook = xlsxwriter.Workbook('pricesOfCoins.xlsx')
    worksheet = workbook.add_worksheet('Coins')

    data = get_prices()

    print(data)

    all_coins = []
    for el in data:
        if data[el] != None:
            for el2 in data[el]:
                all_coins.append(el2[0])
    all_coins = list(set(all_coins))

    for el in all_coins:
        worksheet.write(all_coins.index(el) + 2, 0, el)

    configs = pickle.load(open('configs.pickle', 'rb'))
    for i in range(len(configs['values'])):
        worksheet.merge_range(1, 10 * i + 2, 1, 10 * i + 6, str(configs['values'][i]))

    for i in range(len(configs['values'])*2):
        worksheet.write(0, 2+5*i, 'Osmosis')
        worksheet.write(0, 3+5*i, 'Emeris')
        worksheet.write(0, 4+5*i, 'Sifchain')
        worksheet.write(0, 5+5*i, 'Junoswap')
        worksheet.write(0, 6+5*i, 'Marbledao')

    if data['junoswap'] != None:
        for el in data['junoswap']:
            for i in range(1, len(el)):
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 5, el[i][1])
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 10, el[i][2])
    if data['sifchain'] != None:
        for el in data['sifchain']:
            for i in range(1, len(el)):
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 4, el[i][1])
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 9, el[i][2])
    if data['marbledao'] != None:
        for el in data['marbledao']:
            for i in range(1, len(el)):
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 6, el[i][1])
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 11, el[i][2])
    if data['osmosis'] != None:
        for el in data['osmosis']:
            for i in range(1, len(el)):
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 2, el[i][1])
                worksheet.write(all_coins.index(el[0]) + 2, 10 * (i - 1) + 7, el[i][2])

    workbook.close()
