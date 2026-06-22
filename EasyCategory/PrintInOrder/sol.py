import threading

class Foo(object):
    def __init__(self):
        self.gate_one = threading.Semaphore(0)
        self.gate_two = threading.Semaphore(0)


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        #first in the chain, has the right to release gate one (set to 0 so its already locked)
        self.gate_one.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        #waits on gait one to increment (set to 0, first releases)
        self.gate_one.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        #gate two is now open so third can run
        self.gate_two.release()
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.gate_two.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
