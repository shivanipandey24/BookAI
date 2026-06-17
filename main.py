import pickle

def load_popular():
    with open('popular.pkl','rb') as file:
        return pickle.load(file)