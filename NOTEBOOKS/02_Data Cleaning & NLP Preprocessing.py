# 02_Data Cleaning & NLP Preprocessing

## Import the required packages.
import pandas as pd
import re
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


## Load the CSV files.
Reviews_All = pd.read_csv('/Users/jeffreykuo5872/Documents/Michelin/Data/Reviews_All.csv')
Reviews_All.head()


## Check for missing values.
missing_values = Reviews_All.isnull().sum()
print(missing_values)


## Check for duplicate review texts.
duplicate_reviews = Reviews_All[Reviews_All.duplicated(['Review_Text'])]
print(duplicate_reviews)

Reviews_All = Reviews_All.drop_duplicates(subset=['Review_Text'])
Reviews_All.shape[0]


## Standardize date format in 'Review_Date'
Reviews_All['Review_Date'] = pd.to_datetime(Reviews_All['Review_Date'], errors='coerce')
nat_count = Reviews_All['Review_Date'].isna().sum()
print(nat_count)


## Check for outliers in the Yelp overall rating (Y_Rating_Value) and review ratings (Review_Rating)
outliers = Reviews_All[(Reviews_All['Y_Rating_Value'] < 1) | (Reviews_All['Y_Rating_Value'] > 5)]
print(outliers)


## SSL Bypass.
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

ssl._create_default_https_context = ssl.create_default_context
'''


## NLP Preprocessing.
def preprocess_text(text):
    text = text.lower()   # 小寫化
    text = text.translate(str.maketrans('', '', string.punctuation))   # 移除標點符號
    text = ''.join([i for i in text if not i.isdigit()])   # 去除數字
    text = re.sub(r'[^a-zA-Z\s]', '', text)   # 非字母全部過濾
    words = nltk.word_tokenize(text)   # 分詞（tokenization）
    stop_words = set(stopwords.words('english'))   # 去除停用詞
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()   # 詞形還原
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

Reviews_All['Processed_Review'] = Reviews_All['Review_Text'].apply(preprocess_text)
Reviews_All['Processed_Review'].head()