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
      "id": "367b0578-2da8-4653-8cc9-77bc3c9d53f1",
      "cell_type": "code",
      "source": "import time\nimport random\n\ndef generate_data(size):\n    return [random.randint(1, 1000) for _ in range(size)]\n\n#Example\n\nprint(generate_data(100))\n\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\ntest_list = [64, 34, 25, 12, 22, 11, 90]\n\nprint(\"Original:\", test_list)\nprint(\"sorted:\", bubble_sort(test_list.copy()))\n\n\n\ndef merge_sort(tab):\n    if len(tab) > 1 :\n        mid = len(tab) // 2\n        left = tab[:mid]\n        right = tab[mid:]\n\n        merge_sort(left)\n        merge_sort(right)\n\n        i=j=k=0\n\n        while i < len(left) and j < len(right):\n            if left[i] < right[j]:\n                tab[k] = left[i]\n                i+=1\n            else:\n                tab[k] = right[j]\n                j+=1\n            k+=1\n\n        while i < len(left):\n            tab[k] = left[i]\n            i+=1\n            k+=1\n\n        while j < len(right):\n            tab[k] = right[j]\n            j+=1\n            k+=1\n    return tab\n\ntest_list = [65, 34, 77, 12, 89, 90, 100]\n\nprint(\"Original:\", test_list)\nprint(\"Sorted:\", merge_sort(test_list.copy()))\n\n\ndef quick_sort(tab):\n    if len(tab) <= 1:\n        return tab\n    else:\n        pivot = tab[len(tab) // 2]\n        left = [ x for x in tab if x < pivot]\n        middle = [ x for x in tab if x == pivot]\n        right = [ x for x in tab if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)\n\ntest_list = [43, 1, 23, 3, 11, 23, 45, 55, 80, 100]\n\nprint(\"Original:\", test_list)\nprint(\"Sorted:\", quick_sort(test_list.copy()))\n\n\ndef measure_time(sort_func, data):\n    start = time.time()\n    sort_func(data.copy())\n    end = time.time()\n    return end - start\n\n#Examples\nsizes = [100, 1000, 5000]\nresults = {}\n\nfor size in sizes:\n    data = generate_data(size)\n    results[size] = {\n    \"Bubble Sort\" : measure_time(bubble_sort, data),\n    \"Merge Sort\" : measure_time(merge_sort, data),\n    \"Quick Sort\" : measure_time(quick_sort, data),\n    }\n\nprint(results)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "[254, 579, 963, 140, 912, 370, 8, 824, 266, 432, 861, 335, 48, 263, 166, 801, 397, 279, 2, 340, 715, 143, 232, 709, 448, 890, 37, 549, 624, 94, 922, 611, 895, 216, 546, 878, 57, 289, 222, 837, 849, 651, 985, 899, 567, 309, 887, 473, 69, 364, 780, 871, 208, 495, 381, 943, 81, 395, 517, 136, 871, 298, 552, 790, 750, 203, 404, 419, 394, 899, 857, 994, 467, 541, 212, 238, 170, 854, 488, 278, 508, 646, 853, 193, 485, 203, 921, 833, 440, 297, 216, 895, 991, 870, 451, 553, 992, 811, 648, 189]\nOriginal: [64, 34, 25, 12, 22, 11, 90]\nsorted: [11, 12, 22, 25, 34, 64, 90]\nOriginal: [65, 34, 77, 12, 89, 90, 100]\nSorted: [12, 34, 65, 77, 89, 90, 100]\nOriginal: [43, 1, 23, 3, 11, 23, 45, 55, 80, 100]\nSorted: [1, 3, 11, 23, 23, 43, 45, 55, 80, 100]\n"
        },
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'results' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Cell \u001b[0;32mIn[4], line 92\u001b[0m\n\u001b[1;32m     90\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m size \u001b[38;5;129;01min\u001b[39;00m sizes:\n\u001b[1;32m     91\u001b[0m     data \u001b[38;5;241m=\u001b[39m generate_data(size)\n\u001b[0;32m---> 92\u001b[0m     \u001b[43mresults\u001b[49m[size] \u001b[38;5;241m=\u001b[39m {\n\u001b[1;32m     93\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBubble Sort\u001b[39m\u001b[38;5;124m\"\u001b[39m : measure_time(bubble_sort, data),\n\u001b[1;32m     94\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMerge Sort\u001b[39m\u001b[38;5;124m\"\u001b[39m : measure_time(merge_sort, data),\n\u001b[1;32m     95\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mQuick Sort\u001b[39m\u001b[38;5;124m\"\u001b[39m : measure_time(quick_sort, data),\n\u001b[1;32m     96\u001b[0m     }\n\u001b[1;32m     98\u001b[0m \u001b[38;5;28mprint\u001b[39m(results)\n",
            "\u001b[0;31mNameError\u001b[0m: name 'results' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "a7d05f0f-6fea-42c1-87df-cfe1291bbe9a",
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