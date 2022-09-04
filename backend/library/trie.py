class Trie:
    def __init__(self, is_end=False, children_data=None):
        if children_data is not None:
            self.is_end = children_data[0]
            self.children = children_data[1]
        else:
            self.is_end = is_end
            self.children = {} 

    def add(self, string):
        node = self
        for char in string:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True

    def addlist(self, wordlist):
        node = self
        for word in wordlist:
            node.add(word)

    def search(self, s):
        node = self
        for char in s:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end else None

    def get_strings(self):
        def get(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for char in node.children:
                string.append(char)
                get(node.children[char], string, strings)
                string.pop()
        strings = []
        get(self, [], strings)
        return strings

    # Autocomplete Functions
    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return [prefix+string for string in node.get_strings()]

    def to_dict(self):
        return [self.is_end, {char: self.children[char].to_dict() for char in self.children}]