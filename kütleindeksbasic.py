
## girdiler yerine rakam degilde string girersem ne oluyor niye oluyor ? --> lütfen kilonuzu giriniz: gargamel ?: fixed
### Dosya uzantisi yok --> .py vs: fixed
### tek tirnak ve cift tirnak arasinda ne fark var ? --> uzun=input('Uzun Kenar : ') ve boy=int(input("lütfen boyunuz giriniz: ")) arasinda ne fark var ?:
#tek tırnak ile çift tırnak aynı işlevi görür ancak iç içe kullanımda kullanılırlar. örn : print('ahmet "bugün okula gelmicem" dedi')

def get_vki():
    try:
        kg = int(input("lütfen kilonuzu giriniz: "))
        boy = int(input("lütfen boyunuzu giriniz:"))
    except ValueError:
        print("lütfen bir sayı giriniz")
        get_vki()

    boy = boy / 100

    vki = kg / boy ** 2

    if vki < 18.5:
        print("zayıfsınız çünkü kitle indeksiniz", vki)

    elif vki >= 18.5 and vki <= 25.5:
        print("normal kilodasınız kitke indeksiniz", vki)

    elif vki >= 25.5 and vki <= 29.9:
        print("fazla kilodasınız kitle indexsiniz", vki)

    elif vki >= 30 and vki <= 39.9:
        print("şişmansınız kitle indexsiniz", vki)

    elif vki >= 40:
        print("obezite riski mevcut kitle indexsiniz", vki)

get_vki()


