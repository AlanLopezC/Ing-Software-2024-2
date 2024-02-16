
###
###
# Exercise 1
###
###

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node: Node):
        if key <= node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def inorder(self) -> list:
        inord = []
        self._inorder(self.root, inord)
        return inord

    def _inorder(self, node: Node, inord: list):
        if node:
            self._inorder(node.left, inord)
            inord.append(node.val)
            self._inorder(node.right, inord)

    def preorder(self) -> list:
        preord = []
        self._preorder(self.root, preord)
        return preord

    def _preorder(self, node: Node, preord: list):
        if node:
            preord.append(node.val)
            self._preorder(node.left, preord)
            self._preorder(node.right, preord)

    def postorder(self) -> list:
        postord = []
        self._postorder(self.root, postord)
        return postord

    def _postorder(self, node: Node, postord: list):
        if node:
            self._postorder(node.left, postord)
            self._postorder(node.right, postord)
            postord.append(node.val)


def testBST():
    print("Testing BST")
    bst = BST()
    print("                 5               ")
    print("             3       7            ")
    print("           2   4   6   8          ")
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    print("Inorder, Preorder, Postorder:")
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())

###
    ###
    # Exercise 2
    ###
###


def count_mountain_valley(s: str) -> tuple:
    sea_level = 0
    mountain = 0
    valley = 0

    for step in s:
        if step == "U":
            sea_level += 1
        else:
            sea_level -= 1

        if step == "U" and sea_level == 0:
            valley += 1
        if step == "D" and sea_level == 0:
            mountain += 1

    return mountain, valley


def valid_caminata(s: str) -> bool:
    """
    Validates that there are only U and D in the string.
    """
    for step in s:
        if step not in ["U", "D"]:
            return False
    return True


def caminata():
    camino = input("Ingrese la caminata: ")
    if not valid_caminata(camino):
        print("Caminata inválida")
        print("Solo se aceptan los caracteres U y D.")
        return
    mountain, valley = count_mountain_valley(camino)

    print(f"Montañas: {mountain}, Valles: {valley}")


# Exercise 1
# testBST()


# Exercise 2
caminata()
