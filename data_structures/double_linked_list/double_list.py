from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QInputDialog
from data_structures.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        if current:
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    def delete_at_beginning(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if not self.head:
            return
        if position <= 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        if not current.next:
            return
        current.next = current.next.next
        if current.next:
            current.next.prev = current

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        display_text = ""
        while current:
            display_text += f"{current.data} <-> "
            current = current.next
        return display_text


class DoublyLinkedListGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doubly Linked List GUI")
        self.layout = QVBoxLayout()

        self.function = QLabel('In a doubly linked list you can insert and remove elements at the beginning, end,\n'
                                'or at a specific position. You can also search for elements in the list.')
        self.input_field = QLineEdit()
        self.insert_beginning_button = QPushButton("Insert at Beginning")
        self.insert_end_button = QPushButton("Insert at End")
        self.insert_position_button = QPushButton("Insert at Position")
        self.delete_beginning_button = QPushButton("Delete at Beginning")
        self.delete_end_button = QPushButton("Delete at End")
        self.delete_position_button = QPushButton("Delete at Position")
        self.search_button = QPushButton("Search")
        self.display_label = QLabel()

        self.doubly_linked_list = DoublyLinkedList()

        self.insert_beginning_button.clicked.connect(self.insert_at_beginning)
        self.insert_end_button.clicked.connect(self.insert_at_end)
        self.insert_position_button.clicked.connect(self.insert_at_position)
        self.delete_beginning_button.clicked.connect(self.delete_at_beginning)
        self.delete_end_button.clicked.connect(self.delete_at_end)
        self.delete_position_button.clicked.connect(self.delete_at_position)
        self.search_button.clicked.connect(self.search_item)

        self.layout.addWidget(self.function)
        self.layout.addWidget(self.input_field)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.insert_beginning_button)
        buttons_layout.addWidget(self.insert_end_button)
        buttons_layout.addWidget(self.insert_position_button)
        buttons_layout.addWidget(self.delete_beginning_button)
        buttons_layout.addWidget(self.delete_end_button)
        buttons_layout.addWidget(self.delete_position_button)
        buttons_layout.addWidget(self.search_button)
        self.layout.addLayout(buttons_layout)
        self.layout.addWidget(self.display_label)

        self.setLayout(self.layout)

    def insert_at_beginning(self):
        item = self.input_field.text()
        if item:
            self.doubly_linked_list.insert_at_beginning(item)
            self.display_list()
        self.input_field.clear()

    def insert_at_end(self):
        item = self.input_field.text()
        if item:
            self.doubly_linked_list.insert_at_end(item)
            self.display_list()
        self.input_field.clear()

    def insert_at_position(self):
        item, ok = QInputDialog.getText(self, "Insert Position", "Enter position:")
        if ok and item:
            position = int(item)
            item, ok = QInputDialog.getText(self, "Insert Element", "Enter element:")
            if ok and item:
                self.doubly_linked_list.insert_at_position(item, position)
                self.display_list()

    def delete_at_beginning(self):
        self.doubly_linked_list.delete_at_beginning()
        self.display_list()

    def delete_at_end(self):
        self.doubly_linked_list.delete_at_end()
        self.display_list()

    def delete_at_position(self):
        item, ok = QInputDialog.getText(self, "Delete Position", "Enter position:")
        if ok and item:
            position = int(item)
            self.doubly_linked_list.delete_at_position(position)
            self.display_list()

    def search_item(self):
        item = self.input_field.text()
        if item:
            if self.doubly_linked_list.search(item):
                QMessageBox.information(self, 'Item Found', f'The item "{item}" is in the list.')
            else:
                QMessageBox.warning(self, 'Item Not Found', f'The item "{item}" is not in the list.')
        self.input_field.clear()

    def display_list(self):
        display_text = self.doubly_linked_list.display()
        self.display_label.setText(display_text)


