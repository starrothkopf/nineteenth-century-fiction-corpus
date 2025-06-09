from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('noveltm_ef.csv')
inferreddate,enumcron,volnum,nonficprob,place,estimated_gender,page_count,genre
X = df[['page_count', 'nonficprob', 'inferreddate', 'enumcron']]  
y = df['genre'].str.contains("fiction", case=False).astype(int)  # 1 = fiction, 0 = not

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)