import time
import os

def get_ip():
    try:
        ip=input("lütfen saldırmak istediğiniz ip giriniz: ")
        ping= int(input("ping boyutu: "))
        t = int(input("saldırı ne zaman başlasın?(saniye cinsinden): "))
    except ValueError:
        print("lütfen doğru bir değer giriniz")
        get_ip()
    while t:
        dak= t//60
        sny= t%60
        timer = '{:02d}:{:02d}'.format(dak,sny)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("saldırı başladı")
    os.system("ping -c {} {}".format(ping, ip))
    
    ip = ip.split(".")
    if len(ip) != 4:
        print("IP address {} doğru değil".format(ip))
        
    
get_ip() 
