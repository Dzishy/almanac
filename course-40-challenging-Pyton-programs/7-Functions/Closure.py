# 1
def outer():        # внешняя функция
    n = 5           # лексическое окружение - локальная переменная
 
    def inner():      # локальная функция
        nonlocal n
        n += 1        # операции с лексическим окружением
        print(n)
 
    return inner
  
fn = outer()   # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
fn()    # 6
fn()    # 7
fn()    # 8



#2 
def multiply(n):
    def inner(m): return n * m
 
    return inner
  
fn = multiply(5)
print(fn(5))        # 25
print(fn(6))        # 30
print(fn(7))        # 35


#3
def multiply(n): return lambda m: n * m

fn = multiply(5)
print(fn(5))        # 25
print(fn(6))        # 30
print(fn(7))        # 35


#4
def makeCounter():
    n = 0
    def inner ():
        nonlocal n
        n +=1
        return n
    return inner

counter = makeCounter()
print(counter())  # Вывод: 1
print(counter())  # Вывод: 2
print(counter())  # Вывод: 3

new_counter = makeCounter()
print(new_counter())  # Вывод: 1
print(new_counter())  # Вывод: 2