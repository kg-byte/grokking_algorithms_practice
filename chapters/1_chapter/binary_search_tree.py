from dataclasses import dataclass
from typing import Optional


# 1 without tree class
@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def insert(self, value: int):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        # traverse tree in ascending order
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        # traverse tree and print as it traverses
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        # traverse tree and print at deepest node reached
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        print(self.value)

    def find(self, value: int) -> bool:
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


# 2 with tree class
@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


@dataclass
class BinarySearchTree:
    root: Optional["TreeNode"] = None

    def insert(self, value: int):
        self.root = self._insert(self.root, value)

    def _insert(self, root: Optional[TreeNode], value: int) -> TreeNode:
        if root is None:
            return TreeNode(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        return root

    def search(self, value: int) -> TreeNode | None:
        return self._search(self.root, value)

    def _search(self, root: Optional[TreeNode], value: int) -> TreeNode | None:
        if root is None or root.value == value:
            return root

        if value < root.value:
            return self._search(root.left, value)
        if value > root.value:
            return self._search(root.right, value)

    def inorder_traversal(self) -> None:
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            self._inorder_traversal(root.left)
            print(root.value)
            self._inorder_traversal(root.right)


def main():
    values = [50, 30, 70, 20, 40, 60, 80]
    # nodes without tree
    node = Node(50)
    for value in values[1:]:
        node.insert(value)
    search_result = node.find(40)
    if search_result:
        print(f"Found: {40}")
    else:
        print("Not Found")

    print("Inorder Traversal:")
    node.inorder_traversal()

    print("Preorder Traversal:")
    node.preorder_traversal()

    print("Postorder Traversal:")
    node.postorder_traversal()

    # nodes with tree
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)

    # Search for a value
    search_result = bst.search(40)
    if search_result:
        print(f"Found: {search_result.value}")
    else:
        print("Not Found")

    # Inorder traversal
    print("Inorder Traversal:")
    bst.inorder_traversal()


if __name__ == "__main__":
    main()
