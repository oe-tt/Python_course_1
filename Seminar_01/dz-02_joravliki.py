# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

num = int(input("Введите количество журавликов >> "))
while num % 6 != 0:
    print("Не годится. Число должно быть кратно шести.")
    num = int(input("Введите количество журавликов >> "))
print(f"Петя сделал {num // 6}, Катя сделала {num // 6 * 4}, Сережа сделал {num // 6} журавликов.")