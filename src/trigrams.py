import io


def main(source_file, generation_amt):
    pass


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


if __name__ == '__main__':
    main()
