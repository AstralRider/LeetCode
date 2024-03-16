class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
          self.store[key].append([value, timestamp])
        else:
          arr = [value, timestamp]
          self.store[key] = [arr]

    def get(self, key: str, timestamp: int) -> str:
      ans = ""
      temp = self.store.get(key, [])
      L = 0
      R = len(temp) - 1

      while L <= R:
        mid = (L + R) // 2

        if temp[mid][1] > timestamp:
          R = mid - 1
        elif temp[mid][1] <= timestamp:
          ans = temp[mid][0]
          L = mid + 1
      return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)