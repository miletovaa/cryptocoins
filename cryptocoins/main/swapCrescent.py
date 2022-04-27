import sys
import swapCoins

if __name__ == "__main__":
    junoswap = swapCoins.SwapCoins.Crescent()
    junoswap.swapCoins(sys.argv[1], sys.argv[2], sys.argv[3])