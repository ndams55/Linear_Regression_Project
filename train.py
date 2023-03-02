# Instanciate the LinearRegression class 
model1= LinearRegression(method = "Normal_Eq")
model2= LinearRegression(method = "CGS")

# Train the model
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)