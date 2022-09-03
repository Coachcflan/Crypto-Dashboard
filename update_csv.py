import pandas as pd
import numpy as np
import time, datetime
import requests
from bs4 import BeautifulSoup
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
def coin_data_csv():
    old_df = pd.read_csv('/Users/thesavage/Dashboard_folder/top_200.csv')
    coin_ids = list(old_df['coin_id'].unique())
    df_concat_list = []
    count = -1
    while True:
        count += 1
        if count == len(coin_ids):
            break
        else:
            coin = coin_ids[count]
            try:
                coin_market_dictionary = cg.get_coin_by_id(coin)
                temp_df = pd.DataFrame()
                temp_df['date'] = [pd.Timestamp(datetime.date.today())]
                temp_df['coin_id'] = [coin]
                temp_df['prices'] = [coin_market_dictionary['market_data']['current_price']['usd']]
                temp_df['volume'] = [coin_market_dictionary['market_data']['total_volume']['usd']]
                temp_df['mktcap'] = [coin_market_dictionary['market_data']['market_cap']['usd']]
                temp_df['tags'] = old_df.loc[old_df['coin_id'] == coin]['tags'].unique()
                temp_df = old_df.loc[old_df['coin_id'] == coin].append(temp_df).drop_duplicates()
            except Exception as e:
                print(e)
                print(coin)
                time.sleep(120) #sleep for a minute to get more coingecko requests
                count -= 1
            df_concat_list.append(temp_df)
            master_df = pd.concat(df_concat_list)
            master_df['date'] = pd.to_datetime(master_df['date'])
            master_df = master_df.drop_duplicates()
   
    return master_df.set_index('date').to_csv('/Users/thesavage/Dashboard_folder/top_200.csv')
coin_data_csv()
