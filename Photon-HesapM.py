
import cmath , math , time , numpy as np 
import matplotlib.pyplot as plt
def toplama():
    a = float(input("Bir sayı giriniz "))
    b = float(input("Bir sayı giriniz "))
    print("Toplam:", a+b)
def çıkarma():
    e = float(input("Bir sayı giriniz "))
    f = float(input("Bir sayı giriniz "))
    print("Toplam:", e-f)
def çarpma():
    t = float(input("Bir sayı giriniz "))
    y = float(input("Bir sayı giriniz "))
    print("Toplam:", t*y)
def bölme():
    u = float(input("Bir sayı giriniz "))
    p = float(input("Bir sayı giriniz "))
    print("Toplam:", u/p)
def karekök():
    s = float(input("Karekökü alınacak sayıyı girin "))
    print("Karekök:", cmath.sqrt(s))
def trigonometri():
    aci = float(input("Açıyı derece cinsinden girin "))
    radyan = math.radians(aci)
    print("Sin:", math.sin(radyan))
    print("Cos:", math.cos(radyan))
    print("Tan:", math.tan(radyan))
def faktöriyel():
    n = float(input("Faktöriyeli alınacak sayıyı giriniz "))
    print("Faktröriyel değeri: ", math.factorial(n))
def logaritma():
    x = float(input("Logu alıncak değeri girin "))
    rt = float(input("Logaritmanın tabanını girin "))
    print("Logaritma değeri:", math.log(x,rt))
    print("Doğal logaritma değeri:", math.log(x))
def fonksiyonlar():
    alt_sinir = float(input("Alt sınırı girin "))
    ust_sinir = float(input("Üst sınırı girin "))
    fonk = input("Fonksiyonu girin (örnek: x**2,np.sin(x)): "  )
    tr = np.linspace(alt_sinir, ust_sinir, 400)
    ef = eval(fonk)
    plt.plot(tr, ef)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"yt = {fonk}")
    plt.grid(True)
    plt.show()
def kombinasyon():
    kom = int(input("Bir değer girin "))
    kom2 = int(input("ikinci değeri girin"))
    if kom2 > kom:
        print("Hata: İkinci değer birinciden büyük olamaz!")
    else:
        print("Kombinasyon değeri:", math.comb(kom, kom2))
def permütasyon():
    per = int(input("Bir değer girin "))
    per2 = int(input("ikince değeri girin "))
    if per2>per:
        print("Hata: İkinci sayı birinciden büyük olamaz! ")
    else:
        print("Permütasyon değeri:", math.perm(per, per2))
def menu():
    while True:
        print("\nPhoton Hesap Makinesi\n")
        konusma = input("Size nasıl yardımcvı ola bilirim?  ")
        if konusma == "Help me": 
         print("Toplama")
         print("Çıkarma")
         print("Çarpma")
         print("Bölme")
         print("Karekök")
         print("Trigonometri")
         print("Faktöriyel")
         print("Logaritma")
         print("Fonksiyon Çizimi")
         print("Kombinasyon")
         print("Permütasyon")
         print("Çıkış") 
        elif konusma == "Toplama":
            toplama()
        elif konusma == "Çıkarma":
            çıkarma()
        elif konusma == "Çarpma":
            çarpma()
        elif konusma == "Bölme":
            bölme()
        elif konusma == "Karekök":
            karekök()
        elif konusma == "Trigonometri":
            trigonometri()
        elif konusma == "Faktöriyel":
            faktöriyel()
        elif konusma == "Logaritma":
            logaritma()
        elif konusma == "Fonksiyon Çizimi":
            fonksiyonlar()
        elif konusma == "Kombinasyon":
            kombinasyon()
        elif konusma == "Permütasyon":
            permütasyon()
        elif konusma == "Çıkış":
            print("Hesap makinesinden çıkılıyor...")
            time.sleep(5)
            break  
  

    