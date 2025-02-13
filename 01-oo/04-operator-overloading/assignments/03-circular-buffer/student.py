class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.elements = []


    def add(self, element):
        if self.__len__() < self.size:
            self.elements.append(element)
        else:
            self.elements.pop(0)
            self.elements.append(element)
    
    def __len__(self):
        return len(self.elements)
    

    def __getitem__(self, index):
        return self.elements[index]
    


# 1 4 9 2 5
# add 0
# 4 9 2 5 0


buffer = CircularBuffer(5)
buffer.add(1)
buffer.add(4)
buffer.add(9)
buffer.add(2)
buffer.add(5)

print(buffer.elements)

buffer.add(0)

print(buffer.elements)