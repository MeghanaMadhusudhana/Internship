def count_word_frequencies(text):
    # Initialize an empty dictionary to store word frequencies
    word_frequencies = {}

    # Split the text into words
    words = text.split()

    # Iterate through each word in the list
    for word in words:
        # Remove punctuation and convert to lowercase for better matching
        word = word.strip('.,!?()-"').lower()

        # Check if the word is already in the dictionary
        if word in word_frequencies:
            # If it is, increment the count by 1
            word_frequencies[word] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            word_frequencies[word] = 1

    return word_frequencies

if __name__ == "__main__":
    text = "This is a simple example. Simple is as simple does."

    # Get word frequencies
    word_frequencies = count_word_frequencies(text)

    # Print the word frequencies
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")
