"=================Циклы==============="
# циклы - это блок кода который повторяется несколько раз
# while
# for - цикл который работает с интерируемыми обьектами, цикл
# заканчивает свою работу, когда дошел до конца (до последного
# элемента) в итерируемом обьете
# while - цикл, который работает до тех пор пока условие верное


# count = 10
# while count != 0:
#     count = count - 1
#     print(count)
# print("end")   # итого вышла 10 9 8 7 6 5 4 3 2 1 end


# a = 0
# while a:
#     print("hello")  # не отработает воопще потому что bool(a) False

# for i in [1,2,3]:
#     print(i)  # 1 2 3


# for i in range(5)
#     print(i)  #   0, 1 2 3 4


# for i in range(1, 10)
#     print(i)   # 1, 2, 3, 4, 5, 6, 7, 8, 9



# for i in '12345'
# print(i)  # '1' '2' '3' '4' '5'

# num = 12345678
# sum = 0
# for i in str(num):
#     # sum = sum + 1
#     # TypeError: unsupported operant type (s) for +: 'int' and 'str'
#     sum = sum +int(i)
#     print(i)  # 36


# string = 'hello'
# for i in string:
#     print(i)  # h e l l o



# string = 'hello'
# string2 = 'world'
#  for i in range(len(string)):
#     print(i, string[i], string[i])
# # 0 h w
# # 1 E O
# # 2 l r
# # 3 l l
# # 4 o d


# for i in []:
#     print(i)  # не работает воопще,потому что нет элементов




# list_ = [1,2,3,]
# for i in list_:
#     print(i)
#     list_.append('hello') # будет работать безконечно

# string = 'hello'
# for i in string:
#     print(i)
#     string = string + "hello"
#     print(string)  #   # отработает только 5 раз, потому что у переменной string ссылка на
#     81 строке ,а у цикла (страка79) нет



# "================Ключевые слова из циклах================="
# break -  полностью выйти из цикла
# continue - перейти к следуещей итерации
  
# for i in range(10):
#    if i == 3:
#        break      #0,1,2
#   print(i)

# for i in range(10):
#    if i == 3:
#       continue
#    print(i)        # 0,1,2,4,5,6,7,8,9   выйдет без 3  


# for i in range(10)
#    if i > 3:
#       continue
#    print(i)  #  3,4,5,6,7,8,9



# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             break
#     if i == 2:
#         break


# list_ = [2,3,4,5,2,4,6,2,2,4,5]
# while 2 in list_:
#     list_.remove(2)
# print(list_)






#  "==========Итерирование словарей============"

dict1 = {"a":1, "b":2, "c":3, "d":4}

# при итерации словаря, мы будем получать его ключи
for key in dict1:
    print(key)
# "a" "b" "c" "d"

# при итерации dict_keys, мы получим его ключи
for key in dict1.keys():
    print(key)
# "a" "b" "c" "d"

# при итерации dict_values, мы будем получать значения словаря
for value in dict1.values():
    print(value)
# 1 2 3 4

for key in dict1:
    print(dict1[key])
    # так мы тоже выведем значения

# при итерации dict_items, мы будем получать tuple из ключа и значения
for items in dict1.items():
    key = items[0]
    value = items[1]
    print(key, value)

# можем распаковать tuple на 2 переменные
for key, value in dict1.items():
    print(key, value)


# for key, value in dict1.keys():
# ValueError: not enough values to unpack (expected 2, got 1)
# потому что метод keys возвращает нам только 1 элемент, а мы распаковываем его на 2 переменные


for a, b, c in [ (1,2,3), (4,5,6), (7,8,9) ]:
    print(a, b, c)
# a=1 b=2 c=3 (iter1)
# a=4 b=5 c=6 (iter2)
# a=7 b=8 c=9 (iter3)

for a, b in [(1,2),(2,3),(3,4)]:
    print(a,b)
# a=1 b=2 (iter1)
# a=2 b=3 (iter2)
# a=3 b=4 (iter3)

a = []
for i in a:
    print("for")
else:
    # сработает только если цикл вообще ни разу не отработал
    print("else")

while 0:
    print("while")
else:
    # не сработает только если цикл был прерван break
    print("else")

a = 1
while a:
    print("while") 
    if a == 1:
        break
else:
    # не сработает только если цикл был прерван break
    print("else")
            