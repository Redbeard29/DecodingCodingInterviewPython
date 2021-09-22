#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#2: Fetch Top Movies - Now, we need to build a criterion so the top movies from multiple countries will combine into a single list of top-rated movies. 
#In order to scale, the content search is performed in a distributed fashion. Search results for each country are produced in separate lists. Each member of a 
#given list is ranked by popularity, with 1 being most popular and popularity decreasing as the rank number increases. We’ll be given n lists that are all sorted 
#in ascending order of popularity rank. We have to combine these lists into a single list that will be sorted by rank in ascending order, meaning from best to worst. 
#Keep in mind that the ranks are unique to individual movies and a single rank can be in multiple lists.

from LinkedList import *

def mergeTwoCountries(headOne, headTwo):
    dummy = Node(-1)

    p1 = headOne
    prev = dummy
    p2 = headTwo

    while p1 and p2:
        if p1.data <= p2.data:
            prev.next = p1
            p1 = p1.next
        else:
            prev.next = p2
            p2 = p2.next
        prev = prev.next
    
    if p1 is not None:
        prev.next = p1
    else:
        prev.next = p2

    return dummy.next

def mergeAllLists(lists):
    if len(lists) > 0:
        result = lists[0]
        for x in range(1, len(lists)):
            result = mergeTwoCountries(result, lists[x])
        return result
    return

myFirstList = LinkedList()
mySecondList = LinkedList()
myThirdList = LinkedList()
myFirstList.create_linked_list([11, 41, 51])
myFirstList.print_list()
mySecondList.create_linked_list([21, 23, 42])
mySecondList.print_list()
myThirdList.create_linked_list([25, 56, 66, 72])
myThirdList.print_list()

mergeAllLists([myFirstList.head, mySecondList.head, myThirdList.head])


myFirstList.print_list()