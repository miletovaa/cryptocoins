from swapCoins import SwapCoins
from multiprocessing import Process, Manager
from saveTransactionValues import saveTransactionValues

swapCoins = SwapCoins()

junoswap = SwapCoins.JunoSwap()
sifchain = SwapCoins.Sifchain()
osmosis = SwapCoins.Osmosis()
crescent = SwapCoins.Crescent()

# sifchain.swapCoins('rowan', 0.0001, 'osmo')
# osmosis.swapCoins('osmo', 0.001, 'juno')


manager = Manager()
return_dict = manager.dict()
func1 = Process(target=crescent.swapCoins, args=('ust', 0.1, 'bcre', return_dict))
func2 = Process(target=junoswap.swapCoins, args=('ust', 0.0001, 'atom', return_dict))
func1.start()
func2.start()
func1.join()
func2.join()
saveTransactionValues(return_dict)