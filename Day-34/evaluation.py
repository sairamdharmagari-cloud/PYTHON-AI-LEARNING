import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Dataset
data={
       "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "PreviousScore": [40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    "FinalScore": [45, 50, 55, 60, 65, 72, 78, 82, 88, 94]
}

df = pd.DataFrame(data)

#input features
X=df[["Hours", "Attendance", "PreviousScore"]]

# Target
y = df["FinalScore"]

#Train/Test split
X_train,X_test,y_train,y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42

)

#model
model = LinearRegression()

#Training
model.fit(X_train,y_train)

#Prediction
prediction = model.predict(X_test)

#Evaluation
mae=mean_absolute_error(y_test,prediction)
mse=mean_squared_error(y_test,prediction)
rmse= mse**0.5
r2= r2_score(y_test,prediction)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)