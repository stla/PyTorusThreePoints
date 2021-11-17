# PyTorusThreePoints

Draw a torus passing through three given points.

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/example2.png)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/example3.png)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/example4.png)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/HopfFibration.png)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/HopfGreatCircle.gif)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/CliffordCircles.gif)

![](https://github.com/stla/PyTorusThreePoints/raw/main/examples/VillarceauCircles.gif)

## Usage

```python
import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints

plotter = pv.Plotter()

torusThreePoints(
  plotter, p1, p2, p3, r, S=64, s=32, show=False, ....
)
```

#### Arguments

- `plotter`: PyVista plotter region
- `p1, p2, p3`: three points (numpy arrays)
- `r`: minor radius
- `S,s`: numbers of subdivisions for the torus mesh
- `show`: whether to show the figure (if `True`, this closes the plotter)
- `...`: parameters passed on to `pyvista.add_mesh`, such as `smooth_shading=True, color="red", specular=0.9`

Instead of setting `show=True`, you can run `plotter.show()` once you're done.
