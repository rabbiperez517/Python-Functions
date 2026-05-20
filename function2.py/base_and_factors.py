#This function returns a boolean if the number is a fcator of the base or not
def is_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False