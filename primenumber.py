
### cok buyuk bir asal sayi denemesi yapmak istersem ne olur --> 243112609 uzeri -1 ornegin: işlem gücüne bağlı olarak sonucun çıkma süresi değişebilir
### Dosya uzantisi yok --> .py vs: fixed
### tek tirnak ve cift tirnak arasinda ne fark var ? --> uzun=input('Uzun Kenar : ') ve boy=int(input("lütfen boyunuz giriniz: ")) arasinda ne fark var ?:
#tek tırnak ile çift tırnak aynı işlevi görür ancak iç içe kullanımda kullanılırlar. örn : print('ahmet "bugün okula gelmicem" dedi')

girdi= int(input('Enter your number here: '))
liste=[]
for i in range(2, girdi):
    if girdi % int(i) == 0:
        liste.append(i)
print(liste)
if len(liste) != 0:
    print(str(girdi)+' Not a Prime Number')
elif len(liste) == 0:
    print(str(girdi)+' Prime Number ')
