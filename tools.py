# Function to format numbers in scientific notation for plots

from matplotlib.ticker import ScalarFormatter
import numpy as np


f =  ScalarFormatter(useOffset=False, useMathText=True)
f.set_scientific(True)
f.set_powerlimits((0, 0))

def sci_notation(x):
    if x == 0:
        return "0"
    else:
        formatted = f"{x:.2e}"  # Converte in notazione scientifica
        coefficient, exponent = formatted.split('e')
        exponent = int(exponent)  # Converti l'esponente a intero
        return f"${coefficient} \\times 10^{{{exponent}}}$"  # Notazione LaTeX
    
# Initalizing constants

K = 1.380649e-23 # J / K
vc = 299792458 # m / s
h_pl = 6.62607015e-34 # J*s
T_cmb = 2.726 # K
omegab_h2 = 0.0224

I0 =(2*K**3*T_cmb**3)/(vc**2*h_pl**2)*1e26 # in Jy / sr

# Normalised distortion spectral shapes

def nbb(x): return (1/(np.exp(x)-1)) # * I0
def G(x): return (x * np.exp(x) * nbb(x)**2 )   # intensity not occupation number /4.0 * I0
def Y(x): return x**3 * I0 * (G(x) * ( x * ( 2 * nbb(x) + 1 ) - 4 ) ) / 4.0
def M(x): return x**3 * I0 * (G(x) * ( 1.0 / 2.1923 - 1.0 / x ) ) * 1.401
def D(x): return x**3 * I0 * (G(x) * 1.6449 / (3*2.4041) - nbb(x) / x) / 0.5421 