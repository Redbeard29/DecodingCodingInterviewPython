#Facebook is a huge social media platform, and they own a number of other social media platforms, 
#notably instagram. The majority of the problems in this chapter are related to improving connections between 
#all of Facebook’s platforms, because this will allow users to share and view content across FB’s platforms, 
#improving user experience. 

#4 - Request Limiter:
#The Facebook Status API queues requests using the requested Status ID and a timestamp. We want to implement a throttling mechanism 
#on the requests that limits one request for a particular Status ID at a pre-configured time interval. Any additional requests for the 
#same Status ID in this interval will be dropped. Multiple requests for different Status IDs can occur at the same time.
#We’ll be provided with the name of the request and the time it arrived. Our system will have to decide whether to accept the request 
#or reject it based on its arrival time. In this scenario, we’ll use a time limit of five days before a similar request can be sent 
#from the same or different platform.

class RequestLimiter:
    def __init__(self):
        self.requests = {}

    def request_approver(self, request, timestamp):

        if request not in self.requests or timestamp - self.requests[request] >= 5:
            self.requests[request] = timestamp
            print("request accepted")
            return True
        else:
            print("request denied")
            return False


limiter = RequestLimiter()
limiter.request_approver("send message user 3001", 1)
limiter.request_approver("block user 3000", 1)
limiter.request_approver("block user 3000", 5)


