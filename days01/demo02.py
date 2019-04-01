"""

"""
import types

class Stu:
    """
    这是一个学生的类
    """

    def __init__(self, name):
        self.name = name

    # def get_name(self):
    #     return self.__name


g1 = Stu('li')
# print(g.name)

g2 = Stu('wang')


def get_name(self):
    print(self.name)


g2.getn = types.MethodType(get_name, g2)
g2.getn()


@classmethod
def getcls(cls):
    print(cls.__doc__)


Stu.getc = getcls
Stu.getc()


@staticmethod
def pprint():
    print("++++++++++")



Stu.pp = pprint
Stu.pp()

# del Stu.pp
# delattr(Stu, "pp")
Stu.pp()

