class ReTrie:
    def __init__(self, data):
        self.data = data

    def get_strings(self, node1):
        def get(node, string, strings):
            if node[0]:
                strings.append("".join(string))
            for char in node[1]:
                string.append(char)
                get(node[1][char], string, strings)
                string.pop()
        strings = []
        get(node1, [], strings)
        return strings

    # Autocomplete Functions
    def autocomplete(self, prefix):
        node = self.data
        for char in prefix:
            if char not in node[1]:
                return []
            node = node[1][char]

        return [prefix + string for string in self.get_strings(node)]
