import numpy as np
import math 

def fib_sequence(n):
  if n < 0:
    return -1
  elif n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return fib_sequence(n-1) + fib_sequence(n-2)

def target_function(lambda_):
  return (lambda_ + lambda_ ** 3) ** 2 + 512

def target_function2(lambda_):
  part1 = ((5- 2 * lambda_) + (4 + lambda_)**3)**2
  part2 = 2 * ((5-2*lambda_) - (4 + lambda_) - 4)**4
  result = part1 + part2
  return result    

def golden_section_method(interval , l , f , i):
  
  iteration = i  
  alpha = 0.618
  a = interval[0]
  b = interval[1]
  
  lambda_ = a + (1-alpha) * (b-a)
  mu_ = a + alpha * (b-a)
  f_lambda = f(lambda_)
  f_mu = f(mu_)
  
  print('Iteaation:  a   b  lambda  mu  theta_lambda   theta_mu')
  print('{}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}'.format(
      iteration , a , b , lambda_ , mu_ , f_lambda , f_mu))
  while (b-a) >= l:
    if f_lambda > f_mu:
      a = lambda_
      lambda_ = mu_
      mu_ = a * (1-alpha) + alpha * b
      f_lambda = f_mu
      f_mu = f(mu_)
    else:
      b = mu_
      mu_ = lambda_
      lambda_ = a * alpha + (1-alpha)*b
      f_mu = f_lambda
      f_lambda = f(lambda_)
    iteration += 1
    print('{}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}'.format(
      iteration , a , b , lambda_ , mu_ , f_lambda , f_mu))
    
  mid_point = (a + b) / 2
  print('Answer: {:3.4f} , Midpoint: {:3.4f}'.format(
      f(mid_point) , mid_point))    

def fib_method(interval , eps , fib_sequence , f):
  a = interval[0]
  b = interval[1]
  fn_number = math.ceil((b-a)/eps)
  iter_needed = 0
  
  while fib_sequence(iter_needed) < fn_number:
    iter_needed += 1
  
  # start from here
  fib_list = []
  for i in range(iter_needed + 1):
    if i == 0 or i == 1:
      fib_list.append(1)
    else:
      fib_list.append(fib_list[i-1] + fib_list[i-2])
  
  print('Iteration  a  b    lambda    mu  theta_lambda  theta_mu')
    
  lambda_ = a + fib_list[iter_needed-2]/fib_list[iter_needed]*(b-a)  
  mu_ = a + fib_list[iter_needed-1]/fib_list[iter_needed]*(b-a)
  f_lambda = f(lambda_)
  f_mu = f(mu_)
  
  iteration = 1
  print('{}     {:3.4f} {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}'.format(
      iteration , a , b ,lambda_ , mu_ , f_lambda , f_mu))
  for k in range(1,iter_needed):
    
    if k == iter_needed - 1:  
      mu_ = lambda_ + eps
      if f(mu_) > f(lambda_):
        a = lambda_
      else:
        b = lambda_      
      iteration += 1
      print('{}    {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}  {:3.4f}'.format(
       iteration , a , b ,lambda_ , mu_ , f(lambda_) , f(mu_)))
      continue
            
    if f_lambda > f_mu:
      a = lambda_
      lambda_ = mu_
      mu_ = a + fib_list[iter_needed-k-1]/fib_list[iter_needed-k] * (b-a)#start from here 
      f_mu = f(mu_)
    else:
      b = mu_
      mu_ = lambda_
      lambda_ = a + fib_list[iter_needed-k-2]/fib_list[iter_needed-k] * (b-a)
      f_lambda = f(lambda_)
        
    iteration += 1
    print('{}     {:3.4f} {:3.4f} {:3.4f} {:3.4f} {:3.4f} {:3.4f}'.format(
      iteration , a , b ,lambda_ , mu_ , f_lambda , f_mu))
    
  mid_point = (a + b) / 2
  #print(mid_point)       
  print('Answer: {:3.4f} , Midpoint: {:3.4f}'.format(
      f(mid_point) , mid_point))  

golden_section_method([-2,2], 0.01, target_function2, 1)

#fib_method([0,5] , 1e-2 , fib_sequence , target_function) 