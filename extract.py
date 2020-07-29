# Extract.py to be used to extract artist data from Chartmetric api for processing
import pandas as pd
import pycmc

def search(artist):
    res = pycmc.search_engine.search(artist)
    df = pd.json_normalize(res['artists'])
    return df

def main():
    print("Chartmetric import success!")

if __name__ == '__main__':
    main()
