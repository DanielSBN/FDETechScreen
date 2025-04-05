import sys

NUMERIC_ERROR_MESSAGE = 'ERROR: all values must be numeric'

def sort(width: float, height: float, length: float, mass: float) -> str:
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        print('ERROR: all values must be positive')
        return None

    try:
        is_heavy = mass >= 20
        is_bulky = width >= 150 or height >= 150 or length >= 150 or width * height * length >= 1000000
    except TypeError:
        print(NUMERIC_ERROR_MESSAGE)
        return None

    if is_bulky and is_heavy:
        return 'REJECTED'
    
    if is_bulky or is_heavy:
        return 'SPECIAL'
    
    return 'STANDARD'

if __name__ == '__main__':
    try:
        stack = sort(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
        if stack is not None:
            print('The package was sorted into the following stack:', stack)
    except ValueError:
        print(NUMERIC_ERROR_MESSAGE)