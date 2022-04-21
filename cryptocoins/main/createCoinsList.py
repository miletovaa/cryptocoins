from getInfoOfCoins import getInfo
import pickle

data = {}
try:
    data['marbledao'] = getInfo.Marbledao.get_all_coins()
except:
    print(f'[Marbledao is not loaded!]')

try:
    data['sifchain'] = getInfo.Sifchain.get_all_coins()
except:
    print(f'[Sifchain is not loaded!]')

try:
    data['junoswap'] = getInfo.JunoSwap.get_all_coins()
except:
    print(f'[Junoswap is not loaded!]')

try:
    data['osmosis'] = getInfo.Osmosis.get_all_coins()
except:
    print(f'[Osmosis is not loaded!]')

try:
    data['crescent'] = getInfo.Crescent.get_all_coins()
except:
    print(f'[Crescent is not loaded!]')
with open('coinsList.pickle', 'wb') as f:
    pickle.dump(data, f)
