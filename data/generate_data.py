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
      "id": "11831648-fa0b-4c82-b7d1-9935c33ce4b3",
      "cell_type": "code",
      "source": "import random\n\ndef generate_data(size):\n    return [random.randint(1, 1000) for _ in range(size)]\n\n#Example\n\nprint(generate_data(100))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "[845, 29, 135, 877, 212, 125, 892, 336, 804, 442, 438, 789, 837, 451, 664, 603, 911, 980, 721, 827, 602, 348, 937, 707, 340, 503, 720, 466, 13, 12, 620, 750, 424, 253, 265, 728, 362, 750, 777, 792, 767, 737, 989, 987, 395, 48, 901, 759, 771, 951, 677, 501, 199, 500, 917, 361, 590, 722, 60, 91, 280, 569, 960, 22, 559, 212, 237, 224, 893, 547, 196, 730, 289, 693, 461, 153, 663, 801, 952, 920, 620, 966, 533, 451, 15, 478, 325, 628, 560, 663, 579, 307, 691, 749, 320, 48, 156, 366, 973, 612]\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "ee0766ec-2544-4ea0-9358-130613e9891f",
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