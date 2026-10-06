# fibonacci

def fibonacci(n):
    a = 0
    b = 1
    liste = []
    for i in range(n):
        liste.append(a)
        a, b = b, a + b
    return liste


sayi = int(input("Kac eleman yazdirayim: "))
print(fibonacci(sayi))

#özyinelemeli denemeksel (recursive)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


sayi = int(input("Kac eleman yazdirayim: "))

for i in range(sayi):
    print(fibonacci(i), end=" ")
print()

#yuksek degerlerde yavaslar

#asagıdaki ileri konulardan alinmis hizlandirma saglar

# fibonacci recursive + lru_cache (hizlandiran)

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


sayi = int(input("Kac eleman yazdirayim: "))

for i in range(sayi):
    print(fibonacci(i), end=" ")
print()