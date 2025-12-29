import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Loading and Cleaning of Dataset
df = pd.read_csv('child_safety_dataset.csv')

df['category'] = df['category'].fillna('Safe')
df = df.dropna(subset=['text'])

print("Data loaded and cleaned. Training models now...")

# Training of the safety model  (Binary; Safe or Unsafe)
# The below code is for the conversion of text to numbers - Pipeline
safety_pipe = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression())
])
safety_pipe.fit(df['text'], df['label'])

# Training Category Model (Multiclass: Violence, Scary, etc.)
category_pipe = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression())
])
category_pipe.fit(df['text'], df['category'])

# Saving of models
with open('safety_model.pkl', 'wb') as f:
    pickle.dump(safety_pipe, f)
with open('category_model.pkl', 'wb') as f:
    pickle.dump(category_pipe, f)

print("Models trained and saved successfully!")