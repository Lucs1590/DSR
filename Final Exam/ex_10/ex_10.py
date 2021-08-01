import numpy as np
import math


def main():
    """ # Main
    This is a backbone of the project. This Fuction runs all the others.
    """
    c_a = [0.2, 1, 0.7]
    c_b = [0.3, 0.9, 0.8]
    template = [0.2, 0.9, 0.9]

    d1 = calculate_euclidian_distance(template, c_a)
    d2 = calculate_euclidian_distance(template, c_b)
    print(
        'Template: {0};\nClass A: {2}\n   - dist: {4}\nClass B: {3};\n   - dist: {5}\n\
The class closest to the template is the class: {1}.'.format(
            template,
            c_b if d1 > d2 else c_a,
            c_a,
            c_b,
            d1,
            d2
        )
    )


def calculate_euclidian_distance(_template, _class):
    """# Calculate Euclidian Distance

    Args:
        _template (list): list with the template samples.
        _class (list): list to compare with template.

    Returns:
        float: distance between template and class.
    """
    return math.sqrt(sum((np.array(_template) - np.array(_class))**2))


if __name__ == '__main__':
    main()
