from MaxHeap import *
from MinHeap import *

class MedianAges():

    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def insert_age(self, age):
        if self.max_heap.getMax() == None or self.max_heap.getMax() >= age:
            self.max_heap.insert(age)
        else:
            self.min_heap.insert(age)

        if len(self.max_heap.heap) > len(self.min_heap.heap) + 1:
            self.min_heap.insert(self.max_heap.removeMax())
        elif len(self.min_heap.heap) > len(self.max_heap.heap):
            self.max_heap.insert(self.min_heap.removeMin())

    def find_median(self):
        if len(self.max_heap.heap) == len(self.min_heap.heap):
            return (self.max_heap.getMax() + self.min_heap.getMin()) / 2
        else:
            return self.max_heap.getMax()

        
median_age = MedianAges()
median_age.insert_age(22)
median_age.insert_age(35)
median_age.insert_age(15)
print("Median age for recommended content: " + str(median_age.find_median()))
median_age.insert_age(20)
median_age.insert_age(55)
median_age.insert_age(30)
print("Median age for recommended content: " + str(median_age.find_median()))
    