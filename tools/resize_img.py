from PIL import Image
import os

files = os.listdir(".")

for file in files:
    if not file.endswith('.py'):
        im = Image.open(file)
        im = im.resize((40, 40))
        im.save(file)