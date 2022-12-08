kisa=input('Kısa Kenar : ')
uzun=input('Uzun Kenar : ')
alan=int(kisa)*int(uzun)
cevre=2*(int(kisa)+int(uzun))
print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))


### Dosya uzantisi yok --> .py vs: fixed

### tek tirnak ve cift tirnak arasinda ne fark var ? --> uzun=input('Uzun Kenar : ') ve boy=int(input("lütfen boyunuz giriniz: ")) arasinda ne fark var ?: 
#tek tırnak ile çift tırnak aynı işlevi görür ancak iç içe kullanımda kullanılırlar. örn : print('ahmet "bugün okula gelmiyeceğim" dedi')


### int deger araligi olan min maks degerler disinda birsey input olarak girersem ne olur ? --> ornegin uzun kenar = 123945830234850453459123 yazarsam ne oluyor niye oluyor ?
### program çalışmaya devam eder. Değerlerin çıktısı:
#Kısa Kenar : 123945830234850453459123
#Uzun Kenar : 123945830234850453459123
#Alan : 15362568832606368814889478104135698276231929129
#Çevre : 495783320939401813836492
