#!/usr/bin/python
__author__ = 'Mayank'


# Any class can inherit from multiple classes
# Python generally uses depth first order when searching inheriting classes. eg: class DX
# But when two classes inherit from the same class, python eliminates the first mention of that class from the mro (method resolution order). eg: class D

class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class X(object):
    pass


class DX(B, X):
    pass


class D(B, C):
    pass


print DX.mro()  # DX-B-A-X
print D.mro()  # D-B-C-A
