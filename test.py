y_predict1 = model1.predict(X_test)
y_predict2 = model2.predict(X_test)

normEq_err = mse(y_test, y_predict1)
cgs_err = mse(y_test, y_predict2)