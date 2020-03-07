from fuzzywuzzy import fuzz
from tryner import get_store_results

def extract_store_name(text):
    with open("company_list", "r") as f:
        for line in f.readlines():
            s = fuzz.partial_ratio(text, line,)
            if s > 85:
                return line
            else:
                call_bert(text)

def call_bert(text):
    return get_store_results(text)

if __name__ == "__main__":
    text = "belgian waffle"
    extract_store_name(text)
