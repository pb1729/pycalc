import numpy as np
import matplotlib.pyplot as plt

try:
    import readline
    has_readline = True
except ModuleNotFoundError:
    has_readline = False


print('\n\t\t\t---- Pycalc ----\n')

# functions:
sqrt = np.sqrt
mod = np.mod
atan2 = np.arctan2
Re = np.real; Im = np.imag
conj = np.conj; angle = np.angle
exp  = np.exp; log  = np.log
sin  = np.sin; cos  = np.cos; tan = np.tan
arcsin = np.arcsin; arccos = np.arccos; arctan = np.arctan
sinh  = np.sinh; cosh  = np.cosh; tanh = np.tanh
arcsinh = np.arcsinh; arccosh = np.arccosh; arctanh = np.arctanh
cross = np.cross # vector cross product
dot = np.dot # vector dot product and matrix multiplication

# mathematical constants:
pi  = np.pi
e   = np.e
tau = 2 * np.pi
i   = 1j
rms_sin = sqrt(2) # convert RMS amplitude to actual amplitude

# physical constants
G   = 6.674e-11             # [m.m.m/kg.s.s]
k_B = 1.380649e-23          # [J/K]
hbar= 1.054571817e-34       # [J.s]
c   = 299792458             # [m/s]
epsilon_0= 8.8541878128e-12 # [F/m]
mu_0= 1.25663706212e-6      # [H/m]
N_A = 6.02214076e23         # [/mol]        # Avogadro's Number
# Stefan-Boltzmann Constant:
sigma_SB = (pi**2 * k_B**4) / (60 * hbar**3 * c**2) # [J/m.m.s.K^4]

# physical data
q_e = 1.602176634e-19       # [C]           # Elementary Charge
m_e = 9.1093837015e-31      # [kg]          # Electron Mass
m_p = 1.67262192369e-27     # [kg]          # Proton Mass
m_n = 1.67492749804e-27     # [kg]          # Neutron Mass
m_u = 1.6605390666e-27      # [kg]          # Atomic mass unit (dalton)
r_B = 5.29177210904e-11     # [m]           # Bohr radius
minute = 60                 # [s]
hour = 60 * minute          # [s]
day = 86400                 # [s]
year= 365.2425*day          # [s]
celsius_0 = 273.15          # [K]
m_E = 5.9722e24             # [kg]          # Earth Mass
m_S = 1.98847e30            # [kg]          # Sun Mass
C_H2O = 4179.6              # [J/kg.K]      # Specific Heat Capacity of Liquid Water at 25 Celsius

# united states customary units
inch = 0.0254               # [m]
foot = 12 * inch            # [m]
mile = 5280 * foot          # [m]
nautical_mile = 1852        # [m]
acre = 43560 * (foot**2)    # [m.m]
teaspoon = 4.92892159375e-6 # [m.m.m]
tablespoon = 3 * teaspoon   # [m.m.m]
fl_oz = 2 * tablespoon      # [m.m.m]
cup = 8 * fl_oz             # [m.m.m]
pint = 2 * cup              # [m.m.m]
quart = 2 * pint            # [m.m.m]
gallon = 4 * quart          # [m.m.m]
ounce = 28.349523125e-3     # [kg]
pound = 16 * ounce          # [kg]
us_ton = 2000 * pound       # [kg]
horsepower = 735.49875      # [W] (metric horsepower)

# temperature conversion functions
def F2C(F): return (F - 32) * 5/9
def C2F(C): return 32 + C * 9 / 5
def C2K(C): return C + celsius_0
def K2C(K): return K - celsius_0

# obtaining greek letters:
get_symb = {'alpha': 'Αα', 'beta': 'Ββ', 'gamma': 'Γγ', 'delta': 'Δδ', 'epsilon': 'Εε',
    'zeta': 'Ζζ', 'eta': 'Ηη', 'theta': 'Θθ', 'iota': 'Ιι', 'kappa': 'Κκ', 'lambda': 'Λλ',
    'mu': 'Μμ', 'nu': 'Νν', 'xi': 'Ξξ', 'omicron': 'Οο', 'pi': 'Ππ', 'rho': 'Ρρ',
    'sigma': 'Σσς', 'tau': 'Ττ', 'upsilon': 'Υυ', 'phi': 'Φφ', 'chi': 'Χχ', 'psi': 'Ψψ', 'omega': 'Ωω'}

# make a dictionary of useful formulas
formulas = {
    'newton gravity': 'F_g = G * m_1 * m_2 / r**2',
    'newton gravity vector': 'F_g = -G * m_1 * m_2 * r / abs(r)**2',
    'coulomb electric force': 'F_C = q_1*q_2 / (4*pi*epsilon_0 * r**2)',
    'coulomb electric force vector': 'F_C = q_1*q_2*r / (4*pi*epsilon_0 * abs(r)**2)',
    'newton\'s second law vector': 'F = m*a',
    'angular momentum vector': 'L = cross(r, p)',
    'centripetal acceleration (angular circle centrifugal)': 'a_c = r * omega**2',
}
def ldform(query):
    """ allows the user to load a formula based on search query """
    terms = query.split()
    formlist = []
    for key in formulas:
        if all( (term in key) for term in terms ):
            print(len(formlist), key, ':', formulas[key])
            formlist.append(formulas[key])
    if len(formlist) > 0:
        which = int(input('   which formula? >'))
        if has_readline:
            readline.replace_history_item(readline.get_current_history_length() - 1, formlist[which]) # replace user entering number with formula
        return formlist[which]
    else:
        return 'no formulas found'

def fplot(flst, xlims=[0, 1.], ylims=None):
    """ allows the user to plot a or list of functions, flst,
    each fn represented either as a string (fn of x) or as a python function """
    if not isinstance(flst, list):
        flst = [flst]
    for f in flst:
        x = np.linspace(xlims[0], xlims[1], 256)
        if isinstance(f, str):
            y = eval(f)
        else:
            y = f(x)
        plt.plot(x, y)
        if ylims != None:
            plt.ylim(ylims)
    plt.show()
    return 'plot...'

def vec(*args):
    return np.array(args)

if __name__ == '__main__':
    # initialize ans to 0, and make a history list, multiline mode initially false
    ans  = 0
    hist = []
    mult = False
    code = []

    # calc loop
    while True:
        if mult:
            line = input('\t| ')
            if line == 'quit':
                break
            elif line == '=}':
                mult = False
            else:
                code.append(line)
        else:
            if len(code) > 0:
                inp = '\n'.join(code)
                code = []
            else:
                inp = input('pycalc> ')
            
            if inp == 'quit':
                break
            elif inp == '':
                pass
            elif inp == '{=': # multiline input
                mult = True
                code = []
            else:
                try:
                    if '=' in inp or '\n' in inp:
                        exec(inp)
                    else:
                        result = eval(inp)
                        print(result)
                        if not isinstance(result, str):
                            ans = result
                    hist.append(inp)
                except Exception as error:
                    print(error)


