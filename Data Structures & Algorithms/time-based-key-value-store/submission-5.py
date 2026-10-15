class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.hash_map[key]
        # print(data)
        if data and timestamp < data[0][0]:
            return ""
        if not data:
            return ""
        l, r = 0, len(data) - 1
        while l < r:
            mid = (l + r) // 2
            if data[mid][0] < timestamp:
                if data[mid + 1][0] > timestamp:
                    return data[mid][1]
                else:
                    l = mid + 1
            elif data[mid][0] > timestamp:
                r = mid - 1
            else:
                return data[mid][1]
        return data[l][1]
