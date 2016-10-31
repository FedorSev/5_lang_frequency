import collections
import re
import os


def load_data(filepath):
    if not os.path.exists(filepath) or os.path.isdir(filepath):
        return None

    with open(filepath, 'r') as text_file:
        text = text_file.read()
        return text


def get_most_frequent_words(text):
    split_text = re.findall(r'\w+', text.lower())
    words = collections.Counter(split_text).most_common(10)
    return words


def print_most_frequent_words(words):
    print('MOST FREQUENT WORDS:')
    print('--------------------')
    for word in words:
        print(word[0] + '\t- ' + str(word[1]))


if __name__ == '__main__':
    while True:
        filepath = input('Введите путь к файлу: ')
        data = load_data(filepath)

        if data is not None:
            print_most_frequent_words(get_most_frequent_words(data))
            break

        else:
            print('Некорректный адрес файла, повторите ввод')
