import matplotlib.pyplot as plt

def plot_full_coordinate_grid():
    # Створення нового рисунка та вісей
    fig, ax = plt.subplots()

    # Визначення меж області рисунка для розташування вісей та координатної сітки
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    # Малювання координатної сітки
    ax.grid(True, which='both')

    # Додавання вісей X та Y
    ax.axhline(y=0, color='green', linewidth=1.0)
    ax.axvline(x=0, color='red', linewidth=1.0)

    # Додавання підписів вісей
    ax.text(20, -1, 'X', fontsize=12, ha='right', va='bottom')
    ax.text(-0.5, 20, 'Y', fontsize=12, ha='right', va='top')

    # Додавання позначення квадрантів
    # ax.text(2, 2, 'I', fontsize=12, ha='center', va='center')
    # ax.text(-2, 2, 'II', fontsize=12, ha='center', va='center')
    # ax.text(-2, -2, 'III', fontsize=12, ha='center', va='center')
    # ax.text(2, -2, 'IV', fontsize=12, ha='center', va='center')

    # Налаштування візуалізації
    ax.set_title('Координатна сітка та вісі')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')

    # Відображення графіку
    plt.show()

# Виклик функції для малювання координатної сітки
plot_full_coordinate_grid()