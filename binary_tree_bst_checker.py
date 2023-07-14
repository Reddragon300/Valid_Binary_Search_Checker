# Write a function to check if a binary tree is a valid binary search tree (BST).

# Define the structure of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Implement the is_valid_bst function


def is_valid_bst(root):

    def is_valid(node, min_val, max_val):
        # Base case: an empty tree or leaf node is a valid BST
        if node is None:
            return True

        # Check if the node's value violates the BST property
        if node.val <= min_val or node.val >= max_val:
            return False

        # Recursively check the left and right subtrees
        return (
            is_valid(node.left, min_val, node.val) and
            is_valid(node.right, node.val, max_val)
        )

    # Call the helper function with initial minimum and maximum values
    return is_valid(root, float('-inf'), float('inf'))

# Test cases


# Test Case 1: A valid BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print("Test Case 1:")
print("Binary Tree:")
print("     4")
print("   /   \\")
print("  2     5")
print(" / \\")
print("1   3")
result = is_valid_bst(root)
print("Output:", result)  # Output: True
print("This binary tree is a valid binary search tree.") if result else print(
    "This binary tree is not a valid binary search tree.")
print()

# Test Case 2: An invalid BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
print("Test Case 2:")
print("Binary Tree:")
print("     4")
print("   /   \\")
print("  2     5")
print(" / \\")
print("1   6")
result = is_valid_bst(root)
print("Output:", result)  # Output: False
print("This binary tree is not a valid binary search tree.") if not result else print(
    "This binary tree is a valid binary search tree.")
print()

# Test Case 3: An empty tree
root = None
print("Test Case 3:")
print("Binary Tree: Empty")
result = is_valid_bst(root)
print("Output:", result)  # Output: True
print("This binary tree is a valid binary search tree.") if result else print(
    "This binary tree is not a valid binary search tree.")
print()

# Test Case 4: A single node (valid BST)
root = TreeNode(5)
print("Test Case 4:")
print("Binary Tree:")
print("    5")
result = is_valid_bst(root)
print("Output:", result)  # Output: True
print("This binary tree is a valid binary search tree.") if result else print(
    "This binary tree is not a valid binary search tree.")
print()

# Test Case 5: A single node (invalid BST)
root = TreeNode(10)
root.left = TreeNode(20)
print("Test Case 5:")
print("Binary Tree:")
print("    10")
print("   /")
print("  20")
result = is_valid_bst(root)
print("Output:", result)  # Output: False
print("This binary tree is not a valid binary search tree.") if not result else print(
    "This binary tree is a valid binary search tree.")
print()

# Test Case 6: A tree with negative values (valid BST)
root = TreeNode(-10)
root.left = TreeNode(-20)
root.right = TreeNode(-5)
root.left.left = TreeNode(-30)
root.left.right = TreeNode(-15)
print("Test Case 6:")
print("Binary Tree:")
print("     -10")
print("   /      \\")
print(" -20     -5")
print(" /     \\")
print("-30   -15")
result = is_valid_bst(root)
print("Output:", result)  # Output: True
print("This binary tree is a valid binary search tree.") if result else print(
    "This binary tree is not a valid binary search tree.")
print()

# Test Case 7: A tree with duplicate values (invalid BST)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)  # Duplicate value
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print("Test Case 7:")
print("Binary Tree:")
print("     5")
print("   /   \\")
print("  3     7")
print(" / \\   / \\")
print("2   3 6   8")
result = is_valid_bst(root)
print("Output:", result)  # Output: False
print("This binary tree is not a valid binary search tree.") if not result else print(
    "This binary tree is a valid binary search tree.")
print()
