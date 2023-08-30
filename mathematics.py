# -*- coding: utf-8 -*-
def second_derivative(X, Y):
    """
    """
    number_of_points = len(Y)
    Second_deriv = []       
    ###### forward differences of second order ######
    for i in range(0,2):
        step         = X[i+1]-X[i]
        second_deriv = (2*Y[i]-5*Y[i+1]+4*Y[i+2]-Y[i+3])/(step**2)
        Second_deriv.append(second_deriv)
    ###### central differences of second order #####
    i=2 #initialization   
    while i<=number_of_points-3:
        step         = X[i+1]-X[i]
        second_deriv = (Y[i-1] -2*Y[i] +Y[i+1])/(step**2)
        Second_deriv.append(second_deriv)
        i +=1
    ###### backwards differences of second order ######
    for i in range(number_of_points-2,number_of_points):
        step         = X[i]-X[i-1]
        second_deriv = (-Y[i-3]+4*Y[i-2]-5*Y[i-1]+2*Y[i])/(step**2)
        Second_deriv.append(second_deriv)
        
    return Second_deriv