"""
实例方法：第一个参数为self
类方法: 第一个参数为cls, 用@classmethod来声明
静态方法：需要使用@staticmethod声明

类可以调用类方法和静态方法
"""

class Good():
    """
    这是一个商品类
    """

    def __init__(self,name):
        self.name=name

    def names(self):
        return self.name

    @classmethod
    def clss(cls):
        print(cls.__doc__)

    @staticmethod
    def pprint():
        print("静态方法")


g1=Good('tea')
print(g1.names())
g1.clss()
g1.pprint()




