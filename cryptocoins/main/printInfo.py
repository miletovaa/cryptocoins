import pickle


def get_prices():
    data = {}
    try:
        with open('junoswap.pickle', 'rb') as f:
            data['junoswap'] = pickle.load(f)
            # print(data['junoswap'])
            # print(f'\n')
    except:
        data['junoswap'] = None
        print(f'[Junoswap is not loaded!]')
    try:
        with open('sifchain.pickle', 'rb') as f:
            data['sifchain'] = pickle.load(f)
            # print(data['sifchain'])
            # print(f'\n')
    except:
        data['sifchain'] = None
        print(f'[Sifchain is not loaded!]')
    try:
        with open('marbledao.pickle', 'rb') as f:
            data['marbledao'] = pickle.load(f)
            # print(data['marbledao'])
            # print(f'\n')
    except:
        data['marbledao'] = None
        print(f'[Marbledao is not loaded!]')
    try:
        with open('osmosis.pickle', 'rb') as f:
            data['osmosis'] = pickle.load(f)
            # print(data['osmosis'])
            # print(f'\n')
    except:
        data['osmosis'] = None
        print(f'[Osmosis is not loaded!]')
    try:
        with open('crescent.pickle', 'rb') as f:
            data['crescent'] = pickle.load(f)
            # print(data['osmosis'])
            # print(f'\n')
    except:
        data['crescent'] = None
        print(f'[Crescent is not loaded!]')
    return data