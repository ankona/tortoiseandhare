class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None


class LinkedList:
    def __init__(self):
        self._head = None

    def traverse(self):
        n  = self._head
        p = self._head

        while n is not None:
            if n.nxt is None:
                p = n
            n = n.nxt

        return p

    def __iter__(self):
        n = self._head

        while n is not None:
            yield n
            n = n.nxt

    def add(self, node):
        if self._head is not None:
            tail = self.traverse()
            tail.nxt = node
        else:
            self._head = node

    def has_cycle(self):
        # use tortoise & hare technique.
        tortoise = self._head
        hare = self._head

        cycle = False

        while tortoise is not None and hare is not None and not cycle:
            # tortoise moves by one every time.
            tortoise = tortoise.nxt

            # hare moves by two every time (unless we reach the end).
            hare = hare.nxt
            if hare is not None:
                hare = hare.nxt

            # since we move consistent amounts, the only way for t == h is
            # to have a loop and the hare catches up to the tortoise.
            if tortoise == hare:
                cycle = True

        return cycle


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)

    ll = LinkedList()
    ll.add(n1)
    ll.add(n2)
    ll.add(n3)
    ll.add(n4)
    ll.add(n5)
    ll.add(n6)
    ll.add(n7)
    ll.add(n8)
    # ll.add(n3)

    # print(f'last node value: {ll.traverse().value}')

    has_cycle = ll.has_cycle()

    print(f'Cycle found: {has_cycle}')

    if not has_cycle:
        for n in ll:
            print(f'node.value: {n.value}')


