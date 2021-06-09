import numpy as np
from scipy.optimize import minimize
import math

def function(x1 ,x2):
  return x1**2 + 4*x2**2 -8*x1-16*x2

def constraint_function(x1 , x2):
  c1 = max(x1 + x2 - 5 , 0)**2
  c2 = max(-x1,0)**2
  c3 = max(x1 -3 , 0)**2
  c4 = max(-x2, 0)**2
  return c1+c2+c3+c4

def penalty_function(x1 , x2 , mu_):
  return function(x1,x2) + mu_ * constraint_function(x1,x2)

penalty_func = lambda x: (x[0] ** 2) + 4*(x[1]**2) + -8*x[0]-16*x[1]
h_11 = lambda x: (x[0] + x[1] - 5)
h_21 = lambda x: (-x[0])
h_31 = lambda x: (x[0] - 3)
h_41 = lambda x: (-x[1])

x0 = [4, 2]
cons = ({'type': 'ineq', 'fun': h_11},
       {'type': 'ineq', 'fun': h_21},
       {'type': 'ineq', 'fun': h_31},
       {'type': 'ineq', 'fun': h_41}) 
ans = minimize(penalty_func, x0, constraints=cons).x
print(ans)

print('Penalty function method:')
init_x = [4,2]
mu_ = 1/2
iteration = 1
penalty_func = lambda x: x[0] ** 2 + 4 * (x[1]**2)- 8*x[0]- 16*x[1]+\
    mu_ * (max(x[0] + x[1] - 5 , 0)**2 + 
           max(-x[0],0)**2 + 
           max(x[0] - 3 , 0)**2 +
           max(-x[1], 0)**2)
init_x = minimize(penalty_func , init_x).x
ans = function(init_x[0] , init_x[1]) 
print('Iteration: {} (x1 , x2 , ans) :{:3.4f} {:3.4f} {:3.4f}'.format(
    iteration, init_x[0] , init_x[1],ans))


while constraint_function(init_x[0] , init_x[1]) * mu_ >= 0.03:
  iteration += 1
  penalty_func = lambda x: x[0] ** 2 + 4 * (x[1]**2)- 8*x[0]- 16*x[1]+\
    mu_ * (max(x[0] + x[1] - 5 , 0)**2 + 
           max(-x[0],0)**2 + 
           max(x[0] -3 , 0)**2 +
           max(-x[1], 0)**2)
  init_x = minimize(penalty_func , init_x).x
  ans = function(init_x[0] , init_x[1])
  mu_ = 2*mu_             

  print('Iteration: {} (x1 , x2 , ans) :{:3.4f} {:3.4f} {:3.4f}'.format(
      iteration, init_x[0] , init_x[1],ans))


print('\nBarrier function method: ')
x0 = [1 , 1]
mu = 8
func = lambda x: (x[0] ** 2) + 4*(x[1]**2) + -8*x[0]-16*x[1]
h_1 = lambda x: -1 / (x[0] + x[1] - 5)
h_2 = lambda x: -1/ (-x[0])
h_3 = lambda x: -1/ (x[0] - 3)
h_4 = lambda x: -1 / (-x[1])
barrier_func = lambda x: func(x) + mu * (h_1(x) + h_2(x) + h_3(x) + h_4(x))

iteration = 1
x0 = minimize(barrier_func ,x0 ,method='COBYLA').x
ans = function(x0[0] , x0[1])

print('Iteration: {} (x1 , x2 , ans) :{:3.4f} {:3.4f} {:3.4f}'.format(
    iteration, x0[0] , x0[1], ans))

while (h_1(x0) + h_2(x0) + h_3(x0) + h_4(x0))*mu > 0.6:
  terminate = False
  mu *= 0.5
  barrier_func = lambda x: func(x) + mu * (h_1(x) + h_2(x) + h_3(x) + h_4(x))
  iteration += 1
  x0 = minimize(barrier_func ,x0 ,method='COBYLA').x
  ans = function(x0[0] , x0[1])
  constraint_list = [h_11 , h_21, h_31 , h_41]
  for c in constraint_list:
    if c(x0) > 0:
      terminate = True
      break

  if terminate:
    break         

  print('Iteration: {} (x1 , x2 , ans) :{:3.4f} {:3.4f} {:3.4f}'.format(
      iteration, x0[0] , x0[1],ans))
      
