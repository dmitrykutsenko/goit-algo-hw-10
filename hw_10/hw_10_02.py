# Integral via Monte-Carlo + використання функції quad з бібліотеки SciPy для обчислення інтеграла
import numpy as np
import scipy.integrate as spi
import random
import matplotlib.pyplot as plt

# Визначення функцію, яку хочемо інтегрувати
def f(x):
    return x ** 2

# Нижня та верхня межі інтегрування
a = 0
b = 2

# Обчислення інтеграла за допомогою методу Монте-Карло
n = 1000000  # Кількість точок
# Генеруємо випадкові значення x та y
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

# Обчислюємо кількість точок в сірій зоні (які потрапили під криву)
points_under_curve = sum(y_rand <= f(x_rand))

# Обчислюємо відношення площі під кривою до загальної площі
integral_mc = points_under_curve / n * (b - a) * f(b)

# Обчислення інтеграла за допомогою функції quad з бібліотеки SciPy
integral_scipy, error = spi.quad(f, a, b)

print("Значення інтеграла за методом Монте-Карло:   ", integral_mc)
print("Значення інтеграла за допомогою функції quad:", integral_scipy)

# Візуалізація
# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
# Створення графіка
fig, ax = plt.subplots()
# Малювання функції
ax.plot(x, y, 'r', linewidth=2)
# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()