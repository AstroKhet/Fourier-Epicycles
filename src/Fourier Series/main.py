# run THIS file to draw the Fourier Series :)

from recorder import recorder
from coeff import coeff
from display import display

# Program Flow
path = recorder()
coefficients = coeff(path)
display(coefficients, len(path))

