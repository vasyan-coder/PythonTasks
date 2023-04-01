import numpy as np
import matplotlib.pyplot as plt

# Создаем случайный спрайт размером 5x5 пикселей с использованием свойства симметрии
sprite = np.random.randint(0, 2, size=(5, 5))
print(sprite)
for i in range(3):
    sprite[:, i] = sprite[:, 4-i]
    sprite[i, :] = sprite[4-i, :]

# Выводим спрайт с помощью функции imshow
plt.imshow(sprite, cmap='gray')
plt.show()
