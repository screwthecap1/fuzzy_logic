import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def trapezoidal_mf(x, a, b, c, d):
    if x <= a or x >= d:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)

def fuzzy_complement(x_values, a, b, c, d):
    mu = [trapezoidal_mf(x, a, b, c, d) for x in x_values]
    return mu, [1 - v for v in mu]

a, b, c, d = 50, 65, 90, 100
x_values = np.linspace(0, 100, 101)
mu, mu_compl = fuzzy_complement(x_values, a, b, c, d)

table = pd.DataFrame({
    "Вероятность (%)": x_values,
    "μ(Высокая победа)": mu,
    "μ(НЕ высокая победа)": mu_compl
})
print(table.iloc[::10].round(2).to_string(index=False))

plt.plot(x_values, mu, label="Высокая вероятность победы")
plt.plot(x_values, mu_compl, "--", label="НЕ высокая вероятность")
plt.xlabel("Вероятность победы (%)")
plt.ylabel("Степень принадлежности")
plt.legend()
plt.grid()
plt.show()

user_val = float(input("Введите вероятность победы (%): "))
mu_user = trapezoidal_mf(user_val, a, b, c, d)
print(f"μ(Высокая победа) = {mu_user:.2f}")
print(f"μ(НЕ высокая победа) = {1 - mu_user:.2f}")
