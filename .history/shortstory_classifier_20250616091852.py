import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("rich_noveltm_ef_labeled.csv")

feature_cols = [
    'avg_sentence_count', 'var_sentence_count',
    'avg_line_count', 'var_line_count',
    'avg_tokens_per_page', 'var_tokens_per_page',
    'cap_alpha_freq'
]

X = df[feature_cols]
y = df['shortstory']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
