# Sentiment Analysis of Michelin Restaurants
### Michelin-Guide Restaurants vs Public Opinion in London

This repository presents **a refined and condensed portfolio version** of my **MSc Data Science** dissertation completed at the University of Sheffield (2024).

While the full dissertation contains extensive academic analysis, this portfolio edition reorganises and distills the study into a clean, project-oriented format tailored for practical demonstration.

The project investigates how public sentiment from **Yelp** reviews aligns—or diverges—from expert evaluations in the **Michelin Guide**.

By combining:
- Exploratory Data Analysis
- Sentiment analysis
- Statistical modelling
- Topic modelling

this project analyzes **Yelp** reviews of **Michelin-starred** and **Bib Gourmand** restaurants in London to reveal how customers truly perceive these restaurants relative to their Michelin **recognition**, particularly in terms of **satisfaction**.

This portfolio version focuses on presenting:
- Essential methodology
- Key findings
- Core analytical insights
- Important visualisations

to make the research more accessible and easy to explore.


---


## 🎯 Project Overview

**Main questions**

- Do customer sentiments match Michelin star ratings?
- Are Bib Gourmand restaurants perceived as better value than starred restaurants?
- What themes (food, service, price, atmosphere…) appear most often in reviews?

This repository turns raw Yelp reviews into a full NLP pipeline:
data cleaning → text preprocessing → sentiment analysis → topic modeling → visualization.

---

## 📊 Data

- **Restaurant-level data**: Michelin-starred & Bib Gourmand restaurants in London  
  - Star category (1★ / 2★ / 3★ / Bib)
  - Yelp overall rating & review count
  - Cuisine type & price level

- **Review-level data**: 800+ Yelp reviews  
  - Review text  
  - Review date  
  - User rating (1–5 stars)

> All data is used for educational / portfolio purposes only.

---

## 🧠 Methods

**Data preparation & cleaning**

- Filtered restaurants with sufficient review volume (e.g. ≥ 30 reviews)
- Computed 3-year average Michelin distinction (`Star_Avg`)
- Categorized restaurants into `1 Star / 2 Star / 3 Star / Bib`
- Joined restaurant info with review-level data

**NLP preprocessing**

- Lowercasing, removing punctuation, URLs, numbers
- Tokenization, stopwords removal
- Lemmatization (WordNet)
- Created a cleaned text column: `Processed_Review`

**Analysis**

- **Sentiment Analysis**: VADER (`nltk.sentiment.vader`)
- **Feature Representation**: Bag-of-Words & TF-IDF (`sklearn`)
- **Topic Modeling**: LDA (`sklearn.decomposition.LatentDirichletAllocation`)
- **Visualization**: matplotlib / seaborn

---

## 🔍 Key Findings (examples)

- Bib Gourmand restaurants have **slightly higher average Yelp ratings** than starred restaurants.
- Overall sentiment is positive, but **3-star restaurants show more polarized opinions**  
  (very positive and some very negative reviews).
- Price level shows **weak or no correlation** with sentiment – expensive does not always mean happier customers.
- Positive reviews focus on *“tasting menu”, “flavours”, “experience”, “service”*  
  while negative reviews mention *“money”, “disappointed”, “wait”, “overpriced”*.
- Topics from LDA cluster around:
  1. Food quality & flavours  
  2. Service & staff  
  3. Atmosphere & setting  
  4. Value for money  

---
