#!/usr/bin/env python3
class Account(object):
    """账号类，
    amount 是美元金额.
    """
    def __init__(self,rate):
        self._amt = 0
        self.rate = rate

    @property#@property（python内置的装饰器，负责把一个方法变成属性调用）广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
    def amount(self):#返回美元值的方法
        """账号余额(美元)"""
        return self._amt

    @property
    def cny(self):#返回换算后的人民币值的方法
        """账号余额(人民币)"""
        return self._amt * self.rate

    @amount.setter
    def amount(self,value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self._amt = value

if __name__ ==  '__main__':
    acc = Account(rate=6.5231)#变量acc指向的就是一个Account的object，用Account创建了acc实例
    acc.amount = int(input("请输入美元数量"))
    dollor = acc.amount

    if dollor > 0:
       print("Dollar amount:",acc.amount)
       print("In CNY:",acc.cny)

    if dollor < 0:
       print("Dollar amount:",acc.amount)
