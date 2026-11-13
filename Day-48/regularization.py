from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import mean_squared_error,r2_score

data=fetch_california_housing()

X = data.data
y=data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "Linear Regression":make_pipeline(
        StandardScaler(),
        LinearRegression()
    ),

    "Ridge Regression":make_pipeline(
        StandardScaler(),
        Ridge(alpha=1.0)
    ),

    "Lasso Regression":make_pipeline(
        StandardScaler(),
        Lasso(alpha=0.01,max_iter=10000)
    )
}

for name, model in models.items():
    model.fit(X_train,y_train)

    predicitons = model.predict(X_test)

    mse = mean_squared_error(
        y_test,
        predicitons
    )

    r2 = r2_score(
        y_test,
        predicitons
    )

    print("\nModels:",name)
    print("MSE:",mse)
    print("R2 Score:",r2)



#Ridge(alpha=1.0)

#alpha controls the strength of regularization.
#- Small alpha → weaker penalty.
#- Large alpha → stronger penalty.
#Too much regularization can cause underfitting. 
# Choose alpha using cross validation rather than guessing.