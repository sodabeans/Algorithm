class MyHashMap(object):

    def __init__(self):
        self.arr = [None] * (10 ** 6 + 1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.arr[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.arr[key] if self.arr[key] is not None else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)