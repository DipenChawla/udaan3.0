from rotation import rotate
from correct_skew import skew_correction

def correction(image_path):
    rotate(image_path)
    skew_correction(image_path)
    return 0


