from time import time

# ставить функцию на паузу
# а потом продолжить ее выполнение с места на котором она остановилась

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))
        print('tmp')

#g = gen_filename()



#Round Robin

def gen1(word):
    for i in word:
        yield i

def gen2(number):
    for i in range(number):
        yield i

g1 = gen1('HELLO')
g2 = gen2(5)

tasks = [g1, g2]

# цикл работает пока список содержит в себе хоть какие-то генераторы
while tasks:
    # получение первой задачи, первый работник в очереди
    # перемещие в переменную и удаление из списка
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
