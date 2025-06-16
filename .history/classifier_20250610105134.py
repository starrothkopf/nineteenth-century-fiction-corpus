import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('fiction_proportions.csv') 
X = df[['pages_fic', 'pct_fic', 'totalpages', 'enumcron', 'volnum']] 

docid,title,author,inferred_date,pages_fic,pct_fic,totalpages

y = df['genre'].str.contains("fiction", case=False).astype(int)  # 1 = fiction, 0 = not

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier() # try LLM classifier?
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))

# currently slighlty better than random, 61% accuracy, going to go back and get richer extracted features