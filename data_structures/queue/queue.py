from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QDialog
from data_structures.node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return item

    def is_empty(self):
        return self.head is None


class QueueGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.queue = Queue()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Queue GUI')
        self.setGeometry(100, 100, 400, 300)

        self.function = QLabel('You can add items from the tail of the queue\n'
                                'and remove the items from the head\n'
                                'To understand better use the following queue\n')
        self.input_label = QLabel('Enter item:')
        self.input_edit = QLineEdit()
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_item)

        self.remove_button = QPushButton('Remove')
        self.remove_button.clicked.connect(self.remove_item)

        self.buscar_button = QPushButton('Buscar')
        self.buscar_button.clicked.connect(self.buscar_elemento)

        self.display_label = QLabel('Queue: ')
        self.display_text = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.function)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_edit)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.buscar_button)
        self.layout.addWidget(self.display_label)
        self.layout.addWidget(self.display_text)

        self.setLayout(self.layout)

    def add_item(self):
        item = self.input_edit.text()
        if item:
            self.queue.push(item)
            self.input_edit.clear()
            self.display_queue()

    def remove_item(self):
        item = self.queue.pop()
        if item:
            QMessageBox.information(self, 'Item Removed', f'In a queue you remove in the head \nRemoved item: {item}')
            self.display_queue()
        else:
            QMessageBox.warning(self, 'Empty Queue', 'Queue is empty')

    def buscar_elemento(self):
        item_a_buscar = self.input_edit.text()
        if item_a_buscar:
            current = self.queue.head
            while current:
                if current.data == item_a_buscar:
                    QMessageBox.information(self, 'Elemento Encontrado', f'El elemento {item_a_buscar} está en la cola.')
                    return
                current = current.next
            QMessageBox.warning(self, 'Elemento No Encontrado', f'El elemento {item_a_buscar} no está en la cola.')
        else:
            QMessageBox.warning(self, 'Campo Vacío', 'Por favor ingrese un elemento para buscar.')

    def display_queue(self):
        current = self.queue.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        queue_str = ', '.join(items)
        self.display_text.setText(queue_str)