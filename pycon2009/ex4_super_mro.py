class A(object):
    def __init__(self):
        print "A init"
        print self.__class__.__mro__

class B(A):
    def __init__(self):
        print "B init"
        print self.__class__.__mro__
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print "C init"
        print self.__class__.__mro__
        super(C, self).__init__()

class D(B, C):
    def __init__(self):
        print "D init"
        print self.__class__.__mro__
        super(D, self).__init__()

x = D()
