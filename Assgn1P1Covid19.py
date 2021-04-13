{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPAsSkPxWcX8lAMJZmONWAp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/goransh02/Meta-Learning-SOC-2021-IITB/blob/main/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "imjg0AQsNOp3",
        "outputId": "c084a81b-057b-4e81-9230-8774b44cb0ef"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "a1=np.zeros((100, 50))\n",
        "\n",
        "rows = np.arange(100)\n",
        "cols=np.arange(50)\n",
        "r2=np.random.choice(rows,2)\n",
        "c2=np.random.choice(cols,2)\n",
        "a1[r2[0]][c2[0]]=1\n",
        "a1[r2[1]][c2[1]]=1\n",
        "t=0\n",
        "g=[]\n",
        "g1=[]\n",
        "sum=0\n",
        "while sum<5000:  \n",
        "  row=np.random.choice(rows,8)\n",
        "  col=np.random.choice(cols,8)\n",
        "  t1=a1[row[0]][col[0]]\n",
        "  t2=a1[row[1]][col[1]]\n",
        "  t3=a1[row[2]][col[2]]\n",
        "  t4=a1[row[3]][col[3]]\n",
        "  a1[row[0]][col[0]]=a1[row[4]][col[4]]\n",
        "  a1[row[1]][col[1]]=a1[row[5]][col[5]]\n",
        "  a1[row[2]][col[2]]=a1[row[6]][col[6]]\n",
        "  a1[row[3]][col[3]]=a1[row[7]][col[7]]\n",
        "  a1[row[4]][col[4]]=t1\n",
        "  a1[row[5]][col[5]]=t2\n",
        "  a1[row[6]][col[6]]=t3\n",
        "  a1[row[7]][col[7]]=t4\n",
        "  for i in rows:\n",
        "   for j in cols:\n",
        "    if(a1[i][j]==1):\n",
        "      array_1_to_4 = np.arange(start = 1, stop =5)\n",
        "      v=np.random.choice(a = array_1_to_4, p = [.25,.25,.25,.25])\n",
        "      if(v==1):\n",
        "       a1[i][(j-1)%50]=1\n",
        "      if(v==2):\n",
        "       a1[(i-1)%100][j]=1\n",
        "      if(v==3):\n",
        "       a1[i][(j+1)%50]=1\n",
        "      if(v==4):\n",
        "       a1[(i+1)%100][j]=1\n",
        "      t1=0\n",
        "      t2=0\n",
        "      t3=0\n",
        "      t4=0\n",
        "  sum=0\n",
        "    \n",
        "  for i in rows:\n",
        "   for j in cols:\n",
        "    sum=sum+a1[i][j]  \n",
        "  t=t+1\n",
        "  g.append(sum)    \n",
        "  g1.append(t)\n",
        "plt.plot(g1, g)\n",
        "plt.xlabel(\"No of iterations\")\n",
        "plt.ylabel(\"No of cases\")\n",
        "\n",
        "t\n",
        "\n",
        "    \n",
        "\n",
        "     \n",
        "      \n",
        "     \n",
        "     \n",
        "    \n",
        "     \n",
        "    \n",
        "     \n",
        "\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "41"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}