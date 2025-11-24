# Sentiment Analysis of Michelin Restaurants
### Michelin-Guide Restaurants vs Public Opinion in London

This repository presents a concise, portfolio-oriented version of my **MSc Data Science** dissertation (University of Sheffield, 2024).
While the full dissertation contains comprehensive academic detail, this edition focuses on clarity, reproducibility, and practical demonstration of data science techniques.

The project is motivated by a central question:
> **Do Michelin awards truly reflect what diners value?**

Using publicly available data from the **Michelin Guide** and **Yelp**, this study examines how expert evaluations compare with public sentiment in London’s dining scene.

The analysis covers **881 Yelp reviews** across **58 Michelin-starred and Bib Gourmand restaurants**, enabling a structured comparison of customer satisfaction and perceived value.

This project applies:
- Exploratory Data Analysis
- Sentiment Analysis
- Statistical Modelling
- Topic Modelling

to uncover how diners perceive food quality, service, pricing, and overall experience relative to their Michelin recognition.

This portfolio highlights:
- Essential methodology
- Key findings
- Analytical insights
- Important visualisations

in a clear and accessible format suitable for review by recruiters, interviewers, and technical audiences.


---


## 01_Introduction
The Michelin Guide has long represented expert-driven evaluations based on strict and highly standardised criteria. In contrast, modern platforms like Yelp reflect the experiences of everyday diners, who value not only culinary technique but also service, atmosphere, and overall affordability.

In a city like London, where Michelin-starred and Bib Gourmand restaurants coexist with thousands of public reviews, these two perspectives often highlight different aspects of restaurant quality.

This contrast sets the foundation for examining how expert recognition aligns with public sentiment, and it directly motivates the key objectives and hypotheses of this study.

### 🎯 Research Design: Objectives, Questions, and Hypotheses
To analyse how expert recognition aligns with public sentiment, the study adopts a structured, top-down research design. The process begins with the overarching question of whether Michelin awards reflect what diners truly value. From this starting point, the problem is divided into three core objectives: assessing satisfaction, comparing categories, and identifying the drivers of sentiment.

Each objective is then translated into a concrete research question, ensuring that the analysis remains specific and measurable. Finally, each research question is supported by one or more hypotheses that can be validated through statistical testing and NLP techniques such as sentiment scoring and topic modelling.

The full mapping is summarised below:

| Objective | Research Question(s) | Hypotheses |
|----------|-----------------------|------------|
| **O1. Customer satisfaction** | **RQ1:** Are customers satisfied with Michelin-recognised restaurants? | **H1–H3** |
| **O2. Category & price differences** | **RQ2:** Does higher price correlate with higher satisfaction?<br>**RQ3:** How do Bib Gourmand and Michelin-starred restaurants differ in public sentiment? | **H4–H5**<br>**H6-H9** |
| **O3. Linguistic and thematic drivers** | **RQ4:** Which words, topics, or themes shape positive and negative sentiment? | **H10–H12** |

This structured design ensures that every analytical step—whether statistical testing, sentiment analysis, or topic modelling—directly contributes to answering the central question introduced at the beginning of the study.


---


## 02_Dataset Overview
This study integrates two primary datasets:
- Michelin Guide restaurant information
- Yelp customer reviews

together, they provide a combined view of expert evaluations and public sentiment regarding Michelin-recognised restaurants in London.

### 02-01_Michelin Restaurant Dataset
The Michelin dataset includes all Michelin-starred and Bib Gourmand restaurants in London that form the basis of the study.

#### Structure and Variables
| Variable              | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| **Name**              | Restaurant name (used as unique identifier)                 |
| **Cuisine**           | Primary cuisine type                                        |
| **Price**             | Michelin price indicator (e.g., ££££ · Spare no expense)    |
| **Y_Rating_Value**    | Average Yelp rating for the restaurant                      |
| **Y_Review_Count**    | Total number of Yelp reviews                                |
| **Y_Selected_Review** | Number of reviews used in the analysis                      |
| **Type**              | Michelin category group (“Star” or “Bib”)                   |
| **Star_Distinction**  | Final Michelin classification (1★, 2★, 3★, or Bib Gourmand) |

#### Dataset Summary
- 58 restaurants
- Covers Michelin-starred restaurants (1★ / 2★ / 3★) and Bib Gourmand selections
- Includes both descriptive attributes (cuisine, price) and quantitative metrics (Yelp ratings)

This dataset provides the structural labels required for comparing categories and price levels in later analysis.

### 02-02_Yelp Review Dataset
The Yelp dataset contains processed customer reviews matched to the same 58 restaurants.

#### Structure and Variables
| Variable                 | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| **Name**                 | Restaurant name (join key with Michelin dataset)           |
| **Michelin_Distinction** | Numerical representation of Michelin rating                |
| **Review_Date**          | Date of the review                                         |
| **Review_Rating**        | User rating (1–5 stars)                                    |
| **Processed_Review**     | Cleaned review text used for sentiment and topic modelling |

#### Dataset Summary
- 881 Yelp reviews
- All reviews processed through tokenisation, stopword removal, and lemmatisation
- Contains both numeric fields (ratings) and unstructured text (review content)

### 02-03_Combined Analytical Dataset
After merging the Michelin and Yelp datasets using restaurant names:
- All 58 restaurants include corresponding Yelp metadata
- Each review is linked to Michelin category, price level, and cuisine type
- The final dataset contains structured attributes and processed text, enabling:
  - Cross-category comparisons
  - Sentiment analysis
  - Statistical testing
  - Topic modelling

This integrated dataset forms the foundation for all subsequent analysis.


---


## 03_Methodology





