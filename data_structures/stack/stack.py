from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from data_structures.node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.data if self.top else None

    def search(self, key):
        current = self.top
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        stack_str = ' -> '.join(items[::-1])
        return stack_str


class StackGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stack GUI")
        self.layout = QVBoxLayout()

        self.function = QLabel('In a stack you can add, remove and search for an item.\n'
                               'Using the following stack app, you will be able to perform these operations.')
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Push")
        self.pop_button = QPushButton("Pop")
        self.search_button = QPushButton("Search")
        self.display_label = QLabel()

        self.stack = Stack()

        self.add_button.clicked.connect(self.push_item)
        self.pop_button.clicked.connect(self.pop_item)
        self.search_button.clicked.connect(self.search_item)

        self.layout.addWidget(self.function)
        self.layout.addWidget(self.input_field)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.pop_button)
        buttons_layout.addWidget(self.search_button)
        self.layout.addLayout(buttons_layout)
        self.layout.addWidget(self.display_label)

        self.setLayout(self.layout)

    def push_item(self):
        item = self.input_field.text()
        if item:
            self.stack.push(item)
            self.display_stack()
        self.input_field.clear()

    def pop_item(self):
        item = self.stack.pop()
        if item:
            QMessageBox.information(self, 'Item Popped', f'Popped item: {item}')
            self.display_stack()
        else:
            QMessageBox.warning(self, 'Empty Stack', 'Stack is empty')

    def search_item(self):
        item = self.input_field.text()
        if item:
            if self.stack.search(item):
                QMessageBox.information(self, 'Item Found', f'The item "{item}" is in the stack.')
            else:
                QMessageBox.warning(self, 'Item Not Found', f'The item "{item}" is not in the stack.')
        self.input_field.clear()

    def display_stack(self):
        stack_str = self.stack.display()
        self.display_label.setText(stack_str)
