#Facebook is obviously a huge social media platform, and they own a number of other social media platforms, 
#notably instagram. The majority of the problems in this chapter are related to improving connections between 
#all of Facebook’s platforms, because this will allow users to share and view content across FB’s platforms, 
#improving user experience. 

#3 - Find Story ID:
#This feature will allow us to watch or re-watch stories on Instagram that are uploaded through Facebook. 
#Every story uploaded by a user on Facebook gets assigned a unique incrementing id. On Instagram, a user 
#can only watch one story at a time. These stories will be accessed from Facebook in ascending id order. 
#When a story is watched, the story array rotates to accommodate unwatched stories at the start and watched stories at the end. 
#Stories are fetched from Facebook, so whenever a user wants to rewatch a story on Instagram, our 
#system has to search for its id in the Facebook story list.

def find_story_id(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if array[middle] == target:
            return middle

        elif array[left] <= array[middle]:
            if target >= array[left] and target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target <= array[right] and target > array[middle]:
                left = middle + 1
            else:
                right = middle - 1
                
    return -1

print(find_story_id([6, 7, 1, 2, 3, 4, 5], 7))

