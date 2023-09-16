import base64
import difflib
import time

baslangic_zamani = time.time()
# İlk görselin dosya yolunu belirtin
foto_path1 = 'Flower-with-a-bee.jpg'

# İkinci görselin dosya yolunu belirtin
foto_path2 = 'Flower-with-a-bee3.jpg'

def base64_encode_image(image_path):
    with open(image_path, 'rb') as foto_dosyasi:
        base64_veri = base64.b64encode(foto_dosyasi.read())
    return base64_veri.decode('utf-8')

base64_str1 = base64_encode_image(foto_path1)

base64_str2 = base64_encode_image(foto_path2)

matcher = difflib.SequenceMatcher(None, base64_str1, base64_str2)
similarity_ratio = matcher.ratio()*100

print(f"Benzerlik Oranı % {similarity_ratio:.2f}")
bitis_zamani = time.time()


islemsuresi = bitis_zamani - baslangic_zamani
print(f"Kodun çalışma süresi: {islemsuresi:.2f}", "saniye")
