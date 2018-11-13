{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Welcome to the integer multiplication game. How many questions would you like to see? 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting in\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "3 x -2 = -6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "9 x -3 = -27\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "-2 x -3 = 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "-7 x 2 = 14\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Incorrect\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "-1 x -8 = 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "4 x -2 = -8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "8 x -3 = -24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct\n",
      "You got 6 out of 7 correct. It took you 14.602 seconds.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "def mathgames(num):\n",
    "    start = time.time()\n",
    "    right = 0\n",
    "    for i in range(num):\n",
    "        x = random.randint(-10,10)\n",
    "        y = random.randint(-10,10)\n",
    "        answer = x * y\n",
    "        prompt = str(x) + \" x \" + str(y) + \" =\"\n",
    "        inp = input(prompt)\n",
    "        if int(inp) == answer:\n",
    "            print(\"Correct\")\n",
    "            right += 1\n",
    "        else:\n",
    "            print(\"Incorrect\")\n",
    "            continue\n",
    "    print(\"You got\", str(right), \"out of\", str(num), \"correct.\", \"It took you\", round(time.time() - start, 3), \"seconds.\")   \n",
    "\n",
    "test = input(\"Welcome to the integer multiplication game. How many questions would you like to see?\")\n",
    "print(\"Starting in\")\n",
    "for i in [\"3\",\"2\",\"1\"]:\n",
    "    print(i)\n",
    "    time.sleep(1)\n",
    "mathgames(int(test))\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
