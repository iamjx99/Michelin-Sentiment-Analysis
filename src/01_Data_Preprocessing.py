# 01_Data_Preprocessing

import pandas as pd

filepath_MS = '/Users/jeffreykuo5872/Desktop/michelin/Data/Original_Data/Michelin_Star.csv'
Michelin_Star = pd.read_csv(filepath_MS)

filepath_MB = '/Users/jeffreykuo5872/Desktop/michelin/Data/Original_Data/Michelin_Bib.csv'
Michelin_Bib = pd.read_csv(filepath_MB)


Michelin_Star['Star_Avg'] = Michelin_Star[['M_Distinction_24', 'M_Distinction_23', 'M_Distinction_22']].mean(axis=1)
Michelin_Star_R = Michelin_Star[Michelin_Star['Star_Avg'] >= 0.5]
Michelin_Star_R = Michelin_Star_R[(Michelin_Star_R['Y_Rating_Value'] != 0) & (Michelin_Star_R['Y_Review_Count'] >= 30)]
Michelin_Star_R.shape[0]

Michelin_Bib_R = Michelin_Bib[(Michelin_Bib['Y_Rating_Value'] != 0) & (Michelin_Bib['Y_Review_Count'] >= 30)]
Michelin_Bib_R.shape[0]


Michelin_Star_R['Type'] = 'Star'
Michelin_Bib_R['Type'] = 'Bib'

Selected_R = pd.concat([Michelin_Star_R, Michelin_Bib_R], ignore_index=True)
Selected_R.head()


import numpy as np

conditions = [
    (Selected_R['Type'] == 'Bib'),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 2.5),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 1.5) & (Selected_R['Star_Avg'] < 2.5),
    (Selected_R['Type'] == 'Star') & (Selected_R['Star_Avg'] >= 0.5) & (Selected_R['Star_Avg'] < 1.5)
]
choices = ['Bib Gourmand', '3 Star', '2 Star', '1 Star']
Selected_R['Star_Distinction'] = np.select(conditions, choices, default='Unrated')


Selected_R = Selected_R.drop(columns=['M_Distinction_24', 'M_Distinction_23', 'M_Distinction_22'])
Selected_R = Selected_R.drop(columns=['Michelin_Distinction'])
Selected_R = Selected_R.drop(columns=['Star_Avg'])
Selected_R = Selected_R.drop(columns=['Address'])

missing_values = Selected_R.isnull().sum()
Selected_R = Selected_R.dropna()


Selected_R['Star_Distinction'].value_counts()
Selected_R.to_csv('Selected_Restaurant.csv')



filepath_YR = '/Users/jeffreykuo5872/Desktop/michelin/Data/Selected_Data/Yelp_Reviews.csv'
Yelp_Reviews = pd.read_csv(filepath_YR)


duplicate_reviews = Yelp_Reviews[Yelp_Reviews.duplicated(['Review_Text'])]
print(duplicate_reviews)

Yelp_Reviews = Yelp_Reviews.drop_duplicates(subset=['Review_Text'])
Yelp_Reviews.shape[0]

Yelp_Reviews['Review_Date'] = pd.to_datetime(Yelp_Reviews['Review_Date'], errors='coerce')
nat_count = Yelp_Reviews['Review_Date'].isna().sum()

outliers = Yelp_Reviews[(Yelp_Reviews['Review_Rating'] < 1) | (Yelp_Reviews['Review_Rating'] > 5)]


import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return ' '.join(words)

Yelp_Reviews['Processed_Review'] = Yelp_Reviews['Review_Text'].apply(preprocess_text)

Processed_Review = Yelp_Reviews.drop(columns=['Review_Text'])
Processed_Review.to_csv('Processed_Review.csv', index=False)
