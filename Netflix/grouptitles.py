#The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#1: Group titles - Let the user see relevant search results in spite of minor typos. This requires grouping similar titles
def group_titles(strs):
    results = {}
    for string in strs:
        count = [0] * 26
        for char in string:
            idx = ord(char) - ord('a')
            count[idx] += 1
        key = tuple(count)
        if key in results:
            results[key].append(string)
        else:
            results[key] = [string]
    return results.values()


titles = ["duel","dule","speed","spede","deul","cars"]
grouped_titles = list(group_titles(titles))
query = "spede" 

# Searching for all titles
for group in grouped_titles:
    if query in group:
        print(group)
