# -*- coding: utf-8 -*-
"""  Implementation of the basis for Machine Learning practice.

   It contains all the useful functions, as seen in the Labs, to compute
   a prediction function, to be used on test data set.
   
   To use them, you need to import either mse.py, mae.py or any other python script containing
   a custom loss function (with its function to compute the gradient), and pass those functions
   as argument.  """

import numpy as np
import helpers as hlp
import mse


# Function using gradient descent to compute the weight
#
#     y is the train output
#     tx is the train input
#     
#     gamma is the step size to increment w with the gradient (smaller = more preicision but slower convergence)
#     max_iters is the number of iterations we'll do to find the local minimum
#     
#     initial_w is the start weight to go from
#
#     loss_function is the loss function to use to compute the loss
#     gradient_function is the gradient function to use to compute the gradient
#

"""
# Returns
# 
#     losses (sequence of losses for each weight computed)
#     ws (sequence of computed weights)
# 
"""

def least_squares_GD (y, tx, gamma, max_iters, initial_w = np.zeros (tx.shape [1]), loss_function = compute_mse_loss, gradient_function = compute_mse_gradient):
    
    # Initialize w
    w = initial_w
    
    # Define parameters to store w and loss
    ws = []
    losses = []
    
    # Iterate max_iters times to get closer to the local minimum
    for n_iter in range(max_iters):
        
        # Store current weight
        ws.append (np.copy (w))
        
        # Compute and store current loss
        loss = loss_function (y, tx, w)
        losses.append(loss)
        
        # Compute gradient for the next iteration
        if n_iter < max_iters - 1:
            gw = gradient_function (y, tx, w)
            w = w - gamma * gw

    return losses, ws


# Function using stochastic gradient descent to compute the weight
#
#     y is the train output
#     tx is the train input
#     
#     gamma is the step size to increment w with the gradient (smaller = more preicision but slower convergence)
#     max_iters is the number of iterations we'll do to find the local minimum
#     
#     initial_w is the start weight to go from
#     batch_size is the size of the batch to generate for internal use
#
#     loss_function is the loss function to use to compute the loss
#     gradient_function is the gradient function to use to compute the gradient
# 

"""
# Returns
# 
#     losses (sequence of losses for each weight computed)
#     ws (sequence of computed weights)
# 
"""

def least_squares_SGD (y, tx, gamma, max_iters, initial_w = np.zeros (tx.shape [1]), batch_size = len (y) / 10, loss_function = compute_mse_loss, gradient_function = compute_mse_gradient):
    
    # Initialize w
    w = initial_w
    
    # Define parameters to store w and loss
    ws = []
    losses = []
    
    # Iterate max_iters times to get closer to the local minimum
    for minibatch_y, minibatch_tx in batch_iter (y, tx, batch_size, max_iters):
        
        # Store current weight
        ws.append (np.copy (w))
        
        # Compute and store current loss
        loss = loss_function (minibatch_y, minibatch_tx, w)
        losses.append(loss)
        
        # Compute gradient for the next iteration
        if n_iter < max_iters - 1:
            gw = gradient_function (minibatch_y, minibatch_tx, w)
            w = w - gamma * gw
        
    return losses, ws


# Function using Least Squares method to compute the weight (MSE only)
#
#     y is the train output
#     tx is the train input
# 

"""
# Returns
# 
#     w (the exact weight minimizing the loss function for given y and tx)
#     loss (the loss of this optimal w)
# 
"""

def least_squares (y, tx):
    
    w = np.linalg.inv (tx.T.dot (tx)).dot (tx.T).dot (y)
    loss = compute_mse_loss (y, tx, w)
    
    return loss, w


# Function using Ridge Regression method to compute the weight (MAE only)
#
#     y is the train output
#     tx is the train input
#     
#     lambda_ is the regularization parameter
# 

"""
# Returns
# 
#     w (the exact weight minimizing the loss function for given y, tx and lambda)
#     loss (the loss of this optimal w)
# 
"""

def ridge_regression (y, tx, lambda_ = 0):
    
    w = np.linalg.inv (tx.T.dot (tx) + lambda_ * 2 * tx.shape [0] * np.eye(tx.shape [1])).dot (tx.T).dot (y)
    loss = compute_mse_loss (y, tx, w)
    
    return loss, w