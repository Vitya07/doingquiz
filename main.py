#Суть задачи: Получить строку и на выходе пронумеровать ее от 1 до n. (В видe словаря)
# {"a": 1, "b": 2} и так до конца.

z = {}
alfavit = input("Введите строку: ")
perebor_str = [a for a in alfavit]
perebor_len = [i for i in range(1, len(alfavit) + 1)]
for index in range(len(alfavit)):
    c = {perebor_str[index]: perebor_len[index]}
    z.update(c)
print(z)
