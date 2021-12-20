## Example usage


```python
from api import Observatory

observatory = Observatory()

observatory.connect('alpaca')

luke = observatory.luke_telescope

luke.slewtocoordinates(11.4, -52.239)
luke.park()

```