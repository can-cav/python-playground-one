#burada pozitif tam sayi bolen bulunacak

def find_divisors(sayi):
    divisors = [item for item in range(1, sayi + 1) if sayi % item == 0]
    return divisors

try:
    sayi = int(input("Pozitif deger gir: "))
    if sayi <= 0:
        print("POZITIF sayi gir")
    else:
        result = find_divisors(sayi)
        print(f"Tam sayi bolenleri {sayi}: {result}")
except ValueError:
    print("GECERLI DEGER GIR")
