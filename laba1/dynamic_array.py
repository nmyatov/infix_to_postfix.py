class DynamicArray:

    def __init__(self):
        self.elements = 0 # count the actual number of elements
        self.capacity = 1 # default capacity is set as 1
        self.dynamic_array = self.make_dynamic_array(self.capacity) #  array with the given capacity

    @staticmethod
    def make_dynamic_array(new_cap: int) -> list: # Make an array
        return [None] * new_cap

    def __len__(self) -> int: # Returns the number of elements stored in the array
        return self.elements

    def __getitem__(self, item): # Return the element at position k
        if  not 0 <= item < self.elements:
            return 'Index error'
        return self.dynamic_array[item]

    def append(self, elem): # Add the element at the end of the array
        if self.dynamic_array[0] is None: # Create first element in a dynamic array
            self.dynamic_array[0] = elem
            self.elements += 1
            return elem
        elif self.elements == self.capacity:
            self.dynamic_array = self._resize(2 * self.capacity)

        self.dynamic_array[self.elements] = elem
        self.elements += 1
        return elem

    def pop(self):
        if self.elements == 1:
            self.elements -= 1
            self.dynamic_array[0] = None
            return None

        elif self.elements > 1:
            last_elem = self.dynamic_array[-1]
            copy_ = last_elem
            self.elements -= 1
            self.capacity -= 1
            del self.dynamic_array[-1]
            return copy_
        else:
            return None

    def insertAt(self, index, data):
        if not  0 <= index <= self.elements:
            return 'Index error'
        if index == self.elements:
            self.dynamic_array = self._resize(self.capacity + 1)
            self.capacity += 1
            self.elements += 1

        self.dynamic_array[index] = data
        return data

    def print_array(self) -> str: # print array
        if self.elements == 0:
            return 'Empty arr'
        our_print = ""
        for elem in self.dynamic_array:
            our_print += f"{elem} "
        return our_print

    def _resize(self, new_cap):
        copy_of_array = self.make_dynamic_array(new_cap)
        for i in range(self.elements):
            copy_of_array[i] = self.dynamic_array[i]
        self.capacity = new_cap
        return copy_of_array


if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(20)
    arr.append(30)
    arr.pop()
    arr.pop()
    arr.append(10)
    arr.pop()
    # print(arr.__len__())
    # print(arr.print_array())
    arr.append(20)
    arr.append(30)
    arr.pop()
    arr.pop()
    arr.append(100)
    arr.append(20)
    arr.insertAt(0, 30)
    arr.insertAt(2, 60)
    arr.pop()
    arr.pop()
    arr.pop()
    arr.pop()
    arr.append(20)
    print(arr.__len__())
    print(arr.print_array())
