import pickle


class CoinsListReturn():
    def get():
        try:
            with open('coinsList.pickle', 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(str(e))
            return None
