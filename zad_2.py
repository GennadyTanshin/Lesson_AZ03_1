import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 5  # Количество образцов
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(x_data, y_data, c='blue', alpha=0.5, edgecolors='w', s=50)

# Настройка заголовка и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X данные')
plt.ylabel('Y данные')

# Отображение диаграммы рассеяния
plt.show()