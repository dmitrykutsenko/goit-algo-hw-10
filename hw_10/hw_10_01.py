# Monte-Carlo

from pulp import *

# Створення задачі ЛП
prob = LpProblem("Maximize_Production", LpMaximize)

# Змінні
x_l = LpVariable("Lemonade_units", 0, None, LpInteger)
x_f = LpVariable("Fruit_juice_units", 0, None, LpInteger)

# Цільова функція максимізації
def maximize_production():
    return x_l + x_f, "Total_production"

# Цільова функція максимізації
prob += maximize_production()

# Додаємо обмеження ресурсів
prob += 2 * x_l + x_f <= 100, "Water_constraint"
prob += x_l <= 50, "Sugar_constraint"
prob += x_l <= 30, "Lemon_juice_constraint"
prob += 2 * x_f <= 40, "Fruit_puree_constraint"

# Вирішення задачі
prob.solve()

# Виводимо результати
print("Status:", prob.status)
print("Максимальна загальна кількість продуктів:", round(prob.objective.value(), 2))
print("Кількість Лимонаду:", x_l.value())
print("Кількість Фруктового соку:", x_f.value())

