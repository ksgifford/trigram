import io


def main(source_file, generation_amt):
    pass


def read_file(source_file):
    pass


def parse_text(raw_text):
    pass


def create_trigram(text):
    for i, word in enumerate(text.split()):
        trigram[(text[i:i + 1], text[i + 1:i + 2])] = text[i + 2:i + 3]


if __name__ == '__main__':
    main()
