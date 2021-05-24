# run THIS file to draw the Fourier Series :)

# Program Flow (importing all at once messes up window captions)
from recorder import recorder
path = recorder()

from coeff import coeff
coefficients = coeff(path)

from display import display
display(coefficients, len(path))
