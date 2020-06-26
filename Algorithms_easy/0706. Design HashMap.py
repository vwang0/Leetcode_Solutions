class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data = [None] * 1000000
        

    def put(self, key: int, value: int) :
        """
        value will always be non-negative.
        """
        self.data[key] = value

    def get(self, key: int) :
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.data[key] is None:
            return -1
        else:
            return self.data[key]
        
        

    def remove(self, key: int) :
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.data[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)