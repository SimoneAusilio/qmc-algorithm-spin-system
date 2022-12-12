## Authors
Simone Ausilio, Nunzia Revel-Carsalade

## About
This project implements Quantum Monte Carlo algorithms for worldline configurations applied to the XXZ 1-D quantum spin chain, as described in **F. F. Assaad, H. G. Evertz**, *World line and determinantal Quantum Monte Carlo methods for spins, phonons, and electrons*.

## Structure
1. Libraries (contain useful functions used in other parts of the project)
    - ***weight***: calculates graph weights for loop update
    - ***vertex***: maps the bijection square plaquette from/to vertex plaquette and forms loops
    - ***spin***: implements spin operators for a square plaquette
    - ***configurations_initial_worldsquares***: library of possible initial worldline configurations
2. Classes (main codes to develop the algorithms)
    - ***square***: defines the square plaquette, the building block of the Configuration class (in *Worldline_chessboard*)
    - ***Worldline_chessboard***: creates the worldline configuration and implements the **local update**
    - ***Configuration***: converts from worldline configuration to spin configuration (each vertex of the chessboard is converted to the spin +1 or -1)
    - ***breakup_graph***: defines the plaquette-graphs/breakups for a square plaquette
    - ***graph_chessboard***: creates the plaquette-graph version of a worldline configuration and implements the **loop update**
3. Tests
    - ***hamiltonian***: calculates energy eigenvalues (old version, refer to *hamiltonian_binary*)
    - ***hamiltonian_binary***: calculates energy eigenvalues using binary representation
    - Others...