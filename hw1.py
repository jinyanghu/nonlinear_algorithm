import math
import numpy as np
from pathlib import Path

def target_function1(lambda_):
  return 6 * math.exp(-2 * lambda_) + 2 * lambda_ ** 2
    
def dich_method(interval , eps , l , f):
  a = interval[0]
  b = interval[1]
  
  iteration = 1
  print('Iteration:  ' , ' a ' , ' b ' , ' lambda ' , ' mu ' , ' f(lambda) ' , ' f(mu) ')
  while b-a > l:
    lambda_k = (a + b) / 2 - eps
    mu_k = (a + b) / 2 + eps
    
    f_l = f(lambda_k)
    f_mu = f(mu_k)
    
    #print(iteration , a , b , lambda_k , mu_k , f_l , f_mu)     
    print('{}      {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}'.format(
        iteration , a , b ,lambda_k , mu_k , f_l , f_mu))
    if f_l < f_mu:
      b = mu_k
    else:
      a = lambda_k
    
    iteration += 1
  
  print(str(iteration), "    " ,round(a , 4) , round(b , 4))  
  mid_point = (a + b) /2
  print(round(mid_point , 4))
  return f(mid_point)  


answer = dich_method([0,5], 0.001, 0.01 , target_function1)
print('Final_answer: {:3.4f}'.format(answer))
       