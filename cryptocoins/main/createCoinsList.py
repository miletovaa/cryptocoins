from getInfoOfCoins import getInfo
import pickle

data = {
    'junoswap': getInfo.JunoSwap.get_all_coins(),
    'sifchain': getInfo.Sifchain.get_all_coins(),
    'marbledao': getInfo.Marbledao.get_all_coins(),
}

try:
    data['osmosis'] = getInfo.Osmosis.get_all_coins()
except:
    print(f'[Osmosis is not loaded!]')
with open('coinsList.pickle', 'wb') as f:
    pickle.dump(data, f)
