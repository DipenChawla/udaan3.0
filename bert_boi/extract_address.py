from tryner import get_address_results

def extract_store_address(text):
    return get_address_results(text)

if __name__ == "__main__":
    text = "belgian waffle"
    extract_store_address(text)
