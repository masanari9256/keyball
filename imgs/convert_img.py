from PIL import Image, ImageOps

for i in range(5):
    im = Image.open(f'img/{i}.png')

    im = im.point(lambda x: 255 if x > 115 else 0)
    # im = im.convert('RGB')
    # im = ImageOps.invert(im)
    im.save(f'converted_img/{i}.png')
