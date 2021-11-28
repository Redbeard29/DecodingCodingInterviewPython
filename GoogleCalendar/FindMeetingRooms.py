#1: To develop this project's first feature, we are given a set of meeting times. Our
#job is to implement a solution that can identify the number of meeting rooms needed
#to schedule the required meetings. Each meeting time will contain a start time and
#an end time that are both positive integers. Our list of meeting times looks like
#this: [[2, 8], [3, 4], [3, 9], [8, 20], [5, 11], [11, 15]]. If we schedule each
#meeting in a separate room, that would require six rooms. However, we want to use
#the minimum number of rooms possible. In the example, we can see that the first
#three meetings are overlapping. Therefore, each will require a separate room. However,
#based on the way the meetings do or do not overlap, we can account for all six meetings
#with three rooms

from MinHeap import MinHeap

def get_min_rooms(meeting_times):

    if not meeting_times:
        return 0

    occupied_rooms = MinHeap()
    meeting_times.sort(key = lambda x: x[0])
    occupied_rooms.insert(meeting_times[0][1])

    for meeting in meeting_times[1:]:
        if occupied_rooms.getMin() <= meeting[0]:
            occupied_rooms.removeMin()
        occupied_rooms.insert(meeting[1])

    return len(occupied_rooms.heap)


meeting_times = [[2, 8], [3, 4], [3, 9], [8, 20], [5, 11], [11, 15]]
print(get_min_rooms(meeting_times))