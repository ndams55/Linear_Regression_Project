# cgs
def cgs(A):
  """
    Q,R = cgs(A)
    Apply classical Gram-Schmidt to mxn rectangular/square matrix. 

    Parameters
    -------
    A: mxn rectangular/square matrix   

    Returns
    -------
    Q: mxn square matrix
    R: nxn upper triangular matrix

  """
  # ADD YOUR CODES
  m= len(A) # get the number of rows of A
  n= len(A[0]) # get the number of columns of A

  R= np.zeros((n,n))# create a zero matrix of nxn
  Q= A.copy() # copy A (deep copy)

  for k in range(0,n):
    w = A[:m, k:k+1]
    for j in range(0, k):
      R[j][k] = np.dot(Q[:m, j:j+1].T, w)
    for j in range(0, k):
      w = w - R[j][k]*Q[:m, j:j+1]

    R[k][k] = np.linalg.norm(w,2)
    
    Q[:m, k:k+1] = w/R[k][k]

  return Q, R

# Implement BACK SUBS
def backsubs(U, b):

  """
  x = backsubs(U, b)
  Apply back substitution for the square upper triangular system Ux=b. 

  Parameters
  -------
    U: nxn square upper triangular array
    b: n array
    

  Returns
  -------
    x: n array
  """

  n= U.shape[1]
  x= np.zeros((n,))
  b_copy= np.copy(b)

  if U[n-1,n-1]==0.0:
    if b[n-1] != 0.0:
      print("System has no solution.")
  
  else:
    x[n-1]= b_copy[n-1]/U[n-1,n-1]
  for i in range(n-2,-1,-1):
    if U[i,i]==0.0:
      if b[i]!= 0.0:
        print("System has no solution.")
    else:
      for j in range(i,n):
        b_copy[i] -=U[i,j]*x[j]
      x[i]= b_copy[i]/U[i,i]
  return x

def normalEquation(X,y):
  # ADD YOUR CODES
  theta = np.linalg.inv((X.T.dot(X))).dot(X.T).dot(y)
  return theta

class LinearRegression:

  theta = []
  def __init__(self, method):
    # ADD YOUR CODES
    self.method = method
      
  def fit(self,x,y):
    # ADD YOUR CODES
    if self.method == "Normal_Eq":
      self.theta = normalEquation(x, y)
    elif self.method == "CGS":
      Q, R = cgs(x)
      b = np.dot(Q.T, y)
      self.theta = backsubs(R, b)


  def predict(self,x):
    #ADD YOUR CODES
    y_pred = np.dot(x, self.theta)
    return y_pred

