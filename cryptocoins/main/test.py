from swapCoins import SwapCoins

swapCoins = SwapCoins()

sifchain = SwapCoins.Sifchain()
osmosis = SwapCoins.Osmosis()

sifchain.swapCoins('rowan', 0.0001, 'osmo')
# osmosis.swapCoins('osmo', 0.001, 'juno')