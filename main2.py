from PIL import Image
import imagehash

gorsel1 = Image.open('Flower-with-a-bee.jpg')
width = gorsel1.width
height = gorsel1.height
hash1 = imagehash.whash(gorsel1)  # phash

gorsel2 = Image.open('Flower-with-a-bee.jpg')
gorsel2 = gorsel2.resize((width, height))

hash2 = imagehash.whash(gorsel2)  # phash

fark_orani = hash1 - hash2

yuzde = ((100 - fark_orani) / 100) * 100
print("En yüksek benzerlik oranı:", yuzde)

