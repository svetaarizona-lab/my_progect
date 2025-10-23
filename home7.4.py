#Напишіть функцію common_elements, яка згенерує два списки елементів з
# генераторного виразу (range) для 100 елементів, за наступними правилом:
def common_elements ():
    set1 = {i for i in range(100) if i % 3 ==0}
    set2 = {i for i in range (100) if i % 5 ==0}
    return set1 & set2
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print ("OK")
