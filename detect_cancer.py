import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the data
df = pd.read_csv("cancer_demographics - cancer_demographics.csv.csv")

# Encode categorical variables with separate encoders
encoders = {}
for col in ['Gender', 'AgeGroup', 'FamilyHistory', 'CancerType', 'Stage']:
    enc = LabelEncoder()
    df[col] = enc.fit_transform(df[col])
    encoders[col] = enc

# Features and target
X = df[['Gender', 'AgeGroup', 'FamilyHistory', 'CancerType']]
y = df['Stage']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Evaluate
accuracy = clf.score(X_test, y_test)
print(f"Test accuracy: {accuracy:.2f}")

# Predict for a new patient
sample = pd.DataFrame([{
    'Gender': encoders['Gender'].transform(['Female'])[0],
    'AgeGroup': encoders['AgeGroup'].transform(['50-59'])[0],
    'FamilyHistory': encoders['FamilyHistory'].transform(['Yes'])[0],
    'CancerType': encoders['CancerType'].transform(['Lung'])[0]
}])
pred_stage = clf.predict(sample)
print("Predicted Stage:", encoders['Stage'].inverse_transform(pred_stage)[0])