# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    values = None
    
    def __init__(self, root):
        self.values = set()
        root.val = 0

        def recursive(node):
            self.values.add(node.val)
            if node.left:
                node.left.val = 2*node.val + 1
                recursive(node.left)
            if node.right:
                node.right.val = 2*node.val + 2
                recursive(node.right)

        recursive(root)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
