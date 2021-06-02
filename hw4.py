import numpy as np
import math

def target_function(x1 , x2):
  result = (3 - x1) ** 2 + \
      7 * (x2 - x1**2)**2
  return result    


def theta_function(x1 , x2 , d1 , d2 , lambda_):
  result = (3 - (x1 + lambda_ * d1)) ** 2 +\
            7 *((x2 + lambda_ * d2) - (x1 + lambda_* d1)**2) ** 2
  return result

def theta_function_fst(x1 , x2, d1 , d2 , lambda_):
  part1 = 2 * (3 - (x1 + lambda_ * d1)) * (-d1)
  part2 = 14*((x2 + lambda_*d2) - (x1 + lambda_*d1)**2)*\
          (d2 - 2 * (x1 + lambda_* d1)*d1)
  result = part1 + part2
  return result        

def target_function_gradient(x1 , x2):
  x1_gradient = 2 * (3 - x1) * (-1) + 14 * (x2 - x1**2)*(-2*x1)
  x2_gradient = 14 * (x2 - x1**2)
  return [x1_gradient , x2_gradient]    

def bisection(x1 , x2 , d1 , d2 , f, f1, interval=[0,5] , l=1e-4):
  a = interval[0]
  b = interval[1]
  lambda_k = (a + b) / 2
  while (b-a) >= l:
    #print(round(lambda_k ,4) , round(f(lambda_k) , 4))
    if f1(x1 , x2 , d1 , d2, lambda_k) > 0:
      b = lambda_k
    elif f1(x1 , x2 , d1 , d2, lambda_k) < 0:
      a = lambda_k
    else :
      return  lambda_k #, f(x1 , x2 , d1, d2 ,lambda_k)
    lambda_k = (a + b) /2
  
  #print(lambda_k)  
  return lambda_k #, f(x1 , x2 , d1 , d2 ,lambda_k)

def cyclic_method(x1 , x2, 
                  tf ,f , f1 , find_lambda, i ,eps=2e-2):
  x1 = x1
  x2 = x2
  value = tf(x1 ,x2)
  iteration = i
  print('Iteration: {} (x1,x2,value): {:3.4f} {:3.4f} {:3.4f}'.format(
      iteration, x1 ,x2 , value))
  
  for i in range(2):
    if i == 0:
      x1_new = x1 + find_lambda(x1 , x2 , 1, 0 ,f ,f1)
    else:
      x2_new = x2 + find_lambda(x1_new , x2 , 0 , 1 ,f ,f1)
  if (x1 - x1_new)**2 + (x2 - x2_new)**2 >= eps**2:
    iteration += 1
    cyclic_method(x1_new , x2_new,
                  tf , f , f1 , find_lambda , iteration)    

def DFP_method(x1 ,x2 , gf , 
               tf ,f ,f1 ,find_lambda, i ,eps=2e-2):
  
  x1 = x1  
  x2 = x2
  value = tf(x1 , x2)
  
  gradient = np.array(gf(x1 , x2))
  gradient_dist = np.linalg.norm(gradient)
  d_matrix = np.identity(2)
  
  iteration = i
  print('Iteration: {} (x1 , x2 , value): {:3.4f} {:3.4f} {:3.4f}'.format(
      iteration , x1 , x2 , value))
  
  
  while gradient_dist >= eps:
    d = - d_matrix.dot(np.transpose(gradient))
    lambda_ = find_lambda(x1 , x2 , d[0] , d[1],
                          f, f1)
    x11 = x1 + lambda_ * d[0]
    x21 = x2 + lambda_ * d[1]

    gradient2 = np.array(gf(x11 , x21))
    p = np.array([lambda_ * d[0] , lambda_ * d[1]])
    q = gradient2 - gradient
    
    p = p.reshape(2,1)
    q = q.reshape(2,1)
    
    part1 = d_matrix

    part2 = np.dot(p,np.transpose(p)) / np.dot(np.transpose(p) , q)
    part3 = np.dot(d_matrix.dot(q) , np.transpose(q).dot(d_matrix))\
        / np.transpose(q).dot(np.dot(d_matrix , q))
    
    d_matrix = part1 + part2 - part3
    
    d2 = - d_matrix.dot(np.transpose(gradient2))      
    lambda_ = find_lambda(x11, x21 , d2[0] , d[1],
                          f , f1)
    
    x1 = x11 + lambda_ * d2[0]
    x2 = x21 + lambda_ * d2[1]
    
    iteration += 1
    value = tf(x1 ,x2)    
    print('Iteration: {} (x1 , x2 , value): {:3.4f} {:3.4f} {:3.4f}'.format(
      iteration , x1 , x2 , value))
    
    gradient = np.array(gf(x1 , x2))
    gradient_dist = np.linalg.norm(gradient)
    d_matrix = np.identity(2)
    
    
    

def steepest_descent_method(x1 , x2, gf,
                            tf , f , f1 , find_lambda , i ,eps=2e-2):
  
  gradient = gf(x1 , x2)
  gradient_dist = np.linalg.norm(gradient)
  
  iteration = i

  x1 = x1
  x2 = x2
  value = tf(x1 , x2)
  
  print('Iteration: {} (x1 , x2 , value): {:3.4f} {:3.4f} {:3.4f}'.format(
      iteration , x1 , x2 , value))
  
  if gradient_dist >= eps:
    x1_d = - gradient[0]
    x2_d = - gradient[1]
    lambda_ = find_lambda(x1 , x2, 
                          x1_d , x2_d,
                          f , f1)
    
    x1 = x1 + lambda_ * x1_d
    x2 = x2 + lambda_ * x2_d
    iteration += 1
    steepest_descent_method(x1, x2, gf, tf, f, f1, find_lambda, iteration)

DFP_method(0, 0, 
           target_function_gradient,
           target_function,
           theta_function,
           theta_function_fst, 
           bisection, 
           1)



'''
steepest_descent_method(0, 0, 
                        target_function_gradient, 
                        target_function,
                        theta_function, 
                        theta_function_fst, 
                        bisection,
                        1)
    

cyclic_method(0, 0,
              target_function,
              theta_function, 
              theta_function_fst,
              bisection,
              1
              )
'''        
      
       
       
         