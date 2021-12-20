# OCA Box
Common API for telesocpes.

Based on [EthanChappel/Alpyca](https://github.com/araucaria-project/ocabox)

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

## Documentation
All methods have docstrings accessible with Python's built-in [```help()```](https://docs.python.org/3/library/functions.html#help) function.

For additinal documentation see `/doc` directory.


