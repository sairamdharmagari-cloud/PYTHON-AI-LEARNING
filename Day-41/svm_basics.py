import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Result":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X=df[["Hours"]]
y=df["Result"]

# 3. Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Create SVM model
model=SVC(kernel="linear",C=1)


# 5. Train the model
model.fit(X_scaled,y)

# 6. Predict for a new student
new_student=pd.DataFrame([[7]], columns=X.columns)

new_scaled = scaler.transform(new_student)

prediction = model.predict(new_scaled)

# 7. Display result

if prediction[0]==1:
    print("Student will Pass")
else:
    print("Student will Fail")