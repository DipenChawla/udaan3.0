def get_product(text):
    for line in text.split("\n"):
        yield " ".join([x for x in line.split() if x.isalpha()])

def extract_product_list(text):
    return list(get_product(text))


if __name__ == "__main__":
    text = """ RICE HG SG(LG)   1.00    259.0   259.0
    CRISPY CHILLI BABY CORN     1.0     122.0   122.0
"""
    print(list(extract_product_list(text)))

