class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        item_idx = len(self.data)-1
        parent_idx = item_idx // 2
        if item_idx == 1 :
            pass
        else :
            while not parent_idx == 0 :
                if self.data[item_idx] > self.data[parent_idx] :
                    self.data[item_idx], self.data[parent_idx] = self.data[parent_idx], self.data[item_idx]
                    item_idx = parent_idx
                    parent_idx = item_idx // 2
                else :
                    break
