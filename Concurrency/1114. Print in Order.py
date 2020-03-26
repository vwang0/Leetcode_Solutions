import threading
class Foo:
    def __init__(self):
        self.__cv = threading.Condition()
        self.__has_first = False
        self.__has_secon = False

    def first(self, printFirst): 
        with self.__cv:
            printFirst()
            self.__has_first = True
            self.__cv.notifyAll()

    def second(self, printSecond): 
        with self.__cv:
            while not self.__has_first:
                self.__cv.wait()
            printSecond()
            self.__has_second = True
            self.__cv.notifyAll()

    def third(self, printThird):
        with self.__cv:
            while not self.__has_second:
                self.__cv.wait() 
            printThird()
            self.__cv.notifyAll()            