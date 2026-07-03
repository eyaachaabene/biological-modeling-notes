"""Extended TIV models comparing cell-free and cell-to-cell transmission.

This module provides three ODE variants that share the same state vector
[T, I, V]:

Variant 1 - cell-free only:
  infection term proportional to T * V (free-virus mediated)

Variant 2 - cell-to-cell only:
  infection term proportional to T * I (direct contact mediated)

Variant 3 - combined:
  both routes act simultaneously with additive infection terms.

Parameters and units
--------------------
beta_f : mL / TCID50 / day (cell-free infection rate)
beta_c : mL / cell / day (cell-to-cell infection rate)
delta  : 1 / day (infected cell death rate)
p      : TCID50 / cell / day (viral production rate)
c      : 1 / day (viral clearance rate)

Functions follow numpy-style docstrings. No classes are used; the
module is intentionally minimal and suitable for student research work.
"""

import numpy as np
from scipy.integrate import solve_ivp

# Default parameters (Baccam 2006 for cell-free where applicable)
DEFAULTS = {
    "beta_f": 3.2e-5,
    "delta": 4.0,
    "p": 4.6e-2,
    "c": 5.2,
    # choose beta_c so beta_c * T0 ~ beta_f * V_peak (order-of-magnitude parity)
    "beta_c": 1e-7,
}


def tiv_cellfree(t, y, beta_f, delta, p, c):
    """Cell-free only TIV model.

    Parameters
    ----------
    t : float
        Time (days).
    y : array-like
        State vector [T, I, V].
    beta_f : float
        Cell-free infection rate (mL / TCID50 / day).
    delta : float
        Infected-cell death rate (1 / day).
    p : float
        Virus production rate (TCID50 / cell / day).
    c : float
        Viral clearance rate (1 / day).

    Returns
    -------
    list
        [dT/dt, dI/dt, dV/dt]
    """
    T, I, V = y
    dT_dt = -beta_f * T * V
    dI_dt = beta_f * T * V - delta * I
    dV_dt = p * I - c * V
    return [dT_dt, dI_dt, dV_dt]


def tiv_celltocell(t, y, beta_c, delta, p, c):
    """Cell-to-cell only TIV model (infection scales with T * I).

    Parameters
    ----------
    t : float
        Time (days).
    y : array-like
        State vector [T, I, V].
    beta_c : float
        Cell-to-cell infection rate (mL / cell / day).
    delta, p, c : as above

    Returns
    -------
    list
        [dT/dt, dI/dt, dV/dt]
    """
    T, I, V = y
    dT_dt = -beta_c * T * I
    dI_dt = beta_c * T * I - delta * I
    dV_dt = p * I - c * V
    return [dT_dt, dI_dt, dV_dt]


def tiv_combined(t, y, beta_f, beta_c, delta, p, c):
    """Combined TIV model with both cell-free and cell-to-cell routes.

    Parameters
    ----------
    t : float
        Time (days).
    y : array-like
        State vector [T, I, V].
    beta_f : float
        Cell-free infection rate.
    beta_c : float
        Cell-to-cell infection rate.
    delta, p, c : as above

    Returns
    -------
    list
        [dT/dt, dI/dt, dV/dt]
    """
    T, I, V = y
    infection_cf = beta_f * T * V
    infection_cc = beta_c * T * I
    dT_dt = -infection_cf - infection_cc
    dI_dt = infection_cf + infection_cc - delta * I
    dV_dt = p * I - c * V
    return [dT_dt, dI_dt, dV_dt]


def solve_model(model_func, params_tuple, t_span, t_eval, y0=None):
    """Integrate a given TIV model function using scipy.solve_ivp.

    Parameters
    ----------
    model_func : callable
        The ODE right-hand-side with signature (t, y, *params).
    params_tuple : tuple
        Parameters to pass to ``model_func`` after (t, y).
    t_span : tuple
        (t0, tf) integration interval in days.
    t_eval : array-like
        Times at which to store the computed solution.
    y0 : array-like, optional
        Initial state [T0, I0, V0]. If None, defaults to [4e8, 0, 75].

    Returns
    -------
    OdeResult
        The solve_ivp result object.
    """
    if y0 is None:
        y0 = [4e8, 0.0, 75.0]
    solution = solve_ivp(model_func, t_span, y0, args=params_tuple, t_eval=t_eval, method='RK45', rtol=1e-6, atol=1e-8)
    return solution


def compute_R0_cellfree(beta_f, T0, p, delta, c):
    """Compute basic reproduction number R0 for cell-free route.

    Formula: R0 = (beta_f * p * T0) / (delta * c)

    Parameters
    ----------
    beta_f : float
    T0 : float
        Initial target cell count (cells).
    p, delta, c : floats

    Returns
    -------
    float
        R0 value for cell-free transmission.
    """
    return (beta_f * p * T0) / (delta * c)


def compute_R0_celltocell(beta_c, T0, delta):
    """Compute R0 for cell-to-cell route.

    Formula: R0 = beta_c * T0 / delta

    Parameters
    ----------
    beta_c : float
    T0 : float
    delta : float

    Returns
    -------
    float
        R0 value for cell-to-cell transmission.
    """
    return (beta_c * T0) / delta


def compute_phi(beta_c, beta_f, V_ss):
    """Compute fraction of new infections from cell-to-cell route at steady state.

    phi = beta_c / (beta_c + beta_f * V_ss)

    Parameters
    ----------
    beta_c : float
    beta_f : float
    V_ss : float
        Steady-state viral load (TCID50/mL)

    Returns
    -------
    float
        Fraction (0-1) attributable to cell-to-cell transmission.
    """
    denom = beta_c + beta_f * V_ss
    if denom == 0:
        return 0.0
    return beta_c / denom
