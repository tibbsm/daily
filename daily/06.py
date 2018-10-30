class Node(object):
    def __init__(self, val = None, both = None):
        self.val = val
        self.both = None

class XOR_List(object):
    def __init__(self, Node = None):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.length = 0

    def add(self, element):
        if length == 0:
            self.head.both = 0 ^ get_pointer(element)
            self.tail.both = get_pointer(element) ^ 0
            element.both = get_pointer(self.head) ^ get_pointer(self.tail)
        else:
            prev = dereference_pointer(self.tail.both)
            prev_prev_addr = prev.both ^ get_pointer(self.tail)
            prev.both = prev_prev_addr ^ get_pointer(element)
            element.both = get_pointer(prev) ^ get_pointer(self.tail.both)
            self.tail.both = get_pointer(element) ^ 0
        length += 1

    def get(self, index):
        if index >= length:
            raise ValueError('Invalid Index!')
        else:
            ptr = self.head.both
            prev_addr = get_pointer(self.head)

            while index > 0:
                node = dereference_pointer(ptr)
                ptr = node.both ^ prev_addr
                prev_addr = ptr
                index -= 1

            if index == 0:
                return dereference_pointer(ptr)


def main():
    pass


if __name__ == '__main__':
    main()
