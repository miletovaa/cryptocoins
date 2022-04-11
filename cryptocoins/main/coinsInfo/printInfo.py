import pickle

try:
    with open('junoswap.pickle', 'rb') as f:
        print(pickle.load(f))
        print(f'\n')
except:
    print(f'[Junoswap is not loaded!]')
try:
    with open('sifchain.pickle', 'rb') as f:
        print(pickle.load(f))
        print(f'\n')
except:
    print(f'[Sifchain is not loaded!]')
try:
    with open('marbledao.pickle', 'rb') as f:
        print(pickle.load(f))
        print(f'\n')
except:
    print(f'[Marbledao is not loaded!]')
try:
    with open('osmosis.pickle', 'rb') as f:
        print(pickle.load(f))
        print(f'\n')
except:
    print(f'[Osmosis is not loaded!]')
