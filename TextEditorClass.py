
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("Invalid index")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.tail is None:
                self.tail = new_node

        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node

            if new_node.next is None:
                self.tail = new_node

        self._size += 1

    def delete_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Invalid index")

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next

            if self.head is None:
                self.tail = None

        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            deleted_node = current.next
            current.next = deleted_node.next

            if current.next is None:
                self.tail = current

        self._size -= 1
        return deleted_node.data

    def __iter__(self):
        current = self.head

        while current:
            yield current.data
            current = current.next


class TextEditor:
    def __init__(self):
        self.lines = SinglyLinkedList()
        self.undo_stack = []
        self.redo_stack = []

    def add_line(self, text):
        index = self.lines._size

        self.lines.append(text)

        self.undo_stack.append(("insert", index, text))
        self.redo_stack.clear()

    def insert_line(self, index, text):
        self.lines.insert_at(index, text)

        self.undo_stack.append(("insert", index, text))
        self.redo_stack.clear()

    def delete_line(self, index):
        deleted_text = self.lines.delete_at(index)

        self.undo_stack.append(("delete", index, deleted_text))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return

        action, index, text = self.undo_stack.pop()

        if action == "insert":
            self.lines.delete_at(index)
            self.redo_stack.append((action, index, text))

        elif action == "delete":
            self.lines.insert_at(index, text)
            self.redo_stack.append((action, index, text))

    def redo(self):
        if not self.redo_stack:
            return

        action, index, text = self.redo_stack.pop()

        if action == "insert":
            self.lines.insert_at(index, text)

        elif action == "delete":
            self.lines.delete_at(index)

        self.undo_stack.append((action, index, text))

    def show(self):
        for index, line in enumerate(self.lines, start=1):
            print(f"{index}: {line}")


# aq vtestav kods

ed = TextEditor()

ed.add_line("A")
ed.add_line("B")
ed.add_line("C")

ed.delete_line(1)

ed.undo()
ed.undo()
ed.redo()

ed.add_line("D")

ed.redo()

ed.show()
