'''
from .lp_prev.py import lin_sep
from .lp_scipy.py import lin_sep
from .lp_cvxpy.py import lin_sep
from .lp_sphere.py import lin_sep
'''

"""
NOTE: 

I know the syntax is problematic, we can change it later on, this is just for functionality. This is how it may be used:

	import lin_sep as lp

	lp.lp_prev.lin_sep(...)
"""
