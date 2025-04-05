import sys

ERROR_MESSAGE = 'ERROR: all values must be numeric'

def sort(width: float, height: float, length: float, mass: float) -> str:
    try:
        is_heavy = mass >= 20
        is_bulky = width >= 150 or height >= 150 or length >= 150 or width * height * length >= 1000000
    except TypeError:
        print(ERROR_MESSAGE)
        return None

    if is_bulky and is_heavy:
        return 'REJECTED'
    
    if is_bulky or is_heavy:
        print('HERE')
        return 'SPECIAL'
    
    return 'STANDARD'

if __name__ == '__main__':
    try:
        print('The package was sorted into the following stack:', sort(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
    except ValueError:
        print(ERROR_MESSAGE)