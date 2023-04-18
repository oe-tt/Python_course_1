# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

a = [1, 2, 3, 4, 5]
b = [] 
k = 3

#1
for i in range(k):
    b.append(a[len(a)-k+i])
for i in range(len(a)-k):
    b.append(a[i])
print(b)

#2
c = a[len(a)-k:] + a[:len(a)-k]
print(c)

#3
d = a
for i in range(k):
    d.insert(0, a.pop(-1))
print(d)