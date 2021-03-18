'''buyuk=int(input())
while True:
    sayi=int(input())
    if sayi==-1:
        print("Islem-bitti")
        break
    if sayi>buyuk:
        print(sayi,'buyuk-sayi')
    elif sayi==buyuk:
        print("Beraberler")
    else:
        print(buyuk,'buyuk-sayi')'''
#asagidaki-calihshma-number-5i
'''a=int(input())
for i in range(a,20):
    print(i)'''
'''alfabe='alfabe'
for i in alfabe:
    print(i)'''
#meselen-123456-nin-reqemlerini-alt-alta-chap-etmek-isteyirik
'''for reqem in '123456':
    print(reqem)'''
#mesele-1 ile 20 arasındaki tek sayılar
'''for reqem in range(0,20,2):
    print(reqem)'''
#100’den başlayarak 0’a kadar olan sayıları onar onar azaltın.
'''for reqem in range(100,0,-10):
    print(reqem)'''
#7) Bir sınıfın herhangi bir dersten not ortalamasını hesapladığımızı düşünün.
# Kullanıcıdan sınıf mevcudunu girmesini isteyin.
# Daha sonra sınıfta ne kadar öğrenci varsa adlarını, soyadlarını ve o derse
# ait notlarını yazmamızı sağlayacak bir döngü oluşturun ve girilen değerleri ekrana bastırın.
# En sonda ise sınıfın o derse ait not ortalamasını gösterin.
'''usaq_sayi=int(input())
ort=0
for i in range(1,usaq_sayi+1):
    shagird_adi=input("{}.".format(i))
    shagird_soyadi=input("{}.".format(i))
    shagird_bali=int(input("{}.".format(i)))
    ort=shagird_bali+ort
    print("Shagirdin-adi--bali:",shagird_adi,shagird_soyadi,shagird_bali)
    print("{} {} adli-shagirdin-bali {}".format(shagird_adi,shagird_soyadi,shagird_bali))
print("Ortalama:",(ort/usaq_sayi))'''
#8)Bir sayının faktöriyelini gösterecek programı yazınız

'''reqem=int(input("Ededi-daxil-edin:"))
pre=1
for i in range(1,reqem+1):
    if reqem==0:
        print("{} !=1".format(reqem))
        break

    else:
        pre=pre*i
     print("{}!={}".format(reqem,pre))'''
#9) cümle = "Python 2019'da en popüler dil haline gelmiştir."
#Yukarıdaki değişkeni bir döngü içerisinde kullanın ve aradaki boşlukları
#kaldırıp cümleyi ekrana bastırın.
#İpucu: print() fonksiyonunda kullanılan end="" parametresi, fonksiyon içerisinde
#kullanılan herhangi bir ifadeden sonra yeni satıra geçmeyi engeller.

'''ifade = "Python 2019'da en pupular dil haline gelmiştir."
for i in ifade:
     if i==" ":
         continue
     print(i,end=" ")'''
'''ifade = "Python 2019'da en popüler dil haline gelmiştir."
for i in ifade:
    if i == " ":
        continue
        print(" boslug-goruldu")
    print(i, end = "")'''
#polindrom-eded
'''n = int(input("Bir sayı girin: "))
yedek = n
ters = 0

while (n > 0):
    rakam = n % 10
    ters = ters * 10 + rakam
    n = n // 10

if (yedek == ters):
    print("Palindrom sayıdır.")
else:
    print("Palindrom sayı deyil.")
'''
'''import random

yazı = 0
tura = 0

for i in range(1, 1001):
    atış = random.randint(0, 1)
    if atış == 1:
        yazı += 1
    if atış == 0:
        tura += 1

print("Tura: ", tura)
print("Yazı: ", yazı)'''


#eded-cutleri

'''a="123456789"
b='123456789'
for i in a:
    for k in b:
        print("({},{})".format(i,k))
 '''

#15) On dördüncü sorudaki çözümü baz alarak 1-9 arasındaki sayıların çarpım tablosunu ekrana bastırın.
'''
a='123456789'
b='123456789'
for i in a:
    for j in b:
        print(int(i) * int(j))
        '''
#about-errors
'''
try:
    ilkeded=int(input())
    ikincieded=int(input())
    print("%.3f"%(ilkeded/ikincieded))
except ZeroDivisionError:
    print("Sifira-bolemezsiniz!")'''
'''
ilkeded=int(input())
ikincieded=int(input())
a=ilkeded/ikincieded
print("%.2f"%a)
'''

