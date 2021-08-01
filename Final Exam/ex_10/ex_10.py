import numpy as np


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    c_a = []
    c_b = []
    template = []

    d1 = calculate_euclidian_distance(template, c_a)
    d2 = calculate_euclidian_distance(template, c_b)
    print(
        'Template: {};\nThe class closest to the template is the class: {}.'.format(
            template,
            c_b if d1 > d2 else c_a
        )
    )


def calculate_euclidian_distance(template, classe):
    ...


if __name__ == '__main__':
    main()
