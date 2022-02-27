#For the next feature, we want to find the times during which a user is busy. This feature is intended to show the busy hours of
#a user to other users without revealing the individual meeting slots. Therefore, if any meetings overlap or are back to back,
#then we want to merge their timings. We will be provided with a list of scheduled meetings, ex: [[1, 4], [2, 5], [6, 8], [7.9], [10,13]].
#In this schedule, [1, 4] and [2, 5], as well as [6, 8] and [7, 9], are overlapping. After merging these meetings, the schedule
#becomes [[1, 5], [6, 9], [10, 13]]

#Solution with creating new array

def merge_meetings_new_array(meeting_times):
    sorted_meetings = sorted(meeting_times, key=lambda x: x[0])
    merged = []
    for meeting in sorted_meetings:
        if not merged or merged[-1][1] < meeting[0]:
            merged.append(meeting)
        else:
            merged[-1][1] = max(merged[-1][1], meeting[1])
    return merged

meetings = [[4, 7], [1, 3], [8, 10], [2, 3], [6,8]]
print(merge_meetings_new_array(meetings))

#Solution with merging arrays in place

def merge_meetings_in_place(meeting_times):
    meeting_times = sorted(meeting_times, key=lambda x: x[0])
    idx = 0
    while(idx < len(meeting_times) - 1):
        if meeting_times[idx][1] >= meeting_times[idx + 1][0]:
            meeting_times[idx][1] = max(meeting_times[idx][1], meeting_times[idx + 1][1])
            meeting_times.pop(idx + 1)
        else:
            idx += 1

    return meeting_times

meetings = [[4, 7], [1, 3], [8, 10], [2, 3], [6,8]]
print(merge_meetings_in_place(meetings))