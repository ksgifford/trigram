# -*- coding: utf-8 -*-
TEST_TEXT = """One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own."""


def test_read_file():
    """Tests read_file() against established text sample."""
    from trigrams import read_file
    assert TEST_TEXT in read_file("example.txt")


def test_parse_text():
    """Tests parse_text to ensure proper handling of new lines and spaces."""
    from trigrams import parse_text
    assert parse_text("One\ntwo three") == ["One", "two", "three"]


def test_create_trigram():
    """Tests create_trigram() for creation of trigrams from word list."""
    from trigrams import create_trigram
    word_list = ["I", "wish", "I", "may", "I", "wish", "I", "might"]
    expected = {
        ("I", "wish"): ["I", "I"],
        ("wish", "I"): ["may", "might"],
        ("may", "I"): ["wish"],
        ("I", "may"): ["I"]
    }
    assert create_trigram(word_list) == expected


def test_create_paragraph():
    """Tests create_paragraph() output for proper length and type."""
    from trigrams import create_paragraph
    trigram = {
        ("I", "wish"): ["I", "I"],
        ("wish", "I"): ["may", "might"],
        ("may", "I"): ["wish"],
        ("I", "may"): ["I"]
    }
    # Because create_paragraph() contains random choice elements, we cannot
    # test against an exact string output. These asserts check that the
    # output string matches the specified word count & is of the correct type.
    assert len(create_paragraph(trigram, 10).split()) == 10
    assert type(create_paragraph(trigram, 10)) == str
