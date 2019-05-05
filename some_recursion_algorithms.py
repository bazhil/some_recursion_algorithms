# Algorithms from lesson https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8

# Matreshka
n = int(input('Введите количество уровней вложенности в матрешке: '))

def matreshka(n):
  if n == 1:
    print('Матрешечка')
  else:
    print('Верх матрешки n =', n)
    matreshka(n-1)
    print('Низ матрешки n =', n)

matreshka(n)

# Squares
import graphics as gr

window = gr.GraphWin('Russian game', 600, 600)
alpha = 0.2

def fractal_rectangle(A, B, C, D, max_deep=10):
  if max_deep < 1:
    return
  for M, N in (A, B), (B, C), (C, D), (D, A):
    gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
  A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
  B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
  C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
  D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
  fractal_rectangle(A1, B1, C1, D1, max_deep-1)
  
fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))

# Factorial
n = int(input('Введите число факториал для которого хотите вычислить факториал '))
def factorial(n:int):
  assert n >= 0, 'Факториал отрицательных чисел не определен'
  if n == 1:
    return 1
  return factorial(n-1) * n

print('Факториал для числа ', n, '=', factorial(n))

# Алгоритм Евклида (поиск наибольшего общего делителя)
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def second_gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

print('Первая реализация алгоритма Евклида: ', gcd(2, 100))
print('Вторая реализация алгоритма Евклида: ', second_gcd(56, 7))

# Быстрое возведение в степень
a = int(input('Введите число '))
n = int(input('Введите степень числа '))

def pow(a:float, n:int):
  if n == 0:
    return 1
  elif n % 2 == 1: #нечетная
    return pow(a, n - 1) * a
  else:
    return pow(a**2, n//2)

print('Число {0} в степени {1} = {2}'.format(a, n, pow(a, n)))
