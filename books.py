import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("books.csv")


X = data.drop(columns=["Title","Author","Image"])

y = data[["Title","Author","Image"]]

model = DecisionTreeClassifier()

model.fit(X.values, y)

predicted_value = model.predict([[2, 6]])

print(predicted_value)


