from PIL import Image
import imagehash

gorsel1 = Image.open('7.png')
width = gorsel1.width
height = gorsel1.height
hash1 = imagehash.whash(gorsel1)  # phash
isim1 = gorsel1.filename
print(isim1, "'in hash değeri:  " + str(hash1) + " Görsel boyutu", width, "x", height)

en_yuksek_benzerlik = 0
en_iyi_aci = 0
for i in range(2, 6):
    gorsel2 = Image.open(f'{i}.png')

    for aci in range(361):
        gorsel2_rotated = gorsel2.rotate(aci)  # açıda döndür
        gorsel2_resized = gorsel2_rotated.resize((width, height))

        hash2 = imagehash.whash(gorsel2_resized)  # phash

        fark_orani = hash1 - hash2
        yuzde = ((100 - fark_orani) / 100) * 100

        if yuzde > en_yuksek_benzerlik:
            en_yuksek_benzerlik = yuzde
            en_iyi_aci = aci
            en_iyi_gorsel = f'{i}.png'

print(
    f"{en_iyi_gorsel} dosyası {en_iyi_aci} derece dönünce gorsel1 ile arrasında en yüksek benzerlik oranı olan {en_yuksek_benzerlik} oluyor")
