{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "3d0d7f86-ef18-4a03-8a73-fd055e807b68",
      "cell_type": "code",
      "source": "def quick_sort(tab):\n    if len(tab) <= 1:\n        return tab\n    else:\n        pivot = tab[len(tab) // 2]\n        left = [ x for x in tab if x < pivot]\n        middle = [ x for x in tab if x == pivot]\n        right = [ x for x in tab if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n\ntest_list = [43, 1, 23, 3, 11, 23, 45, 55, 80, 100]\n\nprint(\"Original:\", test_list)\nprint(\"Sorted:\", quick_sort(test_list.copy()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'SyntaxError'>",
          "evalue": "closing parenthesis ']' does not match opening parenthesis '(' (<ipython-input-1-343e1329b4b9>, line 5)",
          "traceback": [
            "\u001b[0;36m  Cell \u001b[0;32mIn[1], line 5\u001b[0;36m\u001b[0m\n\u001b[0;31m    pivot = tab[len(tab0 // 2]\u001b[0m\n\u001b[0m                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m closing parenthesis ']' does not match opening parenthesis '('\n"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "7b2e9fc1-b19d-4823-9ccd-40fca4042394",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}