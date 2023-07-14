# Valid Binary Search Tree Checker

This Python program implements a function to check if a binary tree is a valid binary search tree (BST) and solves:

- Write a function to check if a binary tree is a valid binary search tree (BST).


## Binary Tree Structure

The binary tree structure is defined using the `TreeNode` class. Each `TreeNode` instance has a value (`val`) and references to its left and right child nodes (`left` and `right`, respectively).

## Function: is_valid_bst(root)

The `is_valid_bst` function takes the root of a binary tree as input and returns a boolean value indicating whether the tree is a valid BST or not.

The function uses a recursive approach to check the BST property for each node. It employs a helper function `is_valid` that takes three arguments: the current node, the minimum value it can take, and the maximum value it can take. The helper function recursively checks the left and right subtrees, updating the minimum and maximum values accordingly. If any node's value violates the BST property or the recursion reaches a leaf node or an empty tree, the function returns `False`. Otherwise, if the entire tree satisfies the BST property, the function returns `True`.

## Usage

To test the program, several test cases have been included:

1. Test Case 1: A valid BST
2. Test Case 2: An invalid BST
3. Test Case 3: An empty tree
4. Test Case 4: A single node (valid BST)
5. Test Case 5: A single node (invalid BST)
6. Test Case 6: A tree with negative values (valid BST)
7. Test Case 7: A tree with duplicate values (invalid BST)

Each test case creates a binary tree with specific values and structure. The `is_valid_bst` function is then called on each tree, and the result is printed along with a description of whether the binary tree is a valid binary search tree or not.

Feel free to modify the test cases or add your own to further explore the functionality of the program.

## Running the Program

To run the program, you can simply execute the Python script. Ensure that you have Python installed on your system. The output will be displayed in the console, showing the test case details and the result.

```bash
$ python binary_tree_bst_checker.py
```
Please note that the program uses Python 3 syntax.

This program demonstrates an implementation to check if a binary tree is a valid binary search tree (BST) using Python. It showcases a recursive approach to validate the binary search tree property for each node in the tree.

Feel free to use this program as a reference or starting point for your own projects.

If you have any questions or suggestions, please feel free to reach out.

Happy coding!
