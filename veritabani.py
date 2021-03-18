#veri-tabani-olushturma-okul-icin


data=[]
ad_soyad=[]
numara=[]
ders=[]
for i in range(3):
    ad=input("Ismi-daxil-edin:")
    num=int(input('Ogrencinin-numarasi:'))
    d=input("fenni-daxil-edin:")
    ad_soyad.append(ad)
    numara.append(num)
    ders.append(d)

data=[ad_soyad,numara,ders]
print(data)
for i in range(len(data)):
    data[i].sort()
print(data)