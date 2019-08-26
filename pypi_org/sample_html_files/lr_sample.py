import numpy as np
X_train = np.array([[1, 6, 975, 0], [0, 2, 0, 0], [0, 5, 0, 0],  [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], dtype=object)
Y_train = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0], dtype=object)

# y_temp = [0 if Y_train ==0 else 1]
# Y_train

Y_train = np.asarray(Y_train,dtype=np.float64)

print(X_train.shape, Y_train.shape)

from sklearn.linear_model import LogisticRegression


model = LogisticRegression()

model.fit(X_train, Y_train)

y_test = model.predict([[1, 6, 975, 0]])