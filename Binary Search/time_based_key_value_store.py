# 981. Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.mp={}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((timestamp,value))
        else:
            self.mp[key]=[(timestamp,value)]

    # Time: O(logn)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        search=self.mp[key]
        l,r=0,len(search)-1
        if timestamp<search[l][0]:
            return ""
        while l<=r:
            mid=(l+r)//2
            mid_stamp=search[mid][0]
            if mid_stamp==timestamp:
                return search[mid][1]
            if mid_stamp>timestamp:
                r=mid-1
            elif mid_stamp<timestamp:
                l=mid+1
        return search[min(l,r)][1]
