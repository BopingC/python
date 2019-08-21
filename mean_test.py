from mean import *
def test():
    list=[3,4,5]
    obs=mean(list)
    exp=4
    assert obs==exp
def test1():
    list=[0,4,5]
    obs=mean(list)
    exp=3
    assert obs==exp

