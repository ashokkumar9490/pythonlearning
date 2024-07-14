def analyze_text(text):
    words = text.split()

    
    word_count = len(words)

    
    unique_words = len(set(words))

    
    total_characters = sum(len(word) for word in words)
    average_word_length = round(total_characters / word_count, 2)

    
    longest_word = max(words, key=len)

    
    return {
        'word_count': word_count,
        'unique_words': unique_words,
        'average_word_length': average_word_length,
        'longest_word': longest_word
    }


text = "This is a sample text welcome to python"


print(analyze_text(text))