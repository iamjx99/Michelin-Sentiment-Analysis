# Sentiment Analysis of Michelin Restaurants
### Michelin-Guide Restaurants vs Public Opinion in London

This repository presents **a refined and condensed portfolio version** of my **MSc Data Science** dissertation completed at the University of Sheffield (2024).

While the full dissertation contains extensive academic analysis, this portfolio edition reorganises and distills the study into a clean, project-oriented format tailored for practical demonstration.

The project investigates how public sentiment from **Yelp** reviews aligns or diverges from expert evaluations in the **Michelin Guide**.

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


## 01_Introduction

#### Do Michelin awards truly reflect what diners value?

This question lies at the centre of a long-standing tension in the restaurant world.

For over a century, the Michelin Guide has defined culinary excellence through anonymous inspections and rigorous evaluation standards. Yet in today’s digital era, platforms like Yelp capture a very different perspective — one shaped by diverse diners who care not only about creativity and technique, but also service quality, atmosphere, and above all, value for money.

London, one of the world’s most competitive dining hubs, uniquely amplifies this contrast. Here, Michelin-starred restaurants and Bib Gourmand selections coexist with thousands of real customer reviews, revealing potential gaps between expert judgement and public sentiment. This raises several essential questions:
- Do Michelin distinctions align with what customers actually experience?
- Does a higher price guarantee a better dining experience?
- And do Bib Gourmand restaurants — celebrated for affordability — provide greater perceived value than starred establishments?

To explore these questions, this project applies sentiment analysis, topic modelling, and statistical testing to compare Michelin’s professional assessments with 881 Yelp reviews across 58 restaurants in London. The goal is to uncover how diners perceive food, service, pricing, and overall satisfaction — and to determine whether these perceptions reinforce or challenge Michelin’s awards.

### 🎯 Research Objectives & Hypotheses

This study focuses on three core objectives, each supported by a set of hypotheses derived from both consumer behaviour theory and empirical expectations.

#### Objective 1 — Assess whether Michelin-rated restaurants meet customer expectations

##### Key Question: Are customers truly satisfied with Michelin-recognised restaurants?

##### Hypotheses:
- H1. Most Yelp ratings for Michelin restaurants fall within the 4–5 star range.
- H2. Sentiment score distributions mirror the Yelp rating distribution.
- H3. Sentiment scores and Yelp ratings exhibit a significant positive correlation.



#### Objective 2 — Compare satisfaction between Michelin-starred and Bib Gourmand restaurants
##### Key Question: Does higher price or Michelin prestige translate into higher customer satisfaction?
##### Hypotheses:
- H4. Price level positively correlates with customer satisfaction.
- H5. Higher-priced restaurants receive more positive sentiment.
- H6. Average ratings for Bib Gourmand restaurants differ significantly from Michelin-starred restaurants.
- H7. Sentiment score distributions differ between Bib Gourmand and Michelin restaurants.
- H8. Yelp ratings differ significantly across Michelin star tiers (1, 2, 3 stars).
- H9. Michelin star distinctions correlate with sentiment scores.


#### Objective 3 — Identify the factors shaping positive and negative dining experiences
##### Key Question: What elements — food, service, pricing, or specific language in reviews — drive satisfaction or dissatisfaction?
##### Hypotheses:
- H10. Certain high-frequency words strongly correlate with sentiment scores.
- H11. Word–sentiment relationships differ across Michelin categories (Bib, 1-star, 2-star, 3-star).
- H12. Topic modelling reveals distinct themes across different Michelin distinctions.


---







### 🎯 Project Overview

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
