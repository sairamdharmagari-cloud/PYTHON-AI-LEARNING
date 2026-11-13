from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import(
    train_test_split,cross_val_score,KFold
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import mean_absolute_error, r2_score

data = load_breast_cancer()

X=data.data
y=data.target

X_train ,X_test ,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Linear Regr":make_pipeline(
        StandardScaler(),
        LinearRegression()
    ),

    "DT":DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    ),

    "RF":RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
}

cv =KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

for name , model in models.items():

    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="neg_m_a_e"#Scikit-learn uses negative values for loss metrics so that higher scores are better during model selection.
    )

    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test,predictions)
    r2=r2_score(y_test,predictions)

    print("\n Model:",name)
    print("Avg CV MAE:", -scores.mean())#to display the normal positive MAE.
    print("Test MAE:", mae)
    print("Test R2:",r2)



#Lower MAE = better predictions.
#Higher R² = generally better fit