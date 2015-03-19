import pyknot2.spacecurves as sp
from pyknot2 import make
k = sp.Knot(make.knot.figure_eight(100)*10)
k.plot()
k.rotate()
k.plot_projection()
k.alexander_polynomial()
import sympy as sym
t = sym.var('t')
k.alexander_polynomial(t)
k.alexander_polynomial(mode='maxima')
gc = k.gauss_code()
print(gc)
gc.simplify()
print(gc)
gc = k.gauss_code(recalculate=True)
print(gc)
k.rotate()
gc = k.gauss_code(recalculate=True)
print(gc)
gc.simplify()
print(gc)
pd = k.planar_diagram()
print(pd)
k.writhe()
k.average_crossing_number()
k.planar_writhe()
k.octree_simplify(10)
k.plot()
k.octree_simplify(50)
k.plot_projection()