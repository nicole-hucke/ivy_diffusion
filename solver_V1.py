""" A solver for the 1D diffusion equation. 
- Inputs:

concentration:
spacing:
timestep:
diffusivity: 

- Outputs:

"""

import numpy as np
np.set_printoptions(formatter={'float': '{: 5.1f}'.format})

def solve1d(concentration, spacing, timestep, diffusivity):
    q = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= timestep * np.diff(q) / spacing #-= is grabbing the concentration and subtracting it to what I told it to 
    return concentration


def ejemplo():
    D = 100
    L = 10
    space = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(L)
    C[: int(L/2)] = C1
    C[int(L/2) :] = C2
    dt = space * space / D / 2.1
    print(C)
    
    solve1d(C, space, dt, D)
    print(C)
    
    for _ in range(1,5):
        C = solve1d(C, space, dt, D)
        print(C)
    
    
if __name__ == "__main__":
    ejemplo()
    

    
