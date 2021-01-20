class SampleHashTable:

    MIN_CAPACITY = 1

    DEFAULT_TABLE_SIZE = 17
    DEFAULT_HASH_BASE = 31
    PRIMES = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761, 919,
              1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591, 17519, 21023,
              25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437, 187751, 225307, 270371,
              324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263, 1674319, 2009191, 2411033,
              2893249, 3471899, 4166287, 4999559, 5999471, 7199369]

    def __init__(self, table_size: int = DEFAULT_TABLE_SIZE):
        """
        :complexity: O(N) where N is the table_size
        """
        self.count = 0
        self.table = [None] * table_size
        self.next_prime = 0

        while SampleHashTable.PRIMES[self.next_prime] <= table_size:
            self.next_prime += 1

    def __setitem__(self, key, data):

        position = hash(key)

        self.table = (key, data)

    def hash(self, key: str) -> int:
        """
        Universal Hash function
        :post: returns a valid position (0 <= value < table_size)
        :complexity: O(K) where K is the size of the key
        """
        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % len(self.table)
            a = a * SampleHashTable.DEFAULT_HASH_BASE % (len(self.table) - 1)
        return value


a = SampleHashTable(20)

print(a.hash("Aho"))