### Python - Exercise-6  

## Create A python program to practice combine working with strings, lists, and dictionaries to analyze text data. You'll create a function named analyze_text that takes a piece of text as input and returns a dictionary containing information about the text.

**Function: analyze_text(text)**

Parameters:

text: A string representing the text to be analyzed.
Returns:

A dictionary containing the following key-value pairs:
word_count: The total number of words in the text.
unique_words: The number of unique words in the text.
average_word_length: The average length of words in the text (rounded to two decimal places).
longest_word: The longest word in the text.

**Sample Input:**

text = "This is a sample text to analyze. It contains multiple sentences and some interesting vocabulary."

**Sample Output:**

{'word_count': 13, 'unique_words': 11, 'average_word_length': 5.38, 'longest_word': 'vocabulary'}

Explanation:

The analyze_text function should first split the text into a list of words using appropriate string methods.
Use list methods and set operations to calculate the number of words, unique words, and find the longest word.
Calculate the average word length by dividing the total number of characters (excluding spaces) by the word count.
Create a dictionary with the calculated values for each key and return the dictionary.

**Challenge:**

Extend the function to handle punctuation marks. Convert all words to lowercase before processing them.
Modify the function to return a list of the 10 most frequent words (excluding stop words like "the", "a", "an").


