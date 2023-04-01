class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get(self, key):
        index = self._hash(key) % self.size
        slot = self.table[index]
        for k, v in slot:
            if k == key:
                return v
        raise KeyError(key)

    def set(self, key, value):
        index = self._hash(key) % self.size
        slot = self.table[index]
        for i, (k, v) in enumerate(slot):
            if k == key:
                slot[i] = (key, value)
                return
        slot.append((key, value))

    def clear(self):
        self.table.clear()

    # def copy(self):
    #     copy_hash = HashTable(self.size)
    #     for i in range(self.size):
    #

    def items(self):
        items_keys = []
        for el in self.table:
            if len(el) != 0:
                print(el)
                items_keys.append(el[0])

        return items_keys

    def keys(self):
        hash_keys = []
        for el in self.table:
            if len(el) != 0:
                hash_keys.append(el[0][0])

        return hash_keys

    def pop(self, key):
        i = 0
        for el in self.table:
            if len(el) != 0:
                if el[0][0] == key:
                    self.table.pop(i)
            i += 1

    def __len__(self):
        return sum(len(slot) for slot in self.table)

    def _hash(self, key):
        return hash(key)


hash_table = HashTable(12)

hash_table.set("key1", 1)
hash_table.set("key2", 2)
print(hash_table.get("key1"))
print(hash_table.get("key2"))

print(hash_table.items())
print(hash_table.keys())
hash_table.pop("key1")
print(hash_table.table)
