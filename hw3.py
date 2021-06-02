import math
import numpy as np

def target_function(lambda_):
  return 6 * math.exp(-2 * lambda_) + 2 * lambda_ ** 2

def target_function_fst(lambda_):
  return -12 * math.exp(-2 * lambda_) + 4 * lambda_

def target_function_sec(lambda_):
  return 24 * math.exp(-2 * lambda_) + 4    

def netwon_method(eps , orginal_lambda , f , f1 , f2):
  iter_lambda = orginal_lambda
  while abs(f1(iter_lambda)) >= eps:
    print(round(iter_lambda , 4) , round(f(iter_lambda),4))  
    iter_lambda -= (f1(iter_lambda)/f2(iter_lambda))
  
  return f(iter_lambda)

def bisection_method(interval, l , f , f1):
  a = interval[0]
  b = interval[1]
  lambda_k = (a + b) / 2
  while (b-a) >= l:
    print(round(lambda_k ,4) , round(f(lambda_k) , 4))
    if f1(lambda_k) > 0:
      b = lambda_k
    elif f1(lambda_k) < 0:
      a = lambda_k
    else :
      return f(lambda_k)
    lambda_k = (a + b) /2
  
  return f(lambda_k)  
        
        

answer = netwon_method(0.001 , 1 , 
                       target_function,
                       target_function_fst,
                       target_function_sec)        
print('Answer: {:3.4f}\n'.format(answer))

answer2 = bisection_method([0,5], 0.01 , 
                           target_function,
                           target_function_fst)
print('Answer2: {:3.4f}'.format(answer2))      