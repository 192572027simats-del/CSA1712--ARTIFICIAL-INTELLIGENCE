
from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 1, 0, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[1, 0]])
print("Prediction:", prediction[0])
