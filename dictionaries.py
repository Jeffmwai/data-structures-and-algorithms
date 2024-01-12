import string

def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

if __name__ == "__main__":
    # Test the function here if needed
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
