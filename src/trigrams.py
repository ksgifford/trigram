import io
import random


def main(source_file, word_count):
    raw_text = read_file(source_file)
    parsed = parse_text(raw_text)
    trigram = create_trigram(parsed)
    paragraph = create_paragraph(trigram, word_count)
    return paragraph


def read_file(source_file):
    wrapper = io.open(source_file, mode='r')
    source_text = wrapper.read()
    wrapper.close()
    return source_text


def parse_text(raw_text):
    word_list = raw_text.replace('\n', ' ').split()
    return word_list


def create_trigram(word_list):
    word_tuples = list(zip(word_list, word_list[1:], word_list[2:]))
    trigram_dict = {}
    for item0, item1, item2 in word_tuples:
        if trigram_dict.get((item0, item1)):
            trigram_dict[(item0, item1)].append(item2)
        else:
            trigram_dict[(item0, item1)] = [item2]
    return trigram_dict


def create_paragraph(trigram_dict, word_count):
    keys = list(trigram_dict.keys())
    random_key = random.choice(keys)
    paragraph = ' '.join(random_key)
    # ('hello', 'world') => 'hello world'

    while len(paragraph.split()) <= word_count:
        second_to_last, last = paragraph.split()[-2:]

        if not trigram_dict.get((second_to_last, last)):
            second_to_last, last = random.choice(keys)
            # continue

        paragraph += ' ' + random.choice(trigram_dict[(second_to_last, last)])

    print(paragraph)
    return paragraph


if __name__ == '__main__':
    main()
