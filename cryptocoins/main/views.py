from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import pickle
from .coinsListReturn import CoinsListReturn


class MainPageView(View):
    def get(self, request):
        path = f'{settings.BASE_DIR}/main/coinsList.pickle'
        data = pickle.load(open(path, 'rb'))
        all_coins = []
        for el in data:
            all_coins += data[el]
        data['all_coins'] = set(all_coins)
        try:
            data['configs'] = pickle.load(open(f'{settings.BASE_DIR}/main/configs.pickle', 'rb'))

        except Exception as e:
            print(str(e))
        return render(request, 'main/mainpage.html', data)

    def post(self, request):
        main_coin = request.POST['mainCoin']
        values = [float(el) for el in request.POST['values'].split(' ') if el != '']
        junoswap = request.POST.getlist('junoswap')
        sifchain = request.POST.getlist('sifchain')
        marbledao = request.POST.getlist('marbledao')
        osmosis = request.POST.getlist('osmosis')
        data = {
            'main_coin': main_coin,
            'values': values,
            'add_coins': {
                'junoswap': junoswap,
                'sifchain': sifchain,
                'marbledao': marbledao,
                'osmosis': osmosis,
            }
        }
        pickle.dump(data, open(f'{settings.BASE_DIR}/main/configs.pickle', 'wb'))

        return redirect('/')
