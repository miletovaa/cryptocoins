from getInfoOfCoins import getInfo
import pickle

data = {}
try:
    data['marbledao'] = getInfo.Marbledao.get_all_coins()
except Exception as e:
    print(f'[Marbledao is not loaded! ({str(e)[:50]})]')
try:
    data['sifchain'] = getInfo.Sifchain.get_all_coins()
    print(data['sifchain'])
except Exception as e:
    print(f'[Sifchain is not loaded! ({str(e)[:50]})]')

try:
    data['junoswap'] = getInfo.JunoSwap.get_all_coins()
except Exception as e:
    print(f'[Junoswap is not loaded! ({str(e)[:50]})]')

try:
    data['osmosis'] = getInfo.Osmosis.get_all_coins()
except Exception as e:
    print(f'[Osmosis is not loaded! ({str(e)[:50]})]')

try:
    data['crescent'] = getInfo.Crescent.get_all_coins()
except Exception as e:
    print(f'[Crescent is not loaded! ({str(e)[:50]})]')

with open('coinsList.pickle', 'wb') as f:
    pickle.dump(data, f)
