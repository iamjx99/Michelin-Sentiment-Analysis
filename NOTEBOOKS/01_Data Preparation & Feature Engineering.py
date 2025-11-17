# 01_Data Preparation & Feature Engineering

## Import the required packages.
import pandas as pd
import numpy as np


## Load the CSV files(Original data).
filepath_MS = '/Users/jeffreykuo5872/Documents/Michelin/Original_Data/Michelin_Star.csv'
Michelin_Star = pd.read_csv(filepath_MS)
Michelin_Star.head()

filepath_MB = '/Users/jeffreykuo5872/Documents/Michelin/Original_Data/Michelin_Bib.csv'
Michelin_Bib = pd.read_csv(filepath_MB)
Michelin_Bib.head()


## Filter out target restaurants.
Michelin_Star['Star_Avg'] = Michelin_Star[['M_Distinction_24', 'M_Distinction_23', 'M_Distinction_22']].mean(axis=1)
Michelin_Star_R = Michelin_Star[Michelin_Star['Star_Avg'] >= 1]
Michelin_Star_R = Michelin_Star_R[(Michelin_Star_R['Y_Rating_Value'] != 0) & (Michelin_Star_R['Y_Review_Count'] >= 30)]
Michelin_Star_R.shape[0]

Michelin_Bib_R = Michelin_Bib[(Michelin_Bib['Y_Rating_Value'] != 0) & (Michelin_Bib['Y_Review_Count'] >= 30)]
Michelin_Bib_R.shape[0]


## Merge two sets of data.
Michelin_Star_R['Type'] = 'Star'
Michelin_Bib_R['Type'] = 'Bib'

Selected_R = pd.concat([Michelin_Star_R, Michelin_Bib_R], ignore_index=True)
Selected_R.head()


## Column cleaning.
Selected_R = Selected_R.drop(columns=[
    'M_Distinction_24', 
    'M_Distinction_23', 
    'M_Distinction_22'
])
Selected_R = Selected_R.drop(columns=['Address'])


## Create column 'Star_Distinction'.
conditions = [
    (Selected_R['Type'] == 'Bib'),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 2.5),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 1.5) & (Selected_R['Star_Avg'] < 2.5),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 0.5) & (Selected_R['Star_Avg'] < 1.5)
]
choices = ['Bib Gourmand', '3 Star', '2 Star', '1 Star']
Selected_R['Star_Distinction'] = np.select(conditions, choices, default='Unrated')

Selected_R[['Name', 'Type', 'Star_Avg', 'Star_Distinction']].head()
Selected_R['Star_Distinction'].value_counts()
Selected_R.to_csv('Selected_Restaurant.csv')


## Load the CSV files(Yelp_Reviews).
filepath_YR = '/Users/jeffreykuo5872/Documents/Michelin/Selected_Data/Yelp_Reviews.csv'
Yelp_Reviews = pd.read_csv(filepath_YR)
Yelp_Reviews.head()


## Data Integration.
cols_keep = [
    'Name',
    'Cuisine',
    'Price',
    'Y_Rating_Value',
    'Y_Review_Count',
    'Star_Avg',
    'Type',
    'Star_Distinction'
]

Reviews_All = Yelp_Reviews.merge(
    Selected_R[cols_keep],
    on='Name',
    how='left'
)

Reviews_All.to_csv('Reviews_All.csv', index=False)
Reviews_All.head()