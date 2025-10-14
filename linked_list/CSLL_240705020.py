class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            curr.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position < 0:
            print("Invalid position!")
            return
        elif position == 0:
            self.insert_at_beginning(data)
            return
        curr = self.head
        count = 0
        while curr.next != self.head and count < position - 1:
            curr = curr.next
            count += 1
        if count == position - 1:
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("Position out of range!")

    def delete(self, data):
        if self.is_empty():
            print("Linked List kosong!")
            return
        curr = self.head
        prev = None
        while True:
            if curr.data == data:
                if prev is not None:
                    prev.next = curr.next
                else:
                    # Menghapus head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    self.head = curr.next
                    temp.next = self.head
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        print("Simpul tidak ditemukan!")

    def display(self):
        if self.is_empty():
            print("Linked List kosong!")
            return
        curr = self.head
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == self.head:
                break
        print()

    def search(self, data):
        if self.is_empty():
            print("Linked List kosong!")
            return False
        curr = self.head
        while True:
            if curr.data == data:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False


# Testing the Circular Linked List
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.insert_at_end(40)

print("Data dalam Circular Linked List setelah proses insert:")
cll.display()

print("Simpul 30 ada dalam list?", cll.search(30))
print("Simpul 100 ada dalam list?", cll.search(100))

cll.delete(30)
cll.delete(20)

print("\nData dalam Circular Linked List setelah delete:")
cll.display()

cll.insert_at_position(50, 1)
print("Data terbaru dalam Circular Linked List setelah insert di posisi ke-1:")
cll.display()
