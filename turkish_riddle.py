import random

tur = 0
end = 4
hak = 3
puan = 0

while hak > 0:
    
    bilmece = open('Bilmeceler.txt', "r", encoding="utf8")
    cevap = open('cevaplar.txt',"r", encoding="utf8")
    rastgele_sayi = random.randint(0, 6)
    cevap_metin = cevap.read().lower()
    cevap_listesi = cevap_metin.replace('\n','').split(",")
    rastgelecevap = cevap_listesi[rastgele_sayi]
 
    bilmeceler = bilmece.read()
    bilmece_listesi = bilmeceler.replace('\n','').split(".")
    rastgelesoru = bilmece_listesi[rastgele_sayi]
    print(rastgelesoru)
    
    verilen_cevap = input("bilmecenin cevabını giriniz: ").lower()    
    
  
    if rastgelecevap == verilen_cevap:
            print("doğru")  
            puan += 1
            print("puan durumu",puan)
            tur += 1
    else:
           hak -= 1
           print("yanlış")
           print("kalan hak: ",hak)
           print("toplam puan: ",puan)  
           continue
    if hak == 0:
        print("oyun bitti kazanılan puan",puan)
        break
    if tur == 10:
        print("Oyunu kazandınız!")

