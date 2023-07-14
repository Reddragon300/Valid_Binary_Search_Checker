# Valid Binary Search Tree Checker

This Python program implements a function to check if a binary tree is a valid binary search tree (BST) and solves:

- Write a function to check if a binary tree is a valid binary search tree (BST).


## Binary Tree Structure

The binary tree structure is defined using the `TreeNode` class. Each `TreeNode` instance has a value (`val`) and references to its left and right child nodes (`left` and `right`, respectively).

## Function: is_valid_bst(root)

The `is_valid_bst` function takes the root of a binary tree as input and returns a boolean value indicating whether the tree is a valid BST or not.

The function uses a recursive approach to check the BST property for each node. It employs a helper function `is_valid` that takes three arguments: the current node, the minimum value it can take, and the maximum value it can take. The helper function recursively checks the left and right subtrees, updating the minimum and maximum values accordingly. If any node's value violates the BST property or the recursion reaches a leaf node or an empty tree, the function returns `False`. Otherwise, if the entire tree satisfies the BST property, the function returns `True`.

## Usage

To use this program, follow the steps below:

1. Clone this repository to your local machine using
```Bash
git clone https://github.com/Reddragon300/valid-bst-checker.git
```
3. Navigate to the project directory using
```bash
cd valid-bst-checker
```
5. Open the `binary_tree_bst_checker.py` file in your preferred Python editor or IDE.
6. Scroll down to the test cases section and modify or add your own test cases if desired.
7. Run the Python script.
```bash
$ python binary_tree_bst_checker.py
```
To test the program, several test cases have been included:

1. Test Case 1: A valid BST
2. Test Case 2: An invalid BST
3. Test Case 3: An empty tree
4. Test Case 4: A single node (valid BST)
5. Test Case 5: A single node (invalid BST)
6. Test Case 6: A tree with negative values (valid BST)
7. Test Case 7: A tree with duplicate values (invalid BST)

- The output will be displayed in the console, showing the test case details and the result. Each test case will indicate whether the binary tree is a valid binary search tree or not.
- Feel free to modify the test cases or explore the program further to suit your needs. You can also use this program as a reference or starting point for your own projects.

## Requirments:
- Python 3
Please ensure that you have Python installed on your system before running the program.

This program demonstrates an implementation to check if a binary tree is a valid binary search tree (BST) using Python. It showcases a recursive approach to validate the binary search tree property for each node in the tree.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

If you have any questions or need further assistance, please don't hesitate to reach out.

Happy coding!
