
# coding: utf-8

# In[1]:

# Assignment_API
# Ihsan 67675
# Create API from open api website and then deploy into heroku

import pandas as pd
import uvicorn
from fastapi import FastAPI
from urllib.request import urlopen
import json


def game_data(dat_game):
        game = pd.DataFrame(json.loads(dat_game.read()))
        #Convert the type certain columns into numeric
        game[['dealRating', 'gameID', 'metacriticScore', 'normalPrice', 'salePrice', 
              'savings', 'steamAppID', 'steamRatingCount', 'steamRatingPercent']] = game[['dealRating', 'gameID', 'metacriticScore', 'normalPrice', 'salePrice', 
              'savings', 'steamAppID', 'steamRatingCount', 'steamRatingPercent']].apply(pd.to_numeric)
    
        #Drop unneeded columns
        game.drop(['dealID', 'metacriticLink', 'thumb', 'internalName', 'isOnSale', 'storeID',
               'lastChange', 'releaseDate', 'steamAppID', 'dealRating', 'metacriticScore', 'savings'], axis=1, inplace=True)
    
        #Rearrange the columns
        game = game.reindex(columns=['title', 'gameID', 'normalPrice',
                                     'salePrice', 'steamRatingCount',
                                     'steamRatingPercent', 'steamRatingText'])
    
        #Rename title columns so it will shown first
        game = game.rename(columns={'title':'game_title'})
        return(game)

app = FastAPI()
@app.get('/')
def read_root():
    return {'messages':'This is an api of Steam Games rating and popularity'}

@app.get('/rating_game')
def highrate_game():
    #Read the data from web (Steam Games)
    data = urlopen('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15')
    
    #Call the function
    rate = game_data(data)
    
    #Show the top 10 of the highest steam game's rating
    high_rated = rate.sort_values(by=['steamRatingPercent'], ascending=False).head(10)
    
    #Convert the dataframe into dictionary and then dumps it as json so it will be shown neatly
    game_rate = high_rated.to_dict('records')
    return (game_rate)
    
@app.get('/popular_game')
def pop_game():
    #Read the data from web (Steam Games)
    data1 = urlopen('https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15')
    
    #Call the function
    pop = game_data(data1)
    
    #Show the top 10 of the most popular steam game
    popular = pop.sort_values(by=['steamRatingCount'], ascending=False).head(10)
    
    #Convert the dataframe into dictionary and then dumps it as json so it will be shown neatly
    game_popular = popular.to_dict('records')
    return (game_popular)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')

