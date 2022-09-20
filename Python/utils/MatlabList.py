class MatlabList:
    def __init__(self, size = 0):
        self.items = size * [None]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        if idx == 0:
            raise ValueError('Received index = 0 for matlab list')

        return self.items[idx - 1]

    def __setitem__(self, idx, item):
        if idx == 0:
            raise ValueError('Received index = 0 for matlab list')

        self.items[idx - 1] = item

    def append(self, item):
        self.items.append(item)