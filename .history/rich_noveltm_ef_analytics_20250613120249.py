import pandas as pd
from collections import Counter
import ast

df = pd.read_csv('rich_noveltm_ef.csv')
print(f"\ntotal entries: {len(df)}")

def parse_list(val):
    if pd.isna(val) or val.strip() in ("", "[]"):
        return []
    try:
        parsed = ast.literal_eval(val)
        return [str(x).strip().lower() for x in parsed]
    except:
        return [val.strip().lower()]

df['genre_tag'] = df['genre_tag'].apply(parse_list)
df['lcc_category'] = df['lcc_category'].apply(parse_list)

# pub years
if 'inferreddate' in df.columns:
    df['year_bucket'] = (df['inferreddate'] // 10 * 10).astype(int)
    print("\npublication year distribution by decade:")
    print(df['year_bucket'].value_counts().sort_index())

# top authors
if 'author' in df.columns:
    print("\nmost common authors:")
    print(df['author'].value_counts().head(15))

# 1. Top Genre Tags (excluding 'unknown')
all_genres = sum(df['genre_tag'], [])
genre_counts = Counter([g for g in all_genres if g != "unknown"]).most_common(10)

# 2. Top LCC Categories (excluding 'unknown')
all_lcc = sum(df['lcc_category'], [])
lcc_counts = Counter([c for c in all_lcc if c != "unknown"]).most_common(10)

# 3. Author Gender Distribution
gender_counts = df['estimated_gender'].str.lower().value_counts(dropna=True)

# 4. Nonfiction & Juvenile Probabilities
nonfic_avg = df['nonficprob'].mean()
juvenile_avg = df['juvenileprob'].mean()

# 5. Basic sentence/line/token stats
text_stats = df[[
    'avg_sentence_count', 'avg_line_count', 'avg_tokens_per_page',
    'var_sentence_count', 'var_line_count', 'var_tokens_per_page', 'cap_alpha_freq'
]].describe()


print("\n--- Top Genres ---")
for genre, count in genre_counts:
    print(f"{genre}: {count}")

print("\n--- Top LCC Categories ---")
for lcc, count in lcc_counts:
    print(f"{lcc}: {count}")

print("\n--- Estimated Gender Distribution ---")
print(gender_counts)

print(f"\nAverage Nonfiction Probability: {nonfic_avg:.2f}")
print(f"Average Juvenile Probability: {juvenile_avg:.2f}")

print("\n--- Textual Features Summary ---")
print(text_stats)

"""
total entries: 10519
fiction: 5797
unknown: 4656
novel: 66
england: 5
electronic books: 5
dime novels: 5
mixed: 4
novels: 3
london: 3
fantasy fiction: 3
translations: 3
three deckers: 3
love stories: 3
adventure fiction: 3
mystery and detective fiction: 3
science fiction: 3
illustrated works: 2
historical fiction: 2
great britain: 2
encyclopedia: 2
dictionary: 2
christian fiction: 2
criticism, interpretation, etc: 2
folklore: 2
domestic fiction: 2

publication year distribution by decade:
year_bucket
1780       9
1790     112
1800     283
1810     320
1820     589
1830     599
1840     637
1850     668
1860     803
1870     896
1880    1342
1890    1849
1900    1732
1910     680
Name: count, dtype: int64

most common authors:
author
Oliphant                                    60
Scott, Walter, Sir                          55
James, G. P. R. (George Payne Rainsford)    54
Balzac, Honoré de                           49
Braddon, M. E. (Mary Elizabeth)             49
Defoe, Daniel                               46
Edgeworth, Maria                            44
Wood, Ellen                                 42
Whyte-Melville, G. J. (George John)         41
Yonge, Charlotte M. (Charlotte Mary)        40
Reid, Mayne                                 39
Dickens, Charles                            38
Martineau, Harriet                          34
Ainsworth, William Harrison                 34
Grant, James                                34
Name: count, dtype: int64

most common MARC country codes:
place
enk    10033
stk      466
xxk       18
wlk        2
Name: count, dtype: int64

genre
Fiction    0.208442
unknown    0.354554
Name: nonficprob, dtype: float64

estimated_gender
m          5770
f          2403
unknown    2346
Name: count, dtype: int64

"""