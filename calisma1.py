# --- degiskenler ---
class ClassBir:
    def __init__(self):
        self.ad = "Cans"
        self.yas = 19
        self.boy = 176
        #burada int degeri tirnak ici

    def yazdir(self):
        print("Adim:", self.ad)
        print("Yasim:", self.yas)
        print("Boyum:", self.boy)


# --- if else ---
class ClassIki:
    def not_hesapla(self, not1):
        if not1 >= 50:
            print("Gectin")
        else:
            print("Kaldin") 
            # ders tekrari lazim


# --- donguler ---
class ClassUc:
    def say(self):
        for i in range(1, 6):
            print(i)
            
        #range deger 0 1 2 3 4 5

    def carpim_tablosu(self, sayi):
        for i in range(1, 11):
            print(sayi, "x", i, "=", sayi * i)


# --- liste ---
class ClassDort:
    def __init__(self):
        self.dersler = ["mat", "fiz", "prog"]

    def listele(self):
        for ders in self.dersler:
            print("Ders:", ders)

    def ekle(self, yeni_ders):
        self.dersler.append(yeni_ders)
        print(yeni_ders, "eklendi")


# --- ortalama (bunu hocanin sorusundan yaptim) ---
class ClassBes:
    def ortalama(self, liste):
        toplam = 0
        for n in liste:
            toplam = toplam + n
        return toplam / len(liste)


# --- deneme kismi ---
a = ClassBir()
a.yazdir()

b = ClassIki()
b.not_hesapla(65)
b.not_hesapla(30)

c = ClassUc()
c.say()
c.carpim_tablosu(7)

d = ClassDort()
d.listele()
d.ekle("ing")
d.listele()

e = ClassBes()
print("Ortalama:", e.ortalama([70, 85, 90, 60]))

