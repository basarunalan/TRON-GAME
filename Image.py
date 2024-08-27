from PIL import Image

# Görüntüyü aç
image = Image.open("match_history.png")

# Görüntüyü GIF formatına dönüştür
new_image = image.resize((50, 70))
image.save("Documents/match_history.gif")