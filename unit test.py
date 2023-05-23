# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:04:04 2022

@author: Ahmed Kheiri
"""

class UnitTest():
    def __init__(self, name="UnnamedTest"):
        self.name = name
    def getName(self):
        return self.name
    def execute(self):
        pass

class ApplicationTest():
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def runAll(self):
        for test in self.tests:
            print("- Executing test:", test.getName())
            test.execute()
def A(x,y):
    return x+y
def B(x,y):
    return x-y
def C(x,y):
    return A(x,y) + B(x,y)

class TestA(UnitTest):
    def execute(self):
        print("Test A(7,2)",A(7,2), A(7,2) == 9)
class TestB(UnitTest):
    def execute(self):
        print("Test B(7,2)",B(7,2), B(7,2) == 5)
class TestC(UnitTest):
    def execute(self):
        print("Test C(7,2)",C(7,2), C(7,2) == 14)

test = ApplicationTest()
test.add(TestA("A"))
test.add(TestB("B"))
test.add(TestC("C"))
test.runAll()

# Different approach - The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True
# If not, the program will raise an AssertionError.
#assert A(7,2) == 6
# You can write a message to be written if the code returns False
#assert A(7,2) == 6, "should be 9!"

