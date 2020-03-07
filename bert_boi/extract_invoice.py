import re
import itertools


def get_window(sentence, phrase, window_size):
    sentence = sentence.split()
    phrase = phrase.split()
    words = len(phrase)

    for i, word in enumerate(sentence):
        if word == phrase[0] and sentence[i : i + words] == phrase:
            start = max(0, i - window_size)
            yield " ".join(sentence[start : i + words + window_size])


def extract_invoice(text):
    try:
        alphanumeric_lst = []
        pattern_lst = ["INVOICE", "BILL NO", "INVTR", "TOKEN"]
        for p in pattern_lst:
            l = list(get_window(text, p, 2))
            for em in l:
                longest_an = max(em.split(), key=len)
                if longest_an.isalnum():
                    alphanumeric_lst.append(longest_an)
        return max(alphanumeric_lst, key=len)
    except:
        return []


if __name__ == "__main__":
    text = """ TAX INVOICE
GSTIN NO # 33AABCB1043Q12T
INVOICE NO # CM1786190022812
INVOICE DATE # 09/11/2019
"""
    print(extract_invoice(text))

