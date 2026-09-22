import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# compare the average rating of each cuisine type
def compare_cuisine_rating(data):
    cuisine_unique = data['cuisine'].unique()
    avg_ratings = []
    for cuisine in cuisine_unique:
        spliced = data[data['cuisine'] == cuisine]
        rating = spliced['rating'].mean()
        avg_ratings.append(rating)
    sorted_cuisines = cuisine_unique[np.argsort(avg_ratings)]
    sorted_avg_ratings = np.sort(avg_ratings)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_cuisines, y=sorted_avg_ratings)
    plt.xticks(rotation=45)
    plt.xlabel('Cuisine Type')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Cuisine Type')
    plt.show()

# compare the average rating of each neighborhood
def compare_neighborhood_rating(data):
    neighborhood_unique = data['neighborhood'].unique()
    avg_ratings = []
    for neighborhood in neighborhood_unique:
        spliced = data[data['neighborhood'] == neighborhood]
        rating = spliced['rating'].mean()
        avg_ratings.append(rating)
    sorted_neighborhoods = neighborhood_unique[np.argsort(avg_ratings)]
    sorted_avg_ratings = np.sort(avg_ratings)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_neighborhoods, y=sorted_avg_ratings)
    plt.xticks(rotation=45)
    plt.xlabel('Neighborhood')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Neighborhood')
    plt.show()

# compare the average price of each cuisine type
def compare_cuisine_price(data):
    cuisine_unique = data['cuisine'].unique()
    avg_prices = []
    for cuisine in cuisine_unique:
        spliced = data[data['cuisine'] == cuisine]
        price = spliced['full_menu_price'].mean()
        avg_prices.append(price)
    sorted_cuisines = cuisine_unique[np.argsort(avg_prices)]
    sorted_avg_prices = np.sort(avg_prices)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_cuisines, y=sorted_avg_prices)
    plt.xticks(rotation=45)
    plt.xlabel('Cuisine Type')
    plt.ylabel('Average Price')
    plt.title('Average Price by Cuisine Type')
    plt.show()
