import pickle
from sklearn.metrics import accuracy_score
from sklearn import neighbors
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import datasets


iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)
classifier = tree.DecisionTreeClassifier()

classifier = neighbors.KNeighborsClassifier()
classifier.fit(x_train, y_train)


pickle.dump(classifier, open('model.pkl', 'wb'))
