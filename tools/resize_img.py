from PIL import Image
import os

files = os.listdir("./imgs")

for file in files:
    if not file.endswith('.py'):
        im = Image.open("./imgs/" + file)
        im = im.resize((40, 40))
        im.save(file)