class Trie:
    def __init__(self):
        self.words = set()
        
    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        return True if word in self.words else False

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if prefix == word[:len(prefix)]:
                return True    
        return False
    
"""
파이썬 클래스는 사실 유사 딕셔너리
c나 java와는 다르게 
class a:
    def __init__(self):
        self.val = 1
이래놓고
test = a()
test.val_2 <= 이런식으로 추가가 가능
객체를 많이 만들면 쓸대없는 딕셔너리가 메모리를 낭비
__slots__ 으로 쓸 변수 정해놓으면 딕셔너리 생성 방지 가능
"""
    
class TrieNode:
    __slots__ = ['isend', 'children']
    def __init__(self):
        self.isend = False
        self.children = {}
    
class Trie_2:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.isend = True
        
    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        return curr_node.isend
        
        
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.word_root
        for c in prefix:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        return True
    
class Trie_3:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node:
                curr_node[c] = {}
            curr_node = curr_node[c]
        curr_node['/'] = None

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c not in curr_node:
                return False
            curr_node = curr_node[c]
        return '/' in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c not in curr_node:
                return False
            curr_node = curr_node[c]
        return True

obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")
print(param_2, param_3)