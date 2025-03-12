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
      "id": "eb64daef-f681-4d11-9bc9-f1ecefa99ab6",
      "cell_type": "code",
      "source": "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\ntest_list = [64, 34, 25, 12, 22, 11, 90]\n\nprint(\"Original:\", test_list)\nprint(\"sorted:\", bubble_sort(test_list.copy()))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Original: [64, 34, 25, 12, 22, 11, 90]\nsorted: [11, 12, 22, 25, 34, 64, 90]\n"
        }
      ],
      "execution_count": 5
    },
    {
      "id": "452a8f7b-5649-44c2-a5ae-ff64e8e4fd2f",
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