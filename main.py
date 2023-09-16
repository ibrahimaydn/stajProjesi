from PIL import Image
import imagehash
import time

baslangic_zamani = time.time()
en_yuksek_benzerlik = 0
en_dusuk_benzerlik = 100
en_iyi_aci = 0
en_kotu_aci = 0
ayna_kullanildi = False

gorsel1 = Image.open('Flower-with-a-bee.jpg')
hash1 = imagehash.phash(gorsel1)  # 1. için hash değerini hesapla
width = gorsel1.width
height = gorsel1.height
isim1 = gorsel1.filename
print(isim1, "'in hash değeri:  " + str(hash1) + " Görsel boyutu", width, "x", height)



gorsel2 = Image.open('Flower-with-a-bee10.jpg')
hash2 = imagehash.phash(gorsel2)  # 2. için hash değerini hesapla
width2 = gorsel2.width
height2 = gorsel2.height
isim2 = gorsel2.filename
print(isim2, "'nin hash değeri: " + str(hash2) + " Görselin orijinal boyutu", width2, "x", height2)
gorsel2 = gorsel2.resize((width, height))
width2 = gorsel2.width
height2 = gorsel2.height
print(isim2, "'nin hash değeri: " + str(hash2) + " Görselin yenilenmiş boyutu", width, "x", height)

for aci in range(361):  # 0 ile 360 derece arasında dönüş açıları
    gorsel2 = gorsel2.rotate(aci)  # açıda döndür
    hash2 = imagehash.whash(gorsel2)  # phash
    #  print("Gorsel2'nin", aci, " açıya göre hash değeri: " + str(hash2)) # açıya göre hash yazdırma
    fark_orani = hash1 - hash2
    yuzde = ((100 - fark_orani) / 100) * 100

    if yuzde > en_yuksek_benzerlik:
        en_yuksek_benzerlik = yuzde
        en_iyi_aci = aci
        ayna_kullanildi = False

    if yuzde < en_dusuk_benzerlik:  # Check for the lowest similarity
        en_dusuk_benzerlik = yuzde
        en_kotu_aci = aci
    # Ayna görüntüsünü hesaplamak için
    gorsel2_ayna = gorsel2.transpose(Image.FLIP_LEFT_RIGHT)
    hash2_ayna = imagehash.whash(gorsel2_ayna)  # phash

    fark_orani_ayna = hash1 - hash2_ayna
    yuzde_ayna = ((100 - fark_orani_ayna) / 100) * 100

    if yuzde_ayna > en_yuksek_benzerlik:
        en_yuksek_benzerlik = yuzde_ayna
        en_iyi_aci = aci
        ayna_kullanildi = True

if ayna_kullanildi:
    print("\nAyna kullanılarak ve ", en_iyi_aci, " derece dönünce en yüksek benzerlik oranı olan "
          , en_yuksek_benzerlik, " elde edilir.")
else:
    print("\nAyna kullanılmadan ", en_iyi_aci, " derece dönünce en yüksek benzerlik oranı olan "
          , en_yuksek_benzerlik, " elde edilir")

print("\nEn düşük benzerlik oranı olan", int(en_dusuk_benzerlik), en_kotu_aci, "derece dönünce elde ediliyor.\n")
bitis_zamani = time.time()


islemsuresi = bitis_zamani - baslangic_zamani
print(f"Kodun çalışma süresi: {islemsuresi:.2f}", "saniye")



# Hash 1: 00000000 00111110 01111110 00111110 00111110 11111100 00011100 01000010
# Hash 2: 00000000 00100111 11111110 00111010 00111110 11111000 00011100 01000010

# Farklı bit sayısı: 5
# Toplam bit sayısı: 64

# Benzerlik oranı = (Toplam bit sayısı - Farklı bit sayısı) / Toplam bit sayısı
# Benzerlik oranı = (64 - 5) / 64 ≈ 0.921875
