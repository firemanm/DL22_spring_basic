#Дан массив A[0,\ldots,N-1]A[0,…,N−1]. Реализуйте функцию cumsum_and_erase(...), принимающую один обязательный аргумент A
#и один опциональный аргумент erase, по умолчанию равный 1.
#Функция должна выполнять следующие действия: 

#сформировать массив B[0,\ldots, N-1]B[0,…,N−1], где B_i = A_0 + \ldots + A_{i}B 
#удалить из массива BB все элементы, равные параметру eraseerase; получить массив C;
#вернуть C в качестве ответа

def cumsum_and_erase(A, erase=1):
    B = [0] * len(A)
    for i in range(len(A)):
       for j in range(i + 1):
            B[i] = B[i] + A[j]
    for i in range(len(B)-1, -1, -1):
        if B[i] == erase:
            B.pop(i)
    return B


A = [5, 1, 4, 5, 14, 22, 45, 10, 10, 0, 0] 
B = cumsum_and_erase(A, erase=10) 
print(B)
#assert B == [5, 6, 15, 29], "Something is wrong! Please try again"

from itertools import accumulate

def cumsum_and_erase1(a, erase=1):
    return list(filter((erase).__ne__, accumulate(a)))

def cumsum_and_erase(A, erase=1):
    B = []
    summ = 0
    for elem in A:
        summ += elem
        if summ != erase:
            B.append(summ)
    return B

def cumsum_and_erase(A, erase = 1):
    B = list(filter(lambda x: x != erase, map(lambda x: sum(A[:x+1]), range(len(A)))))
    return B


#Дан список текстов, слова в которых разделены пробелами (можно считать, что знаков препинания нет).
#Часть слов является "мусорными": в них присутствуют цифры и спецсимволы. Отфильтруйте такие слова из каждого текста.
#Используйте функции str.split, str.isalpha, str.join, а также list comprehensions.

#Пример ввода:
#['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']

#Пример вывода: 
#['thousand devils', 'My name is', 'Room costs', '']
#Если в тексте все слова являются мусорными, текст должен преобразоваться в пустую строку.    



def process(sentences):
    #result = list(map(lambda x: str.rstrip(str.lstrip(' '.join(list(map(lambda y: (y if y.isalpha() == True else ''), x.split()))))), sentences))
    result = []
    for string in sentences:
        s = string.split()
        result.append(' '.join(x for x in s if x.isalpha() == True)) 
    return result

s = process(['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888'])
print(s)

def process(sentences):
    return [" ".join(filter(lambda x: x.isalpha(), i.split())) for i in sentences]

s = process(['asdfkl%^ sdfk 129&&sd wej sdl 63', 'sdjh 28 jejdj28 381 sdkj euqi**', 'sdq sdf qw 11', 'qwesfd', '11'])
print(s)

