def add_ones(X):

  # ADD YOUR CODES
  onesArray = np.ones((len(X), 1))
  
  return hstack((onesArray, X))


  ## Get X and y
X,y= get_data()
X

## Add ones to X
X= add_ones(X)
X

def split_data(X,Y, train_size):
  # ADD YOUR CODES
  # shuffle the data before splitting it
  data = np.concatenate((X, Y), 1)
  np.random.shuffle(data)

  
  n_train = round(len(data)*train_size)
  n_test = len(data) - n_train

  data_train = data[:n_train, :]
  data_test = data[:n_test, :]

  X_train, y_train = data_train[:, :-1], data_train[:, -1]
  X_test, y_test = data_test[:, :-1], data_test[:, -1]

  y_train = y_train.reshape(len(y_train),1)
  y_test = y_test.reshape(len(y_test),1)

  return X_train, X_test, y_train, y_test

# Split (X,y) into X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test= split_data(X, y, train_size = 0.8)

print(X_train.shape, y_train.shape, y_test.shape, X_test.shape)