#Написати програму, яка переміщає всі нулі у кінець списку.
#Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
#Порядок ненульових чисел має зберегтися!
example = [0, 1, 0, 12, 3]
count_z = example.count(0)
for _ in range(count_z):
    example.remove(0)
    example.append(0)
print("Result:" , example)

