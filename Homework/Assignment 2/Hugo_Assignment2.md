---
title: "Assignment 2"
date: 2020-09-06
---

In this assignment, I will solve 3 problems from the Euler Project using Python.

### Problem 13: Large Sum
Work out the first ten digits of the sum of the following one-hundread 50-digit numbers.

- Solved by 225065

- Link: https://projecteuler.net/problem=13

```{python}
nums = """
one-hundred 50-digit numbers
""""

def large_sum(a):
    """Sum 50-digit numbers and return the first ten digits

    Parameters
    ----------
    a : string
        A one-hundred numbers string that is separated by '\n'
        
    Returns
    -------
    int
    		First ten digits of the calculation
    """
    a = a.split("\n")
    total = 0
    for i in range(len(a)):
        if a[i] != '':
            total = total + int(a[i])
    return int(str(total)[:10])
large_sum(nums)
```
Ran the above code with the given data, the returned answer is 5537376230

### Problem 42: Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by  *tn* = ½*n*(*n*+1) ; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

- Solved by: 73178
- Link: https://projecteuler.net/problem=42

```{python}
def triangle_nums(file, nth):
  	"""Read words from the local file,
  		 Calculate the value of each word by adding its corresponding alphabetical positions,
  		 Return the number of triangle words
  		 
  	Parameters
    ---------- 
    file : local file position
  			A '.txt' file that contains English words
  	nth : int
  			An integer that represents the number of triangle number we want, 
  			choose a large number(eg.2000) to cover the entire alphabetic sum
  	
  	Returns
  	-------
  	int
  			The number of triangle words in the file
  	"""
    from numpy import loadtxt
    import string

    # read file
    with open(file, "rt") as in_file:
        with open("out.txt", "wt") as out:
            for line in in_file:
                out.write(line.replace('"', ''))
    words = list(loadtxt("./out.txt", dtype=str, delimiter=",", unpack=False))

    # create triangle numbers
    tri_num = [i * (i+1)/2 for i in range(1, nth)]

    # create alphabetical_num dictionary
    alpha = dict(zip(string.ascii_uppercase, range(1, 27)))

    # calculate the count
    sum = 0
    for word in words:
        word_value = 0
        for i in range(len(word)):
            word_value += int(alpha.get(word[i]))
        if word_value in tri_num:
            sum += 1
    return sum
```

Ran the code with the 'words.txt' file it provided, the function returns answer 162

### Problem 145: How many reversible numbers are there below one-billion?

Some positive integers n have the property that the **sum [ n + reverse(n) ]** consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion?

- Solved by: 15904

- Link: https://projecteuler.net/problem=145

```{python}
def reversible(n):
  	"""Find the reversible number
  	
  	Parameters
    ---------- 
    n : int
    		Number limit, find any target value below this number
  	
  	Returns
    ------- 
  	int
  			The number of reversible numbers that being find
  	"""
    num = 0
    even = ['0','2','4','6','8']
    for i in range(n):
        if str(i)[0] != '0' and str(i)[-1] != '0':
            rev = int(str(i)[::-1])
            sum = i + rev
            inter = set(str(sum)).intersection(set(even))
            if not inter:
                num += 1
    return num
```

Ran the code with one-billion, the function returns the answer 608720. However, it takes around 10 minutes to get that answer. More efficient code rather than the brutal 'for loop' is needed to decrease the operating time.