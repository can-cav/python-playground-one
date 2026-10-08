#girilen dort basamakli sayiyi yaziya cevirmek

def number_to_words(number):
    ones = ["", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
    tens = ["", "on", "yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]

    if not (1000<= number<= 9999):
        return "4 bas sayi gir"

 # sayiyi parcaliyoruz
    one_digit = number % 10   #birler bas
    ten_digit = (number // 10) % 10
    hundred_digit = (number // 100) % 10
    thousand_digit = number // 1000

    parts = []  # kelimeleri buraya ekleyip sonda birlestiriyoz

# binler: 1000 "bir bin" degil "bin" diye okunur
    if thousand_digit > 1:
        parts.append(ones[thousand_digit])
    parts.append("bin")

# yuzler: 100 "bir yuz" degil "yuz" diye okunur
    if hundred_digit > 1:
        parts.append(ones[hundred_digit])
    if hundred_digit > 0:
        parts.append("yuz")

# onlar ve birler (0 ise bos string eklenir so kontrol)
    if ten_digit > 0:
        parts.append(tens[ten_digit])
    if one_digit > 0:
        parts.append(ones[one_digit])

    return " ".join(parts)


number = int(input("4 basamakli bir sayi gir: "))
print(number_to_words(number))
