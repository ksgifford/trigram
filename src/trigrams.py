import io
import random
import sys


def main(source_file, word_count):
    """Call component functions to build paragraph for printing."""
    raw_text = read_file(source_file)
    parsed = parse_text(raw_text)
    trigram = create_trigram(parsed)
    paragraph = create_paragraph(trigram, word_count)
    return paragraph


def read_file(source_file):
    """Read source file and store contents locally."""
    wrapper = io.open(source_file, mode='r')
    source_text = wrapper.read()
    wrapper.close()
    return source_text


def parse_text(raw_text):
    """Scrub raw text from source file to reformat '_' and '\n' characters."""

    # TODO: What about quotes and other special characters? Could write a
    # separate function just for scrubbing.
    word_list = raw_text.replace("_", "").replace('\n', ' ').split()
    return word_list


def create_trigram(word_list):
    """Generate a list of three-word tuples from parsed text."""
    """Convert list of tuples to trigrams and populate trigram dict."""

    # Found some examples of using the zip() method to create n-grams here:
    # http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    word_tuples = list(zip(word_list, word_list[1:], word_list[2:]))
    trigram_dict = {}
    for item0, item1, item2 in word_tuples:
        if trigram_dict.get((item0, item1)):
            trigram_dict[(item0, item1)].append(item2)
        else:
            trigram_dict[(item0, item1)] = [item2]
    return trigram_dict


def create_paragraph(trigram_dict, word_count):
    """Create output paragraph from keys and values in trigram dictionary."""

    # Seed paragraph string with a random key from the trigram dict.
    keys = list(trigram_dict.keys())
    random_key = random.choice(keys)
    paragraph = ' '.join(random_key)

    # Iterates until specified word count is reached. Pulls last two words from
    # paragrah and searches the trigram dict for a matching key, then randomly
    # selects one of the corresponding values and appends that word to the
    # paragraph.
    while len(paragraph.split()) < word_count:
        second_to_last, last = paragraph.split()[-2:]

        # TODO: What happens if random.choice() keeps selecting dead-end keys?
        if not trigram_dict.get((second_to_last, last)):
            second_to_last, last = random.choice(keys)

        paragraph += ' ' + random.choice(trigram_dict[(second_to_last, last)])
    return paragraph


if __name__ == "__main__":
    paragraph = main(sys.argv[1], int(sys.argv[2]))
    print(paragraph)
