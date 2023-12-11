# Aditi Saraswat - Impledge Placement Assignment

## Introduction

Hello! I'm Aditi Saraswat, a dedicated and passionate individual seeking placement at Impledge. This README provides an overview of the Python solution for a specific assignment. 

## Solution Overview

The provided Python solution (`try.py`) is designed to read two input files (`Input_01.txt` and `Input_02.txt`). It identifies and displays the longest and second longest compounded words based on specific criteria. The approach involves recursively checking if a word is compounded by breaking it into smaller words without any additional characters in between.

## How to Run the Solution

Follow these steps to run the Python file `try.py` along with the provided input files:

1. **Ensure Python is Installed:**
   Make sure you have Python installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/).

2. **Download the Repository:**
   Clone or download this repository to your local machine.

3. **Navigate to the Directory:**
   Open a terminal or command prompt and navigate to the directory where the Python file (`try.py`), `Input_01.txt`, and `Input_02.txt` are located.

4. **Run the Script:**
   Execute the following command to run the Python script:

   ```bash
   python try.py

   
## View Output:
The script will display the longest and second longest compounded words based on the provided input files.

## Approach Overview
The goal of the solution is to identify the longest and second longest compounded words from the given input files (Input_01.txt and Input_02.txt). A compounded word is defined as a word that can be formed by concatenating two or more smaller words without any additional characters in between.

## Recursive Check for Compounded Words
The core of the solution lies in the is_compounded function, which recursively checks if a given word can be compounded. The function takes three parameters: the word to be checked, a set of existing words (word_set), and a memoization dictionary (memo) to optimize repeated computations.

 ```bash
    def is_compounded(word, word_set, memo):
    if word in memo:
        return memo[word]
    
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set and (suffix in word_set or is_compounded(suffix, word_set, memo)):
            memo[word] = True
            return True
    
    memo[word] = False
    return False
```
## Dynamic Programming and Memoization
Dynamic programming is utilized through memoization to store the results of previous computations, avoiding redundant work and improving the efficiency of the solution. The memo dictionary is employed to keep track of whether a particular word is compounded or not.

```bash
  def find_longest_compounded(words):
    words_set = set(words)
    compounded_words = [word for word in words if is_compounded(word, words_set, {})]
    compounded_words.sort(key=len, reverse=True)
    return compounded_words
```
The find_longest_compounded function iterates through the list of words, using the is_compounded function to filter out compounded words. The resulting list is then sorted by length in descending order to obtain the longest compounded words first.



## Contact
LinkedIn: [https://www.linkedin.com/in/aditisaraswat/]
Email: [saraswataditi2002@gmail.com]
Thank you for considering my application. If you have any questions or need further clarification, feel free to reach out.

Best regards,
Aditi Saraswat
