## Example usage

```python
from ocaboxapi import Observatory

observatory = Observatory()

observatory.connect('default')

luke = observatory.luke_telescope

luke.slewtocoordinates(11.4, -52.239)
luke.park()

```