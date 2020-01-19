# Utils.py

def check_int(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False
def check_str(input):
    try:
        val = int(input)
        return False
    except ValueError:
        return True