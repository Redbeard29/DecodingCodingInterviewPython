#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#2: Fetch Top Movies - We currently have a list of top-ranked movies regionally, but we want to merge them into a list of
# top-ranked movies worldwide. Keep in mind that we will be merging more than 2 lists.

from LinkedList import LinkedList

myList = LinkedList()
myList.append("A")
myList.append("B")
myList.append("C")
myList.append("D")

print(myList.head.next.prev)

