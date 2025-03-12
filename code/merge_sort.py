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
      "id": "234a1338-6235-4b15-a7f9-473b3ce968d4",
      "cell_type": "code",
      "source": "def merge_sort(tab):\n    if len(tab) > 1 :\n        mid = len(tab) // 2\n        left = tab[:mid]\n        right = tab[mid:]\n\n        merge_sort(left)\n        merge_sort(right)\n\n        i=j=k=0\n\n        while i < len(left) and j < len(right):\n            if left[i] < right[j]:\n                tab[k] = left[i]\n                i+=1\n            else:\n                tab[k] = right[j]\n                j+=1\n            k+=1\n\n        while i < len(left):\n            tab[k] = left[i]\n            i+=1\n            k+=1\n\n        while j < len(right):\n            tab[k] = right[j]\n            j+=1\n            k+=1\n    return tab\n\ntest_list = [65, 34, 77, 12, 89, 90, 100]\n\nprint(\"Original:\", test_list)\nprint(\"Sorted:\", merge_sort(test_list.copy()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Original: [65, 34, 77, 12, 89, 90, 100]\nSorted: [12, 34, 65, 77, 89, 90, 100]\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "03bb2146-0643-4281-a3c6-8367be082546",
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