


from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton,
    QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

from data_structures.queue import queue
from data_structures.linked_list import linked_list
from data_structures.stack import stack
from data_structures.double_linked_list import double_list
from data_structures.circular_list import circular_list
from data_structures.double_circular_list import double_circular_list
from data_structures.binary_tree import binary_tree
from data_structures.search_binary_tree import search_tree

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.generate_ui()

    def generate_ui(self):
        self.setGeometry(100,100,600,500)
        self.setWindowTitle('Project 2 menu')
        self.generate_window()
        self.show()

    def generate_window(self):
        button1 = QPushButton(self)
        button1.move(110,50)
        button1.setText('Linked list')
        button1.resize(150,70)
        button1.clicked.connect(self.linked_list)
        button2 = QPushButton(self)
        button2.move(350,50)
        button2.setText('Double linked list')
        button2.resize(150,70)
        button2.clicked.connect(self.double_linked_list)
        button3 = QPushButton(self)
        button3.move(110,150)
        button3.resize(150,70)
        button3.setText("Circular list")
        button3.clicked.connect(self.circular_list)
        button4 = QPushButton(self)
        button4.move(350,150)
        button4.resize(150,70)
        button4.setText('Stack')
        button4.clicked.connect(self.stack)
        button5 = QPushButton(self)
        button5.move(110,250)
        button5.setText('Queue')
        button5.resize(150,70)
        button5.clicked.connect(self.queue)
        button6 = QPushButton(self)
        button6.move(350,250)
        button6.setText("Double circular list")
        button6.resize(150,70)
        button6.clicked.connect(self.double_circular_list)
        button7 = QPushButton(self)
        button7.move(110,350)
        button7.setText('Binary tree')
        button7.resize(150,70)
        button7.clicked.connect(self.binary_tree)
        button8 = QPushButton(self)
        button8.move(350,350)
        button8.setText('Search tree')
        button8.resize(150,70)
        button8.clicked.connect(self.search_tree)
    def linked_list(self):
        self.linked_list_view = linked_list.LinkedListGUI()
        self.linked_list_view.show()
    def queue(self):
        self.queue_view = queue.QueueGUI()
        self.queue_view.show()
    def stack(self):
        self.stack_view = stack.StackGUI()
        self.stack_view.show()
    def double_linked_list(self):
        self.double_view = double_list.DoublyLinkedListGUI()
        self.double_view.show()
    def circular_list(self):
        self.circular_view = circular_list.CircularLinkedListGUI()
        self.circular_view.show()
    def double_circular_list(self):
        self.double_circular_view = double_circular_list.CircularDoublyLinkedListGUI()
        self.double_circular_view.show()
    def binary_tree(self):
        self.binary_tree_view = binary_tree.BinaryTreeApp()
        self.binary_tree_view.show()
    def search_tree(self):
        self.search_tree_view = search_tree.SearchTreeGUI()
        self.search_tree_view.show()