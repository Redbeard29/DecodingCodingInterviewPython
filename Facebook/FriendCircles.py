#Facebook is a huge social media platform, and they own a number of other social media platforms, 
#notably instagram. The majority of the problems in this chapter are related to improving connections between 
#all of Facebook’s platforms, because this will allow users to share and view content across FB’s platforms, 
#improving user experience. 

#1 - Friend Circles:
#First, we need to find all the people that are in each user’s friends circle on Facebook. Your individual friend circle is defined as a 
#group of users who are directly or indirectly friends with you. Assume there are a total of n users on Facebook. Some of them are your 
#friends and others are not. The friendship/connection is transitive in nature. For example, if Shaw is a direct friend of Andy, and 
#Andy is a direct friend of Noah, then Shaw is an indirect friend of Noah. Getting the total number of friend circles that exist on 
#Facebook helps us suggest connections on Instagram for every user.
#We’ll be provided with an n x n square matrix, where n is the number of users on Facebook. 
#A cell [i,j] will hold the value 1 if user i and user j are friends. Otherwise, the cell will hold the value 0. 

def DFS(friends, size_of_square, visited, person):
    for idx in range(size_of_square):
        if friends[person][idx] and visited[idx] == False:
            if idx != person:
                visited[idx] = True
                DFS(friends, size_of_square, visited, idx)

def find_friend_circles(friends):
    size_of_square = len(friends[0])
    if size_of_square == 0:
        return 0

    friend_circles = 0

    #Keeping track of whether a user is already in a friend circle
    visited = [False for item in friends]
    print(visited)
    
    for person in range(size_of_square):
        if(visited[person] == False):
            visited[person] == True
            DFS(friends, size_of_square, visited, person)
            friend_circles += 1

    return friend_circles


friends = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
]

print(find_friend_circles(friends))