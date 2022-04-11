from django.shortcuts import render
from django.views import View
import pickle
from .coinsListReturn import CoinsListReturn


class MainPageView(View):
    def get(self, request):
        data = {
            'junoswap': ['juno', 'atom', 'ust', 'btsg', 'luna', 'osmo', 'stars', 'huahua', 'akt', 'xprt', 'cmdx', 'dig',
                         'scrt', 'neta', 'canlab', 'tuck', 'hulc', 'bcna', 'hope', 'rac', 'marble', 'coin', 'primo',
                         'daisy', 'future', 'bfot', 'phmn', 'arto'],
            'sifchain': ['rowan', '1inch', 'aave', 'akro', 'akt', 'ant', 'atom', 'axs', 'b20', 'bal', 'band', 'bat',
                         'bnt', 'bond', 'btsg (erc-20)', 'cocos', 'comp', 'conv', 'cream', 'cro', 'csms', 'dai',
                         'daofi', 'dfyn', 'dino', 'dnxc', 'don', 'dvpn', 'eeur', 'enj', 'ern', 'esd', 'eth', 'frax',
                         'ftm', 'fxs', 'grt', 'iotx', 'iris', 'ixo', 'juno', 'keep', 'kft', 'ldo', 'leash', 'lgcy',
                         'lina', 'link', 'lon', 'lrc', 'luna', 'mana', 'matic', 'metis', 'ngm', 'ocean', 'ogn', 'oh',
                         'osmo', 'paid', 'pols', 'pond', 'quick', 'rail', 'ratom', 'reef', 'regen', 'rfuel', 'rly',
                         'rndr', 'rune', 'saito', 'sand', 'shib', 'snx', 'srm', 'susd', 'sushi', 'sxp', 'tidal', 'toke',
                         'tshp', 'tusd', 'ufo', 'uma', 'uni', 'usdc', 'usdt', 'ust', 'ust', 'wbtc', 'wfil', 'wscrt',
                         'xprt', 'yfi', 'zcn', 'zcx', 'zrx'],
            'marbledao': ['block', 'marble', 'juno', 'atom', 'ust', 'luna', 'osmo', 'scrt', 'neta']}

        return render(request, 'main/mainpage.html', data)
