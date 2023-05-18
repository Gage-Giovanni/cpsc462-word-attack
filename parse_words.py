with open('words_original.txt', 'r') as words_original:
    with open('words.txt', 'w') as word_file:
        for word in words_original:
            if len(word) < 8:
                word_file.write(word)