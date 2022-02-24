


#Реализуйте класс "Нейрон", у которого будет несколько методов: 
# __init__. Принимает на вход массив весов нейрона --- w = (w_1,..., w_n),
# а также функцию активации ff (аргумент по умолчанию f(x) = x). Сохраняет веса и функцию внутри класса.
# forward. Принимает на вход массив x = (x_1, \ldots, x_n)x=(x1,…,xn) --- входы нейрона.
# Возвращает f(w_1x_1 + ... + w_nx_n).
# backlog. Возвращает массив x, который подавался на вход функции forward при её последнем вызове.
# Если ранее функция forward не вызывалось, возвращает None.

class Neuron:
    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        sum = 0.0
        for i in range(len(x)):
            sum += self.w[i]*self.x[i]
        return self.f(sum)
        
    def backlog(self):
        
        return self.x
        #YOUR CODE 


class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        return self.f(sum(list(map(lambda x, y: x * y, self.x, self.w))))

    def backlog(self):
        return self.x
        
cl = Neuron([1,1])
print(cl.forward([1,2,3,4,5,6]))
print(cl.backlog())