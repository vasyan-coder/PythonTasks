from PIL import Image
import random
import matplotlib.pyplot as plt

sprite_size = 5
spacing = 2
map_size = 40
sprites_row = map_size // sprite_size


def generate_random_sprite():
    img = Image.new('1', (sprite_size, sprite_size))

    for x in range(sprite_size):
        for y in range(sprite_size):
            img.putpixel((x, y), random.randint(0, 1))

    # Число для определения направления оси: 0 - горизонтальная, 1 - вертикальная
    axis = random.randint(0, 1)

    if axis == 0:
        for x in range(sprite_size):
            for y in range(sprite_size // 2, sprite_size):
                pixel_value = img.getpixel((x, y - sprite_size // 2))
                img.putpixel((x, y), pixel_value)
    elif axis == 1:
        for x in range(sprite_size // 2, sprite_size):
            for y in range(sprite_size):
                pixel_value = img.getpixel((x - sprite_size // 2, y))
                img.putpixel((x, y), pixel_value)

    return img


map_width = map_size + sprites_row * spacing + spacing
map_height = map_size + sprites_row * spacing + spacing

map_img = Image.new('1', (map_width, map_height))

for i in range(sprites_row * sprites_row):
    sprite = generate_random_sprite()

    x = (i % sprites_row) * (sprite_size + spacing) + spacing
    y = (i // sprites_row) * (sprite_size + spacing) + spacing

    map_img.paste(sprite, (x, y))

map_img.save('sprite.png')
img = Image.open('sprite.png')
plt.imshow(img)
plt.show()
