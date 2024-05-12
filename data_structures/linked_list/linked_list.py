import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QInputDialog, QMessageBox
from data_structures.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        display_text = ""
        while temp:
            display_text += f"{temp.data} -> "
            temp = temp.next
        return display_text


class LinkedListGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linked List")
        self.layout = QVBoxLayout()
        
        self.function = QLabel('In a linked list you can add and remove an item by the position\n'
                                'also you can search and insert a element \n'
                                'Using the following linked list app you will be able to understand all the functions on the linked list.')
        self.input_field = QLineEdit()
        self.add_beginning_button = QPushButton("Add at Beginning")
        self.add_end_button = QPushButton("Add at End")
        self.remove_button = QPushButton("Remove")
        self.search_button = QPushButton("Search")
        self.display_label = QLabel()

        self.linked_list = LinkedList()

        self.add_beginning_button.clicked.connect(self.add_at_beginning)
        self.add_end_button.clicked.connect(self.add_at_end)
        self.remove_button.clicked.connect(self.remove_item)
        self.search_button.clicked.connect(self.search_item)

        self.layout.addWidget(self.function)
        self.layout.addWidget(self.input_field)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_beginning_button)
        buttons_layout.addWidget(self.add_end_button)
        buttons_layout.addWidget(self.remove_button)
        buttons_layout.addWidget(self.search_button)
        self.layout.addLayout(buttons_layout)
        self.layout.addWidget(self.display_label)

        self.setLayout(self.layout)

    def add_at_beginning(self):
        item = self.input_field.text()
        if item:
            self.linked_list.insert_at_beginning(item)
            self.display_list()
        self.input_field.clear()

    def add_at_end(self):
        item = self.input_field.text()
        if item:
            self.linked_list.insert_at_end(item)
            self.display_list()
        self.input_field.clear()

    def insert_at_position(self):
        item, ok = QInputDialog.getText(self, "Insert Position", "Enter position:")
        if ok and item:
            position = int(item)
            item, ok = QInputDialog.getText(self, "Insert Element", "Enter element:")
            if ok and item:
                self.linked_list.insert_at_position(item, position)
                self.display_list()
        self.input_field.clear()

    def remove_item(self):
        item = self.input_field.text()
        if item:
            self.linked_list.delete(item)
            self.display_list()
        self.input_field.clear()

    def search_item(self):
        item = self.input_field.text()
        if item:
            if self.linked_list.search(item):
                QMessageBox.information(self, "Item Found", f"The item '{item}' was found.")
            else:
                QMessageBox.warning(self, "Item Not Found", f"The item '{item}' was not found.")
        self.input_field.clear()

    def display_list(self):
        display_text = self.linked_list.display()
        self.display_label.setText(display_text)


if __name__ == '__main__':
    app = QApplication([])
    linked_list_app = LinkedListGUI()
    linked_list_app.show()
    app.exec()
