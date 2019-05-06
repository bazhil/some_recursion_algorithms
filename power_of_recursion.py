# Power of Recursion
# Взял из лекции https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8

# Генерация чисел для двоичной системы счисления
def gen_bin(M:int, prefix=''):
  """
  Генерирует все числа в двоичной системе счисления длины M
  """
  if M == 0:
    print(prefix)
    return
  for digit in '0', '1':
    gen_bin(M-1, prefix+digit)

# Генерация всех перестановок для произвольной системы счисления
def generate_numbers(N:int, M:int=0, prefix=None):
  """
  Генерирует все числа (с лидирующими незначимыми нулями) 
  в N-ричной системе счисления (N <= 10) длины M
  """
  prefix = prefix or []
  if M == 0:
    print(prefix)
    return
  for digit in range(N):
    prefix.append(digit)
    generate_numbers(N, M - 1, prefix)
    prefix.pop()

def find(number, A):
  """
  Ищет х в А и возвращается true если такой есть и false, если такого нет
  """
  flag = False
  for x in A:
    if number == x:
      flag = True
      break
  return flag

def generate_permutations(N:int, M:int=-1, prefix=None):
  """
  Генерирует перестановки N чисел в M позициях, начиная с префиксом prefix
  """
  M = N if M == -1 else M # по умолчанию N чисел в N позициях
  prefix = prefix or []
  if M == 0:
    print(*prefix)
    return
  for number in range(1, N+1):
    if find(number, prefix): 
      continue
    prefix.append(number)
    generate_permutations(N, M-1, prefix)
    prefix.pop()


# gen_bin(3)
# generate_numbers(3, 3)
# generate_permutations(3, 3)
