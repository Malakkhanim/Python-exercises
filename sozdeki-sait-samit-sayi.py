qalin='a,ı,o,u'
ince='e,ə,i,ö,ü'
soz=input("Sozu-daxil-edin:")
soz=tuple(soz)
print(soz)
qalins=0
inces=0
for i in soz:
    if i in qalin:
        qalins+=1
    elif i in ince:
        inces+=1

print("Qalin-saitlerin-sayi",qalins)
print("Ince-saitlerin-sayi",inces)

