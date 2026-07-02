"""A minimal target-infected-virus model for within-host influenza infection.

The model tracks three state variables: T, the number of uninfected target cells;
I, the number of infected cells actively producing virus; and V, the free viral
load measured in TCID50/mL. The parameters beta, delta, p, and c describe the
infection rate, infected-cell death rate, viral production rate, and viral
clearance rate, respectively. The default values follow the Baccam et al. (2006)
parameterization for influenza A infection in humans.
"""

import numpy as np
from scipy.integrate import solve_ivp


def tiv_ode(t, y, beta, delta, p, c):
    """Return the right-hand side of the TIV ordinary differential equations.

    Parameters
    ----------
    t : float
        Time in days.
    y : array-like
        State vector containing T, I, and V.
    beta : float
        Infection rate constant in mL / TCID50 / day.
    delta : float
        Death rate of infected cells in per day.
    p : float
        Virus production rate per infected cell in TCID50 / cell / day.
    c : float
        Viral clearance rate in per day.
    """
    T, I, V = y

    dT_dt = -beta * T * V
    dI_dt = beta * T * V - delta * I
    dV_dt = p * I - c * V

    return [dT_dt, dI_dt, dV_dt]


def solve_tiv(params, t_span, t_eval, y0=None):
    """Integrate the TIV model with scipy solve_ivp.

    Parameters
    ----------
    params : dict
        Dictionary containing beta, delta, p, and c.
    t_span : tuple
        Integration interval (t_start, t_end) in days.
    t_eval : array-like
        Times at which the solution is returned.
    y0 : array-like, optional
        Initial conditions for [T0, I0, V0].
    """
    if y0 is None:
        y0 = [4e8, 0.0, 75.0]

    beta = params["beta"]
    delta = params["delta"]
    p = params["p"]
    c = params["c"]

    solution = solve_ivp(
        tiv_ode,
        t_span,
        y0,
        args=(beta, delta, p, c),
        t_eval=t_eval,
        method="RK45",
        rtol=1e-6,
        atol=1e-8 
    )

    return solution
