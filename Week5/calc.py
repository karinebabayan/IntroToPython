def calculate_cube(x):
    return(x**3)
def calculate_square(x):
    return(x**2)
import pretty_print
def main():
    result = calculate_square(2)
    pretty_print.simple_print(result)
    result = calculate_cube(4)
    pretty_print.pro_print(result)

if __name__ == '__main__':
    main()