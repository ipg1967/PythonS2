# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму двух чисел: ')) # sum 
p = int(input('Введите произведение двух чисел: ')) # product 
if s > 1000:
    print('нарушены условия задачи')
    exit()

# x = (s-int((s**2-4*p)**0.5))//2 # по теореме Виета 
# y = (s+int((s**2-4*p)**0.5))//2
# print(x, y)

# через цикл

# flag = 0 
# for i in range(s + p):
#     if flag:
#         break
#     for j in range(s + p):
#         if i + j == s and i * j == p:
#             flag = 1
#             print(i,j)
#             break
# if not flag:
#     print('Решений нет')


for i in range(s):
    if (i * (s - i)) == p:
        print(i,(s - i))
        break
else:
    print("Нет решений")
