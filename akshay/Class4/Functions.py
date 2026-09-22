import pandas as pd
import numpy as np 

def best_in_cuisine(data, cuisine):
    best_cuisine = data[data['cuisine'] == 'cuisine'].sort_values(by='rating', ascending=False).head(1)
    return best_cuisine

def all_available_cuisines(data):
    all_cuisines = data['cuisine'].unique()
    return all_cuisines

def rank_areas(data):
    area_unique = data['neighborhood'].unique()
    avg_ratings = []
    for area in area_unique:
        spliced = data[data['neighborhood'] == area]
        rating = spliced['rating'].mean()
        avg_ratings.append(rating)
    sorted_areas = area_unique[np.argsort(avg_ratings)]
    return sorted_areas

def add_full_menu_price(data):
    full_menu_price =  data['starter_1_price'] + data['starter_2_price'] + data['main_1_price'] + data['main_2_price'] + data['dessert_price'] 
    data['full_menu_price'] = full_menu_price
    return data



