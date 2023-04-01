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

    def __len__(self):
        return sum(len(slot) for slot in self.table)

    def _hash(self, key):
        return hash(key)


hash_table = HashTable(12)

hash_table.set("key1", 1)
hash_table.set("key2", 2)
print(hash_table.get("key1"))
print(hash_table.get("key2"))
