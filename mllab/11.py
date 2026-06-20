import numpy as np
def step(x):
    return 1 if x >= 0 else 0
def perceptron(X, y, lr=0.1, epochs=10):
    w = np.zeros(2)
    b = 0
    for _ in range(epochs):
        for i in range(len(X)):
            pred = step(np.dot(X[i], w) + b)
            error = y[i] - pred
            w += lr * error * X[i]
            b += lr * error
    return w, b
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([0,0,0,1])
w,b = perceptron(X,y_and)
print("AND Gate")
for x in X:
    print(x,"->",step(np.dot(x,w)+b))
y_or = np.array([0,1,1,1])
w,b = perceptron(X,y_or)
print("\nOR Gate")
for x in X:
    print(x,"->",step(np.dot(x,w)+b))