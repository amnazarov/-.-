class MyMap:
    def __init__(self, method='chain'):  # По умолчанию используется метод цепочек
        self.size = 10  # Размер хэш-таблицы
        self.data = [None] * self.size
        self.method = method  # Метод разрешения коллизий

    def hash_function(self, key):
        return hash(key) % self.size

    def insert_chain(self, key, value):
        idx = self.hash_function(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
        else:
            self.data[idx].append((key, value))

    def insert_open_addressing(self, key, value):
        idx = self.hash_function(key)
        while self.data[idx] is not None:
            idx = (idx + 1) % self.size
        self.data[idx] = (key, value)

    def insert(self, key, value):
        if self.method == 'chain':
            self.insert_chain(key, value)
        elif self.method == 'open':
            self.insert_open_addressing(key, value)

    def get(self, key):
        idx = self.hash_function(key)
        if self.method == 'chain':
            if self.data[idx] is not None:
                for k, v in self.data[idx]:
                    if k == key:
                        return v
        elif self.method == 'open':
            while self.data[idx] is not None:
                k, v = self.data[idx]
                if k == key:
                    return v
                idx = (idx + 1) % self.size
        return None

    def remove(self, key):
        idx = self.hash_function(key)
        if self.method == 'chain':
            if self.data[idx] is not None:
                self.data[idx] = None
        elif self.method == 'open':
            while self.data[idx] is not None:
                k, _ = self.data[idx]
                if k == key:
                    self.data[idx] = None
                    return
                idx = (idx + 1) % self.size

# Пример использования:

map_chain = MyMap(method='chain')
map_chain.insert('key1', 'value1')
map_chain.insert('key2', 'value2')

print(map_chain.get('key1'))  # Вывод: value1

map_open = MyMap(method='open')
map_open.insert('key1', 'value1')
map_open.insert('key2', 'value2')
map_open.insert('key3', 'value3')

print(map_open.get('key2'))  # Вывод: value2
map_open.remove('key3')
print(map_open.get('key3'))