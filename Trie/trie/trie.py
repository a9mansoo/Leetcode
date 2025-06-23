class Node:

    def __init__(self, letter):
        self._letter = letter
        # The index will tell us what letter it is
        self.children = [None]*26
        self.leaf = False
    
    @property
    def letter(self):
        return self._letter



class Trie:


    def __init__(self):
        self.root = Node("")
    
    def search(self, word):
        prev_node = self.root
        for letter in word:
            int_index = ord(letter) - ord('a')
            curr_child = prev_node.children[int_index]
            if curr_child == None:
                return False
            prev_node = curr_child
        return prev_node.leaf
                

    def insert(self, word):
        prev_node = self.root
        for letter in word:
            int_index = ord(letter) - ord('a')
            curr_child = prev_node.children[int_index]
            if curr_child is None:
                # Add a node
                node = Node(letter)
                prev_node.children[int_index] = node
                prev_node = node
            else:
                prev_node = curr_child
        prev_node.leaf = True

    def startsWith(self, prefix):
        prev_node = self.root
        for letter in prefix:
            int_index = ord(letter) - ord('a')
            curr_node = prev_node.children[int_index]
            if curr_node is None:
                return False
            prev_node = curr_node
        return True
    
    def _search_any_char(self, word, curr_node, index):
        if index == len(word):
            return curr_node.leaf
        char = word[index]
        if char == ".":
            for child in curr_node.children:
                if child is not None:
                    if self._search_any_char(word, child, index+1):
                        return True
            return False
        else:
            int_index = ord(char) - ord('a')
            next_node = curr_node.children[int_index]
            if next_node is None:
                return False
            return self._search_any_char(word, next_node, index+1)
        
    
    def search_any_char(self, word):
        # bed ded mad .ad
        val = self._search_any_char(word, self.root, 0)
        return val

    def print_trie(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.letter:
            end_marker = " *" if node.leaf else ""
            print("  " * level + f"- {node.letter}{end_marker}")
        for child in node.children:
            if child is not None:
                self.print_trie(child, level+1)
        


trie = Trie()
trie.insert("bad")
trie.insert("del")
trie.insert("damp")
trie.insert("mad")
trie.search_any_char(".e.")