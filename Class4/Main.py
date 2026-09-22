import pandas as pd
import numpy as np

from Functions import best_in_cuisine, all_available_cuisines, rank_areas, add_full_menu_price
from Visualize import compare_cuisine_rating, compare_neighborhood_rating, compare_cuisine_price

with open('Class4\\barcelona_restaurants_100.csv', 'r') as file:
    data = pd.read_csv(file)

#print(data.head())
#print(data.info())
print(data.iloc[0])



best_italian = best_in_cuisine(data, 'Italian')
print(best_italian)

all_cuisines = all_available_cuisines(data)
print(all_cuisines)

sorted_areas = rank_areas(data)
print(sorted_areas)

data = add_full_menu_price(data)

compare_cuisine_rating(data)
compare_neighborhood_rating(data)
compare_cuisine_price(data)
