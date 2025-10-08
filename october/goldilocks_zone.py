import math


def goldilocks_zone(mass):
    # Calculate the luminosity of the star
    luminosity = pow(mass,3.5)
    
    # calculate the square root of luminosity
    square_root = math.sqrt(luminosity)

    # start, end distances
    start = 0.95 * square_root
    end = 1.37 * square_root
    return [float(f'{start:.2f}'), float(f'{end:.2f}')]

print(goldilocks_zone(1))