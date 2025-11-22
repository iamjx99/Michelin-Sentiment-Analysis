# 02_Exploratory_Data_Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import math
from matplotlib import cm

filepath_SR = '/Users/jeffreykuo5872/Desktop/michelin/Data/Cleaned_Data/Selected_Restaurant.csv'
Selected_Restaurant = pd.read_csv(filepath_SR)

filepath_PR = '/Users/jeffreykuo5872/Desktop/michelin/Data/Cleaned_Data/Processed_Review.csv'
Processed_Review = pd.read_csv(filepath_PR)

## Selected_Restaurant
Selected_Restaurant.groupby('Star_Distinction')['Y_Rating_Value'].describe()

plt.figure(figsize=(12, 7))
sns.boxplot(x='Star_Distinction', y='Y_Rating_Value', data=Selected_Restaurant, palette='coolwarm')
plt.title("Yelp Rating Value by Michelin Star Distinction", fontsize=16, fontweight='bold')
plt.xlabel("Michelin Star Distinction", fontsize=12)
plt.ylabel("Yelp Rating", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


Selected_Restaurant.groupby('Star_Distinction')['Y_Review_Count'].describe()

plt.figure(figsize=(12, 7))
sns.boxplot(x='Star_Distinction', y='Y_Review_Count', data=Selected_Restaurant, palette='coolwarm')
plt.title("Yelp Rating Count by Michelin Star Distinction", fontsize=16, fontweight='bold')
plt.xlabel("Michelin Star Distinction", fontsize=12)
plt.ylabel("Yelp Rating Count", fontsize=12)
plt.yscale('log')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


cuisine_counts = Selected_Restaurant['Cuisine'].value_counts()
cuisine_mapping = {
    'African': 'African', 'African, Creative': 'African',
    'British': 'British', 'Creative British': 'British', 'Modern British': 'British', 'Traditional British': 'British', 'Traditional British, Classic Cuisine': 'British',
    'Californian, Modern Cuisine': 'Modern Cuisine',
    'Chinese': 'Chinese', 'Taiwanese': 'Chinese',
    'Creative': 'Creative', 'Creative, Contemporary': 'Creative',
    'European Contemporary': 'European',
    'French': 'French', 'French Contemporary': 'French', 'French, French Contemporary': 'French', 'Modern French': 'French', 'Modern French, French Contemporary': 'French',
    'Grills': 'Japanese', 'Japanese': 'Japanese', 'Japanese, Sushi': 'Japanese',
    'Indian': 'Indian', 'South Indian, Sri Lankan': 'Indian',
    'Italian': 'Italian',
    'Mediterranean Cuisine': 'Mediterranean', 'North African, Mediterranean Cuisine': 'Mediterranean',
    'Mexican, Modern Cuisine': 'Mexican',
    'Modern Cuisine': 'Modern Cuisine', 'Modern Cuisine, Classic Cuisine': 'Modern Cuisine',
    'Seafood': 'Seafood',
    'Spanish': 'Spanish',
    'Middle Eastern': 'Middle Eastern', 'Persian':'Middle Eastern',
    'Thai': 'Thai'
}
Selected_Restaurant['Cuisine'] = Selected_Restaurant['Cuisine'].map(cuisine_mapping).fillna(Selected_Restaurant['Cuisine'])

cuisine_counts = Selected_Restaurant['Cuisine'].value_counts().reset_index()
cuisine_counts.columns = ['Cuisine', 'Count']

cuisine_counts = cuisine_counts.sort_values(by='Count', ascending=False)

plt.figure(figsize=(12, 7))
sns.barplot(data=cuisine_counts, x='Count', y='Cuisine', palette='coolwarm')
plt.title("Number of Cuisine Types", fontsize=16, fontweight='bold')
plt.xlabel("Count", fontsize=12)
plt.ylabel("Cuisine", fontsize=12)
plt.tight_layout()
plt.show()



## Processed_Review
count_series = Processed_Review['Review_Rating'].value_counts().sort_index()
mean_series = Processed_Review.groupby('Review_Rating')['Review_Length'].mean()

ratings = count_series.index

fig, ax1 = plt.subplots(figsize=(12, 7))

bars = ax1.bar(ratings, count_series, color="#76A5E0", alpha=0.7, zorder=1)
ax1.set_xlabel("Review Rating")
ax1.set_ylabel("Count of Reviews", fontsize=12)
ax1.set_yscale("log")

for x, y in zip(ratings, count_series):
    ax1.text(x, y, str(y), ha='center', va='bottom', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(ratings, mean_series, marker='o', linewidth=3, color='darkorange', zorder=2)
ax2.set_ylabel("Average Review Length", fontsize=12)

for x, y in zip(ratings, mean_series):
    ax2.text(x, y + 1, f"{y:.1f}", ha='center', fontsize=10)

plt.title("Counts vs Average Review Length Across Ratings", fontsize=16, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


Processed_Review['Review_Length'] = Processed_Review['Processed_Review'].str.split().str.len()

plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.histplot(data=Processed_Review, x="Review_Length", bins=50, kde=True, color="#76A5E0", edgecolor=None, alpha=0.75)

plt.axvline(Processed_Review['Review_Length'].median(), color='red', linestyle='--', linewidth=2, label=f"Mean = {Processed_Review['Review_Length'].median():.1f}")
plt.axvline(Processed_Review['Review_Length'].mean(), color='darkorange', linestyle='--', linewidth=2, label=f"Median = {Processed_Review['Review_Length'].mean():.1f}")

plt.title("Distribution of Review Length", fontsize=16, fontweight='bold')
plt.xlabel("Review Length (words)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 7))
sns.boxplot(data=Processed_Review, x='Review_Rating', y='Review_Length', palette='coolwarm')
plt.yscale('log')
plt.title("Review Length vs Rating", fontsize=16, fontweight='bold')
plt.xlabel('Review Rating', fontsize=12)
plt.ylabel('Review Length', fontsize=12)
plt.show()


Processed_Review['Review_Date'] = pd.to_datetime(Processed_Review['Review_Date'], errors='coerce')

Yelp_Reviews_234 = Processed_Review[
    (Processed_Review['Review_Date'].dt.year >= 2023) &
    (Processed_Review['Review_Date'].dt.year <= 2024)
]

michelin_monthly_reviews_filtered = (
    Yelp_Reviews_234
    .groupby(['Michelin_Distinction', Yelp_Reviews_234['Review_Date'].dt.to_period('M')])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(12, 7))
michelin_monthly_reviews_filtered.T.plot(
    kind='bar',
    stacked=True,
    colormap='coolwarm',
    alpha=0.8
)

plt.title('Number of Reviews Over Time by Michelin Distinction (2023–2024)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Michelin Distinction')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


from wordcloud import WordCloud

Counter(" ".join(Processed_Review['Processed_Review']).split()).most_common(20)

text = " ".join(Processed_Review['Processed_Review'])
wc = WordCloud(width=1000, height=600, background_color='white', colormap="icefire",).generate(text)
plt.figure(figsize=(12,7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud of Yelp Reviews', fontsize=16, fontweight='bold')
plt.show()


high = " ".join(Processed_Review[Processed_Review['Review_Rating'].isin([4,5])]['Processed_Review'])
low  = " ".join(Processed_Review[Processed_Review['Review_Rating'].isin([1,2])]['Processed_Review'])

high_counts = Counter(high.split())
low_counts  = Counter(low.split())

def compute_log_odds_with_prior(counts1, counts2, alpha_0=1000):
    vocab = set(counts1) | set(counts2)

    n1 = sum(counts1.values())  
    n2 = sum(counts2.values()) 

    bg = counts1 + counts2
    bg_total = sum(bg.values())

    alpha = {w: alpha_0 * bg[w] / bg_total for w in vocab}

    results = []
    for w in vocab:
        y1 = counts1[w]
        y2 = counts2[w]
        a  = alpha[w]

        log_odds1 = math.log((y1 + a) / (n1 - y1 + alpha_0 - a))
        log_odds2 = math.log((y2 + a) / (n2 - y2 + alpha_0 - a))
        delta = log_odds1 - log_odds2

        var = 1.0 / (y1 + a) + 1.0 / (y2 + a)
        z = delta / math.sqrt(var)

        results.append((w, delta, z, y1, y2))

    results.sort(key=lambda x: x[2], reverse=True)
    return results

results = compute_log_odds_with_prior(high_counts, low_counts, alpha_0=1000)

min_total_count = 5
results = [r for r in results if r[3] + r[4] >= min_total_count]

top_high = [r for r in results if r[2] > 0][:30]
top_low  = [r for r in reversed(results) if r[2] < 0][:30]

print("High Score word：")
for w, delta, z, c1, c2 in top_high:
    print(f"{w:15s} z={z:6.2f}  high={c1:4d}  low={c2:4d}")

print("\nLow Score word：")
for w, delta, z, c1, c2 in top_low:
    print(f"{w:15s} z={z:6.2f}  high={c1:4d}  low={c2:4d}")

k = 12

neg = top_low[:k]
pos = top_high[:k]

neg_words = [w for w,_,_,_,_ in neg]
neg_vals  = [z for _,_,z,_,_ in neg]

pos_words = [w for w,_,_,_,_ in pos]
pos_vals  = [z for _,_,z,_,_ in pos]

cmap = cm.get_cmap("coolwarm")
neg_color = cmap(0.2)
pos_color = cmap(0.8)

fig, axes = plt.subplots(1, 2, figsize=(12, 7))

axes[0].barh(neg_words, neg_vals, color=neg_color)
axes[0].set_title("Low Rating Keywords (1–2 points)", fontsize=14)
axes[0].set_xlabel("z-score")
axes[0].set_xlim(min(neg_vals)*1.2, 0)

axes[1].barh(pos_words, pos_vals, color=pos_color)
axes[1].set_title("High Rating Keywords (4–5 points)", fontsize=14)
axes[1].set_xlabel("z-score")
axes[1].set_xlim(0, max(pos_vals)*1.2)

fig.suptitle("High vs Low Rating Keywords", fontsize=16, fontweight='bold')
plt.subplots_adjust(top=0.90, wspace=0.35)
plt.show()



star_text = " ".join(
    Processed_Review[Processed_Review["type"] == "star"]["Processed_Review"]
)

bib_text = " ".join(
    Processed_Review[Processed_Review["michelin_type"] == "bib"]["Processed_Review"]
)

star_counts = Counter(star_text.split())
bib_counts  = Counter(bib_text.split())


## Reviews_All
cols_keep = ['Name', 'Cuisine', 'Price', 'Y_Rating_Value', 'Y_Review_Count', 'Y_Selected_Review', 'Type', 'Star_Distinction']
Reviews_All = Processed_Review.merge(Selected_Restaurant[cols_keep], on='Name',how='left')
Reviews_All.to_csv('Reviews_All.csv', index=False)

star_text = " ".join(
    Reviews_All[Reviews_All["Type"] == "Star"]["Processed_Review"]
)

bib_text = " ".join(
    Reviews_All[Reviews_All["Type"] == "Bib"]["Processed_Review"]
)

star_counts = Counter(star_text.split())
bib_counts  = Counter(bib_text.split())

results_sb = compute_log_odds_with_prior(star_counts, bib_counts, alpha_0=1000)

min_total_count = 5
results_sb = [r for r in results_sb if r[3] + r[4] >= min_total_count]

top_star = [r for r in results_sb if r[2] > 0][:30]
top_bib  = [r for r in reversed(results_sb) if r[2] < 0][:30]

print("Star restaurants keywords：")
for w, delta, z, c1, c2 in top_star:
    print(f"{w:15s} z={z:6.2f}  star={c1:4d}  bib={c2:4d}")

print("\nBib Gourmand keywords：")
for w, delta, z, c1, c2 in top_bib:
    print(f"{w:15s} z={z:6.2f}  star={c1:4d}  bib={c2:4d}")

k = 12

neg = top_bib[:k]     # 負向 → 必比登
pos = top_star[:k]    # 正向 → 星級

bib_words = [w for w,_,_,_,_ in neg]
bib_vals  = [z for _,_,z,_,_ in neg]

star_words = [w for w,_,_,_,_ in pos]
star_vals  = [z for _,_,z,_,_ in pos]


cmap = cm.get_cmap("coolwarm")
bib_color  = cmap(0.2)
star_color = cmap(0.8)

fig, axes = plt.subplots(1, 2, figsize=(12, 7))

axes[0].barh(bib_words, bib_vals, color=bib_color)
axes[0].set_title("Bib Gourmand Keywords", fontsize=12)
axes[0].set_xlabel("z-score")
axes[0].set_xlim(min(bib_vals)*1.2, 0)

axes[1].barh(star_words, star_vals, color=star_color)
axes[1].set_title("Michelin Star Keywords", fontsize=12)
axes[1].set_xlabel("z-score")
axes[1].set_xlim(0, max(star_vals)*1.2)

fig.suptitle("Michelin Star vs Bib Gourmand Keywords", fontsize=16, fontweight='bold')
plt.subplots_adjust(top=0.90, wspace=0.35)
plt.show()
