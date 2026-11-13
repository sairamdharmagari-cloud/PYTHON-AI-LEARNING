#After running the main project, a file named breast_cancer_model.joblib will be created. 
# Now create predict.py.

import joblib
from sklearn.datasets import load_breast_cancer


# 1. Load saved model
model =joblib.load("breast_cancer_model.joblib")

# 2. Load datadset for a sample input
cancer =load_breast_cancer()

# 3. Select one sample record
sample = cancer.data[0].reshape(1 ,-1)

# 4. Predict
prediction = model.predict(sample)

# 5. Get prediction probability
probability = model.predict_proba(sample)

# 6 display results
result = cancer.target_names[prediction[0]]

print("Predicted Result:",result)

print("\n Prediction Probs:")
for name, value in zip(cancer.target_names ,probability[0]):
    print(name , ":" , round(value *100,2),"%")

#This uses one example from the built-in dataset to demonstrate how a saved model makes a prediction.
#  It is not a real patient's result.
