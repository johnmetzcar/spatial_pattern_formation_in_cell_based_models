# Spatial Pattern Formation in Cell Based Models
Exploring spatial pattern formation in cell-based models, starting with Turing patterns in PhysiCell

This [repo](https://github.com/johnmetzcar/spatial_pattern_formation_in_cell_based_models) houses the code for the ENRG-E 399/599 final project for Team 1.  Team members: [John Metzcar])(https://github.com/johnmetzcar) and [Ben Duggan](https://github.com/BenSDuggan).  The goal of this project is to create Turing-like patterns using [PhysiCell](https://github.com/MathCancer/PhysiCell).  You can download the code and run it (found in the PhysiCell directory) or run it on (NanoHub)[].

Example simultion of the model:
![sim results](/docs/images/sample.gif)

## Model Description
### Cell agents:
There are 3 cells in the model: A cells, B cells and Wall cells.
* A cells are the inhibitor cells and are <span style="color:blue">blue</span>.
	* Using live cycle model and apoptosis
	* Motility enabled, persistance time of 5 minutes, migration bias set to 0 (completely random).
	* Secretes alpha and is effected by beta
* B cells are the effected by A cells and are <span style="color:yellow">yellow</span>.
	* Using live cycle model and apoptosis
	* Motility enabled, persistance time of 5 minutes, migration bias set to 0 (completely random).
	* Secretes beta and is effected by alpha
* Wall cells are placed along the outside of the domain and prevent cells spilling outside of the domain. <span style="color:black">black</span>.
	* Using live cycle model and apoptosis but both have rates set to 0 (disabeling them)
	* Motility disabled
	* Secretes and uptakes nothing

### Chemical components
Only alpha and beta chemiclas are used in this simulation (no oxygen).  

### Domain
The domain is initilized to be a 500 um x 500 um with dx=dy=dz=20 um.  The simulations are designed to be run in 2D but could be converted to 3D with ease.  The domain is initiallized with wall cells along the outer perimiter.  The A and B cells are initilized ____________________- final initialization here.

