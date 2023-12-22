import pulp


model = pulp.LpProblem("Maximize_the_Profit", pulp.LpMaximize)

A = pulp.LpVariable("A", lowBound=0, cat="Integer")
B = pulp.LpVariable("B", lowBound=0, upBound=10, cat="Integer")

# Цільова функція
model += 50 * A + 40 * B, "Profit"

# Обмеження
model += 5 * A + 2 * B <= 80, "#1"
model += 3 * A + 2 * B <= 40, "#2"

# Розв'язання
model.solve()

# Виведення результатів
print("A =", A.varValue)
print("B =", B.varValue)
print("Profit =", pulp.value(model.objective))
