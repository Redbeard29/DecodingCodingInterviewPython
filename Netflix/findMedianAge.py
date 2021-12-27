#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#3: Find Median Age:
#Our third task is building a filter that will fetch relevant content based on the age of the users for a specific country or region.
#For this, we use the median age of users and the preferred content for users that fall into that specified category. Because the number
#of users is constantly increasing on the Netflix platform, we need to figure out a structure or design that updates the median age of
#users in real-time. We will have a list that constantly receives age values, and we will output the median value after each new data point.

from heapq import *

class median_ages:
    
    max_heap = []
    min_heap = []

    def insert_age(self, age):
        if not self.max_heap or -self.max_heap[0] >= age:
            heappush(self.max_heap, -age)
        else:
            heappush(self.min_heap, age)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2 + self.min_heap[0] / 2
        else:
            return -self.max_heap[0] / 1


median_age = median_ages()
median_age.insert_age(22)
median_age.insert_age(35)
median_age.insert_age(15)
print("Median age for recommended content: " + str(median_age.find_median()))
median_age.insert_age(20)
median_age.insert_age(55)
median_age.insert_age(30)
median_age.insert_age(25)
print(median_age.max_heap, median_age.min_heap)
print("Median age for recommended content: " + str(median_age.find_median()))