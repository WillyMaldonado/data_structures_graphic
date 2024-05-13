from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt6.QtGui import QColor
from data_structures.binary_tree.binary_node import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            node.data = self._min_value_node(node.right)

            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, node.data)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.data)
            self._inorder_traversal_recursive(node.right, result)


class BinaryTreeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binary Tree")
        self.setGeometry(100, 100, 800, 600)

        self.tree = BinaryTree()

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.insert_input = QLineEdit()
        self.search_input = QLineEdit()
        self.delete_input = QLineEdit()

        self.insert_button = QPushButton("Insert")
        self.search_button = QPushButton("Search")
        self.delete_button = QPushButton("Delete")

        self.TreeUI()

    def TreeUI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()


        insert_layout = QHBoxLayout()
        insert_layout.addWidget(QLabel("Insert value:"))
        insert_layout.addWidget(self.insert_input)
        insert_layout.addWidget(self.insert_button)


        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search value:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)


        delete_layout = QHBoxLayout()
        delete_layout.addWidget(QLabel("Delete value:"))
        delete_layout.addWidget(self.delete_input)
        delete_layout.addWidget(self.delete_button)

        main_layout.addWidget(self.view)
        main_layout.addLayout(insert_layout)
        main_layout.addLayout(search_layout)
        main_layout.addLayout(delete_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.insert_button.clicked.connect(self.insert_node)
        self.search_button.clicked.connect(self.search_node)
        self.delete_button.clicked.connect(self.delete_node)

    def redraw_tree(self):
        self.scene.clear()
        self.draw_tree_recursive(self.tree.root, 400, 50, 300)

    def draw_tree_recursive(self, node, x, y, offset):
        if node:
            green_color = QColor('#228B22')

            circle = self.scene.addEllipse(x, y, 30, 30)
            circle.setBrush(green_color)



            text_item = self.scene.addText(str(node.data))
            text_item.setPos(x + 5, y + 5)

            if node.left:
                line = self.scene.addLine(x + 15, y + 30, x - offset + 15, y + 100)
                self.draw_tree_recursive(node.left, x - offset, y + 100, offset / 2)

            if node.right:
                line = self.scene.addLine(x + 15, y + 30, x + offset + 15, y + 100)
                self.draw_tree_recursive(node.right, x + offset, y + 100, offset / 2)

    def insert_node(self):
        try:
            value = int(self.insert_input.text())
            self.tree.insert(value)
            self.redraw_tree()
            self.insert_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Value not valid", "Insert a integer number.")

    def search_node(self):
        try:
            value = int(self.search_input.text())
            if self.tree.search(value):
                QMessageBox.information(self, "Search successfully", f"The value {value} is on the tree.")
            else:
                QMessageBox.warning(self, "Search failed", f"The value {value} is not on the tree.")
            self.search_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Value not valid", "Please insert a integer number.")

    def delete_node(self):
        try:
            value = int(self.delete_input.text())
            self.tree.delete(value)
            self.redraw_tree()
            self.delete_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Not valid value", "Please insert an integer number.")
