##The problems in this chapter are all related to content displaying functionality, and how it can be optimized - this is obviously a major goal for a 
#content-streaming service like Netflix. Primarily, we’ll focus on problems related to the search and recommendation functionality.

#8 - Verify User Session:

"""
Netflix has received a user complaint about the Back button we implemented in the previous feature misbehaving. The complaint was 
that the viewing history was not shown in the sequence it was accessed. Being the lead developer of this functionality, you went 
through the logs and retrieved the sequence of push operations and the sequence of pop operations in separate lists. Each new entry that the 
user clicked went to the push operations list. Each time the user clicked the back button, the removed entry went to the pop operations list.
The user also had a session where they browsed for some titles or pressed the Back button several times. The user did not browse the same title more 
than once. At the end of the session, the Back button was disabled. Unfortunately, these logs are separate and there are no timestamps. We want to know if 
the stack handled the user session correctly or if there may be a bug in the stack implementation. We’ll receive two lists of push and pop operations. These 
lists will contain the ID’s of the pages that were browsed. We want to verify whether our implementation of the max stack is behaving correctly or not. 
To do this, we can check if the sequence of push operations and the sequence of pop operations have been interleaved and performed on a valid stack that was initially empty.
"""

def verify_session(push_list, pop_list):

    if len(push_list) != len(pop_list):
        return False
    
    x = 0
    stack = []
    for item in push_list:
        stack.append(item)
        while stack and stack[-1] == pop_list[x]:
            stack.pop()
            x += 1

    if not stack:
        return True
    return False

push_list = [1, 2, 3, 4, 5]
pop_list = [5, 4, 3, 2, 1]

if verify_session(push_list, pop_list):
    print("Functioning properly")
else:
    print("Faulty functionality")