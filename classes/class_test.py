from classes.hello import Hello
import functools

class Timer(object):
    def run(self):
        print('Start...')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


def run_twice(animal):
    animal.run()
    animal.run()


class Student(object):
    na = "St"

    def __init__(self, name):
        self.name = name


class Screen(object):
    def __init__(self):
        self.__width = 0
        self.__height = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

h = Hello()
h.hello()
print(type(Hello))


max2 = functools.partial(max, 10)
a = max(1,2,3)
print(a)


# s = Student('Bob')
# s.score = 90
# print(s.score)
# print(Student.na)

# if __name__ == '__main__':
#     d = Dog()
#     d.run()
#     run_twice(Timer())
#     print(dir(d))
#     print()
