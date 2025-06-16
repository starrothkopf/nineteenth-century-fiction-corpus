import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

ef = pd.read_csv('noveltm_ef.csv')
fic = pd.read_csv('fiction_proportions.csv')

merged = ef.merge(fic, on='docid', how='inner')
print(f"Merged shape: {merged.shape}")

merged['label_fiction'] = (merged['pct_fic'] > 0.7).astype(int)

# You can add others later: author gender, title length, etc.
features = ['page_count', 'nonficprob', 'inferreddate', 'enumcron', 'volnum', 'pct_fic', 'pages_fic', 'totalpages']
X = merged[features]
y = merged['label_fiction']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier() # try LLM classifier?
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))

# currently slighlty better than random, 61% accuracy, going to go back and get richer extracted features