import numpy as np
from scipy.special import expit

def calculate_loss(y, tx, w):
    """compute the cost by negative log likelihood."""
    Loss=[]  
    for i in range(len(y)):
        sigmoid = expit(tx[i] @ w);
        Loss.append( -(y[i]*np.log(sigmoid)+(1-y[i])*np.log(1-sigmoid)) )
    
    return np.array(np.sum(Loss))


def calculate_gradient(y, tx, w):
    """compute the gradient of loss."""
    return tx.T @ (expit(tx @ w) - y)


def learning_by_gradient_descent(y, tx, w, alpha):
    """
    Do one step of gradient descent using logistic regression.
    Return the loss and the updated w.
    """  
    loss = calculate_loss(y, tx, w)
    w = w - alpha * calculate_gradient(y, tx, w)
    
    return loss, w


def calculate_hessian(y, tx, w):
    """return the hessian of the loss function."""
    N = len(y)
    
    temp=[]
    S = np.zeros((N,N))
    for i in range(N):
        sigmoid = expit(tx[i] @ w);
        S[i][i] = ( sigmoid * (1 - sigmoid) )
 
    return tx.T @ S @ tx


def logistic_regression(y, tx, w):
    """return the loss, gradient, and hessian."""
    loss = calculate_loss(y, tx, w)
    gradient = calculate_gradient(y, tx, w)
    hessian = calculate_hessian(y, tx, w)
    
    return loss, gradient, hessian


def learning_by_newton_method(y, tx, w, alpha):
    """
    Do one step on Newton's method.
    return the loss and updated w.
    """
    loss, gradient, hessian = logistic_regression(y, tx, w)
    w = w - alpha * np.linalg.solve(hessian, gradient)
    
    return loss, w


def penalized_logistic_regression(y, tx, w, lambda_):
    """return the loss, gradient, and hessian."""
    loss = calculate_loss(y, tx, w) + lambda_ * np.sum(w**2)
    gradient = calculate_gradient(y, tx, w) + lambda_ * 2 * w
    hessian = calculate_hessian(y, tx, w) + 2 * lambda_
    
    return loss, gradient, hessian


def learning_by_penalized_gradient(y, tx, w, alpha, lambda_):
    """
    Do one step of gradient descent, using the penalized logistic regression.
    Return the loss and updated w.
    """
    loss, gradient, hessian = penalized_logistic_regression(y, tx, w, lambda_)
    w = w - alpha * np.linalg.solve(hessian, gradient)
    
    return loss, w


