from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QInputDialog
from data_structures.node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_at_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head

    def search(self, key):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def rotate_left(self):
        if self.head:
            self.head = self.head.next

    def rotate_right(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = current

    def display(self):
        display_text = ""
        if self.head:
            current = self.head
            while True:
                display_text += f"{current.data} -> "
                current = current.next
                if current == self.head:
                    break
        return display_text


class CircularLinkedListGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circular Linked List GUI")
        self.layout = QVBoxLayout()

        self.function = QLabel('In a circular linked list, you can insert and delete elements at the beginning and end,\n'
                                'search for elements, and rotate the list left or right.')
        self.input_field = QLineEdit()
        self.insert_beginning_button = QPushButton("Insert at Beginning")
        self.insert_end_button = QPushButton("Insert at End")
        self.delete_beginning_button = QPushButton("Delete at Beginning")
        self.delete_end_button = QPushButton("Delete at End")
        self.search_button = QPushButton("Search")
        self.rotate_left_button = QPushButton("Rotate Left")
        self.rotate_right_button = QPushButton("Rotate Right")
        self.display_label = QLabel()

        self.circular_linked_list = CircularLinkedList()

        self.insert_beginning_button.clicked.connect(self.insert_at_beginning)
        self.insert_end_button.clicked.connect(self.insert_at_end)
        self.delete_beginning_button.clicked.connect(self.delete_at_beginning)
        self.delete_end_button.clicked.connect(self.delete_at_end)
        self.search_button.clicked.connect(self.search_item)
        self.rotate_left_button.clicked.connect(self.rotate_left)
        self.rotate_right_button.clicked.connect(self.rotate_right)

        self.layout.addWidget(self.function)
        self.layout.addWidget(self.input_field)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.insert_beginning_button)
        buttons_layout.addWidget(self.insert_end_button)
        buttons_layout.addWidget(self.delete_beginning_button)
        buttons_layout.addWidget(self.delete_end_button)
        buttons_layout.addWidget(self.search_button)
        buttons_layout.addWidget(self.rotate_left_button)
        buttons_layout.addWidget(self.rotate_right_button)
        self.layout.addLayout(buttons_layout)
        self.layout.addWidget(self.display_label)

        self.setLayout(self.layout)

    def insert_at_beginning(self):
        item = self.input_field.text()
        if item:
            self.circular_linked_list.insert_at_beginning(item)
            self.display_list()
        self.input_field.clear()

    def insert_at_end(self):
        item = self.input_field.text()
        if item:
            self.circular_linked_list.insert_at_end(item)
            self.display_list()
        self.input_field.clear()

    def delete_at_beginning(self):
        self.circular_linked_list.delete_at_beginning()
        self.display_list()

    def delete_at_end(self):
        self.circular_linked_list.delete_at_end()
        self.display_list()

    def search_item(self):
        item = self.input_field.text()
        if item:
            if self.circular_linked_list.search(item):
                QMessageBox.information(self, 'Item Found', f'The item "{item}" is in the list.')
            else:
                QMessageBox.warning(self, 'Item Not Found', f'The item "{item}" is not in the list.')
        self.input_field.clear()

    def rotate_left(self):
        self.circular_linked_list.rotate_left()
        self.display_list()

    def rotate_right(self):
        self.circular_linked_list.rotate_right()
        self.display_list()

    def display_list(self):
        display_text = self.circular_linked_list.display()
        self.display_label.setText(display_text)