#Let's use Polynomial Regression to see how model complexity affects predictions.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Dataset
np.random.seed(42)

X= np.linspace(0,10,50).reshape(-1,1)

y=2* X.ravel()  + 3+ np.random.normal(0, 2,50)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 3. Test different model complexities

degrees = [1,2,15]

plt.figure(figsize=(8 , 3))

for degree in degrees:
    # Create polynomial model
    model = make_pipeline(
        PolynomialFeatures(degree=degree),
        LinearRegression()
    )

#Train 
    model.fit(X_train,y_train)

#Predictions:
    train_predictions = model.predict(X_train)
    test_predictions= model.predict(X_test)

#Calculate Errors

    train_error = mean_squared_error(
        y_train,
        train_predictions
)

    test_error = mean_squared_error(
         y_test,
         test_predictions
        
)

    print("\nPoly Degree:",degree)
    print("Training Error:",train_error)
    print("Testing Error:",test_error)

    #plot predictions
    X_plot =np.linspace(0,10,200).reshape(-1 ,1)
    y_plot = model.predict(X_plot)

    plt.plot(
        X_plot,
        y_plot,
        label=f"Degree {degree}"

    )

# Plot original data
plt.scatter(
    X_train,
    y_train,
    label ="Training data"
)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Underfittind vs Overfitting:")

plt.legend()
plt.show()



#degrees = [1, 2, 15]

#We are testing three different levels of model complexity.
#- Degree 1: simple linear model; may underfit.
#- Degree 2: more flexible model; may fit the pattern well.
#- Degree 15: highly flexible model; may overfit.



#mean_squared_error(y_train, train_predictions)
#Calculates the average squared prediction error on training data.
#Important: The exact results depend on the dataset and random split. 
# Don't assume degree 2 must always be the best.