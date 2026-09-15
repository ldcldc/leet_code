from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capa = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict.get(key)
            self.dict.pop(key)
            self.dict[key] = val
            #print(f'get {self.dict}')
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        flag = key in self.dict
        if len(self.dict) == self.capa and not flag:
            self.dict.pop(next(iter(self.dict)))
        elif flag:
            self.dict.pop(key)
        
        self.dict[key] = value
        #print(f'put {self.dict}')


class LRUCache_2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
            
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache_3:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            
            self._remove(lru_node)
            del self.cache[lru_node.key]