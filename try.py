import time

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

def find_longest_compounded(words):
    words_set = set(words)
    compounded_words = [word for word in words if is_compounded(word, words_set, {})]
    compounded_words.sort(key=len, reverse=True)
    return compounded_words

def main():
    start_time = time.time()

    # Read input files
    with open("Input_01.txt", "r") as file:
        words_01 = [line.strip() for line in file]

    with open("Input_02.txt", "r") as file:
        words_02 = [line.strip() for line in file]

    # Combine words from both files
    all_words = words_01
    all_words2= words_02 

    # Find the longest and second longest compounded words
    compounded_words = find_longest_compounded(all_words)
    compounded_words2 = find_longest_compounded(all_words2)

    # Display results
    if compounded_words:
        print("Longest Compounded Word in input 1:", compounded_words[0])
        if len(compounded_words) > 1:
            print("Second Longest Compounded Word in input 1:", compounded_words[1])
    else:
        print("No compounded words found.")


     # Display results
    if compounded_words2:
        print("Longest Compounded Word in input 2:", compounded_words2[0])
        if len(compounded_words2) > 1:
            print("Second Longest Compounded Word in input 2:", compounded_words2[1])
    else:
        print("No compounded words found.")

    # Display time taken
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to process input files: {elapsed_time:.4f} seconds")

    
    


if __name__ == "__main__":
    main()
