from sklearn.model_selection import TimeSeriesSplit

#create sample data
data = list(range(1,16))

#create TIme Series Split

tscv = TimeSeriesSplit(n_splits=5)

#Display Trainig and testing icndices
for fold,(train_index,test_index) in enumerate(
    tscv.split(data),
    start=1
):
    print(f"\n Fold {fold}")

    print("Training data:", [data[i] for i in train_index])

    print("Testing data:", [data[i] for i in test_index])