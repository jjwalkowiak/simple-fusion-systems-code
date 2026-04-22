#!/usr/bin/env python

# Simple fusion reactor systems code, based on the approach in Plasma Physics and Fusion Energy, Freidberg
# Section 5.5
# Adapted and expanded by Richard Kembleton for TU/e Fusion Reactor Design Masterclass
# 2021
# Additional plasma equations from Iter Physics Design Guidelines 1989 (Uckan)
# and Iter Physics Basis Nucl. Fusion 39 (1999)
# Radiation equations from
# Matthews et al, Nuc. Fus. 39 (1999)
# Johner, Fus. Sci. Tech. 59 (2011)
# Uckan (1989)

# %%

from IPython import embed
from simplesystemcode import InputParameters, simplesystemcode
from utilities import plot_scan, write_csv

# %%

# Assumed inputs/targets: have a play! 
input_parameters = InputParameters(
	GrossElecPower=650.0, # MW
    # Neutron wall load in MW/m^2
	WallLoad=1.2,
    # Maximum magnetic field on the TF superconductor in Tesla
	BMax=12.5,
    # Maximum stress on the TF structure in MPa
	SigmaMax=1000.0,
	# Fractional concentration of Li6 in breeder material (7.5% in natural lithium)
	Li6=0.60,
	# Neutron shielding efficiency target for blanket and vacuum vessel
	NeutShield=0.99,
	# Blanket/shield structural support thickness in meters
	BlktSupport=0.3,
	# Thermal efficiency of electricity generation (Pe/Pth)
	ThermalEff=0.25,
	# Plasma elongation
	Kappa=1.6,
	# Plasma temperature in keV
	PlasmaT=12.6,
	# Plasma safety factor (q_edge)
	SafetyFac=3.5,
	# Current drive efficiency (gamma_CD)
	GamCD=0.7,
	# Electrical efficiency of the CD system
	ElectEffCD=0.9,
	# Fraction of extracted heat representing coolant pumping power.
	PowerRecirc=0.05,
	# Plasma effective charge number
	ZEff=2.2
)

# %%

## Do a single run of the systems code
design_point = simplesystemcode(input_parameters)

# %%

## sample code for elongation scan
elongations = [1.0,1.1,1.2,1.3,1.4,1.5,1.6]
NWL_limit = [0.8, 0.9, 1.0, 1.1, 1.2]
scan_out = []

# for elongation in elongations:
# 	input_parameters.Kappa = elongation
# 	scan_out.append(simplesystemcode(input_parameters, print_out=False))

for NWL in NWL_limit:
	input_parameters.WallLoad = NWL
	scan_out.append(simplesystemcode(input_parameters, print_out=False))
    

# %%

## Sample code for visualising a scan
plot_scan(scan_out, 'betaN', 'RMajor')

# %%

## Sample code for exporting scan data to .csv for Mimer (https://assar.his.se/mimer/html/). Be careful with overwriting data!
write_csv(scan_out, filename = 'demo_output.csv')

# %%

## Option to look at scan embedded in IPython, by typing e.g. "scan_out[3]", "scan_out[5]"
# embed()
