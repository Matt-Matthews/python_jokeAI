from googlesearch import search

class Googlesearch:
    # def __init__(self):
    #     self.query
    def searchQuery(self, query):
        for j in search(query, sleep_interval=5, num=20):
            print(j)