from Node import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print List
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Create new node and add to end
    def append(self, value):
        node = Node(value)
        # If the linked list is empty:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    # Create new node and add to beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Create new node and insert where needed
    def insert(self, index, value):
        pass

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Popping last node and return it
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    # Popping the first node and return it
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp

    # get method to check a node with specified index in the linked list
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # set value at a specific place in the linked list
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # Insert a specific value at a specific index
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif index < 0 or index > self.length:
            return False
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    # Removing at a specific place:

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    # Reverse Link List
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Find Middle Node
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.value

    # Check if linked list has cycle

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def reverse_between(self, m, n):
        if self.length == 0 or self.length == 1:
            return
        dummy = Node(0)

        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next
        current = prev.next
        for _ in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next

