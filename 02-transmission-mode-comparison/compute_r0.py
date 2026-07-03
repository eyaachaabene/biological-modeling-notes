from pathlib import Path
import sys
project_dir = Path(__file__).parent
sys.path.append(str(project_dir / 'src'))
from extended_tiv_model import compute_R0_cellfree, compute_R0_celltocell, DEFAULTS
T0 = 4e8
beta_f = DEFAULTS['beta_f']
beta_c = DEFAULTS['beta_c']
delta = DEFAULTS['delta']
p = DEFAULTS['p']
c = DEFAULTS['c']
R0_cf = compute_R0_cellfree(beta_f, T0, p, delta, c)
R0_cc = compute_R0_celltocell(beta_c, T0, delta)
R0_comb = R0_cf + R0_cc
print(f"R0_cf={R0_cf:.3f}")
print(f"R0_cc={R0_cc:.3f}")
print(f"R0_combined={R0_comb:.3f}")
