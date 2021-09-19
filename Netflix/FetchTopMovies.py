#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#2: Fetch Top Movies - Now, we need to build a criterion so the top movies from multiple countries will combine into a single list of top-rated movies. 
#In order to scale, the content search is performed in a distributed fashion. Search results for each country are produced in separate lists. Each member of a 
#given list is ranked by popularity, with 1 being most popular and popularity decreasing as the rank number increases. We’ll be given n lists that are all sorted 
#in ascending order of popularity rank. We have to combine these lists into a single list that will be sorted by rank in ascending order, meaning from best to worst. 
#Keep in mind that the ranks are unique to individual movies and a single rank can be in multiple lists..

from LinkedList import *

def merge_two_countries(headOne, headTwo):
    p1 = headOne
    p1Prev = Node(None)
    p2 = headTwo

    while p1 and p2:
        if p1.data < p2.data:
            p1Prev.next = p1
            p1 = p1.next
        else:
            if p1Prev:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    
    if p1 is None:
        p1Prev.next = p2

    return headOne if headOne.data < headTwo.data else headTwo

myFirstList = LinkedList()
mySecondList = LinkedList()
myThirdList = LinkedList()
myFirstList.create_linked_list([11, 41, 51])
myFirstList.print_list()
mySecondList.create_linked_list([21, 23, 42])
mySecondList.print_list()
myThirdList.create_linked_list([25, 56, 66, 72])
myThirdList.print_list()

print(merge_two_countries(myFirstList.head, mySecondList.head))