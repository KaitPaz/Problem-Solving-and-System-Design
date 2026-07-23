import re
import string

def read_input_text(filename):
    """Read the input text from a file. Then, tokenize into words

    Args: 
        Filename (string data type): Name of the file containing input text.

    Returns: 
        List: a list of tokens
    """

    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the entire contents of the file as a single string
        text = file.read()

    # Convert all text to lowercase to keep tokens consistent
    text = text.lower()

    # Split the text into words based on whitespace
    # (spaces, newlines, tabs)
    tokens = text.split()

    return tokens

def load_words_from_file(filename):
    """
    Loads a set of words (either positive or negative) from a file

    Each line int the file should contain a single word

    Args: 
        filename (str): the path to the file containing positive/negative words
    """

    words = set()

    # Open the file in read mode
    with open(filename, "r") as file:
        for line in file:
            # Remove leading/trailing whitespace and newline characters
            word = line.strip().lower()

            # Only add non-empty lines
            if word:
                words.add(word)

    return words

def input_to_sentences(multiSentenceInput):
    """Splits input text into individual sentences.

    Args:
        multiSentenceInput (str): Entire contents of input.txt

    Returns:
        list: A list of strings, one for each sentence.
    """
    # Replace newlines with spaces so sentences aren't broken
    text = multiSentenceInput.replace("\n", " ").strip()

    # Regex pattern to capture sentences including punctuation
    # Explanation:
    #   .*?      → match as few characters as possible
    #   [.!?]    → stop at sentence-ending punctuation
    pattern = r'.*?[.!?]'

    # Find all sentence matches
    sentences = re.findall(pattern, text)

    # Clean up extra whitespace
    sentences = [sentence.strip() for sentence in sentences]

    return sentences


# Function to split the string into substrings
def sentence_to_words(sentence):
    """Spilts a sentence into individual words
    arg(s)
        -Sentence (str)

    returns:  
        - List of strings for each word in the sentence
    """ 

    # Remove punctuation
    for char in string.punctuation:
        sentence = sentence.replace(char, "")

    # Convert to lowercase and split
    return sentence.lower().split()


def sentence_analysis(words, pWords, nWords):
    """ Determines if a sentence is considered positive, negative, or neutral
    depending on keywords from the file

    Args:
        - Words (str): Words in each sentece to analyze
        - pWords (str): Positive words to compare from load_words_from_file(positive.txt)
        - nWords (str): Negative words to compare from load_words_from_file(negative.txt)
    Returns:
        - Sentiment of a particular sentence (str) (positive, negative, neutral)
    """

    positive_count = 0
    negative_count = 0

    # Count positive and negative words
    for word in words:
        word = word.lower()

        if word in pWords:
            positive_count += 1
        elif word in nWords:
            negative_count += 1

    # Determine sentiment based on counts
    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# Implementation

# Read input text
with open("input.txt", "r") as file:
    text = file.read()

# Split into sentences
sentences = input_to_sentences(text)

# Load positive and negative words (make sure these exist)
positiveWords = load_words_from_file("positive.txt")
negativeWords = load_words_from_file("negative.txt")

# Open output.txt for writing (it will be created if it doesn't exist)
with open("output.txt", "w") as outfile:
    for s in sentences:
        wordsInSentence = sentence_to_words(s)
        analysis = sentence_analysis(wordsInSentence, positiveWords, negativeWords)

        # Write to the new file
        outfile.write(f"{analysis}: {s}\n")
