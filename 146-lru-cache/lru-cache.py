class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.stack.remove(key)
            self.stack.append(key)

            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value

            self.stack.remove(key)
            self.stack.append(key)
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
                self.stack.append(key)
            else:
                lru_key = self.stack.pop(0)
                del self.cache[lru_key]

                self.cache[key] = value
                self.stack.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)