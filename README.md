# OCA Box
Common API for telescopes.

Uses [EthanChappel/Alpyca](https://github.com/araucaria-project/ocabox) classes for
ASCOM Alpaca API.

# Developer Installation
```bash
 git clone https://github.com/araucaria-project/ocaboxapi.git
 pip install -e ocaboxapi
```

## Configuration
Observatory configuration is kept in YAML configuration files. 
The configuration files are read one after one, and latter overwrites former.
The configuration is expected to be found in the following locations:
```
              <package_path>/ocaboxapi/default.cfg.yaml
              ~/ocabox.cfg.yaml
              ./ocabox.cfg.yaml
```

See the `ocaboxapi/default.cfg.yaml` for the example.

The top level is the configuration preset name. Preset may include another preset(s).
(See how in `ocabox/default.cfg.yaml` preset `default` includes concrete one).

Each preset contains single `observatory` keyword, which is also the root of device tree.

Each key in the `components` section represents `sys_id` of the component. The only obligatory
key for component is `kind`, which can be (at the moment) one of:
* `telescope`
* `dome`
* `camera`
* `filterwheel`
* `focuser`
* `rotator`
* `switch`
* `safetymonitor`


## Usage
Observatory structure - devices tree is defined in `YAML` configuration file(s) (see above).
Children can be accessed by their `sys_id` as a parent's attributes or via ```Component.children```
dictionary. Parent component is stored in  ```Component.parent``` attribute.

All the commands, and properties of actual telescope driver are available as methods of specific
device class.

E.g.
```python
from ocaboxapi import Observatory

observatory = Observatory()

observatory.connect('default')

tel = observatory.my_telescope  # sys_id "my_telescope" is a key in config file

tel.slewtocoordinates(11.4, -52.239)
tel.park()

```



## Documentation
All device's methods have docstrings accessible with Python's built-in 
[```help()```](https://docs.python.org/3/library/functions.html#help) function.

For additional documentation see `/doc` directory.


