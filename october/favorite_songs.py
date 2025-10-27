"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-23
                                    Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).

"""

def favorite_songs(playlist):
    #solution1: using sort() O(nlogn)
    # playlist.sort(key = lambda x: x['plays'], reverse= True)
    # output = []
    # for i in range(2):
    #     output.append(playlist[i]['title'])

    # return output

    #solution 2: using heap, maintain a min heap with 2 items, when adding a new item to the head the minimum one
    # will be popped first. The heap only maintain top 2 most played songs
    # O(2logn) = O(log(n))

    # import heapq

    # heap = []


    # for song in playlist:
    #     heapq.heappush(heap, (song['plays'], song['title']))
    #     if len(heap) >2:
    #         heapq.heappop(heap)
    # res = []

    # for _ in range(len(heap)):
    #     res.append(heapq.heappop(heap)[1])
    # #res.reverse()
    # return list(reversed(res))

    #Solution3
    #Linear Scan 
    top1 = top2 = None

    for song in playlist:
        if top1 is None or song['plays'] > top1['plays']:
            top2 = top1
            top1 = song
        elif top2 is None or song['plays'] > top2['plays']:
            top2 = song
    res = []
    if top1:
        res.append(top1['title'])
    if top2:
        res.append(top2['title']) 
    return res
print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]) )
#should return ["Sync or Swim", "Earbud Blues"].