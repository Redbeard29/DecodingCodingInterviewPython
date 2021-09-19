#Popularity Analysis:

#Netflix maintains a popularity score for each of its titles. This popularity score is derived from customer feedback, likes, dislikes, etc. This score is updated weekly and added to the end of the list containing previous scores for the same title. 
#This score list helps Netflix identify titles that may be increasing or decreasing in popularity over time. Some titles may be steady in popularity, increasing, decreasing, and fluctuating. We want to identify and separate a title if it is gaining or losing popularity.
#We’ll be provided with a list of integers representing the popularity scores of a movie collected over a number of weeks. We need to identify only those titles that are either increasing or decreasing in popularity, so we can separate them from the fluctuating ones for better analysis.
#A list is increasing if the expression list[i] <= list[i + 1] evaluates to true for every element at index i. Similarly, a list is decreasing if the expression list[i] >= list[i + 1] evaluates to true for every element at index i.

def identify_titles(scores):

    increasing = decreasing = True

    for idx in range(len(scores) - 1):
        if scores[idx] < scores[idx + 1]:
            decreasing = False
        if scores[idx] > scores[idx + 1]:
            increasing = False
        
    return increasing or decreasing

movie_ratings = [
    [1,2,2,3],
    [4,5,6,3,4],
    [8,8,7,6,5,4,4,1]
]

for movie in movie_ratings:
    if identify_titles(movie):
        print("Strictly increasing or decreasing")
    else:
        print("Title is fluctuating")