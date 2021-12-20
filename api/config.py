import os.path
from os import PathLike

import yaml  # pip install pyyaml
from typing import Optional, Iterable, Union


class Config:
    _singleton = None

    def __init__(self) -> None:
        self.data = {}

    @classmethod
    def global_config(cls) -> dict:
        return cls.global_config()['protocol']

    @classmethod
    def global_instance(cls) -> 'Config':
        if cls._singleton is None:
            cls.global_instance_from_files()
        return cls._singleton

    @classmethod
    def global_instance_from_files(cls, source: Optional[Iterable[Union[str, PathLike]]] = None) -> None:
        cls._singleton = cls.instance_from_files(source=source)

    @classmethod
    def instance_from_files(cls, source: Optional[Iterable[str]] = None) -> 'Config':
        cfg = cls()
        cfg.read_config(source=source)
        return cfg

    def read_config(self, source: Optional[Iterable[str]] = None) -> None:
        if not source:
            source = [
                os.path.join(os.path.dirname(__file__), 'default.cfg.yaml')
            ]
        config = {}
        for src in source:
            with open(src) as fd:
                y = yaml.safe_load(fd)
                config.update(y)
        # expand includes
        for k in config.keys():
            self.expand_includes(config, k)
        self.data = config

    @classmethod
    def expand_includes(cls, d: dir, key: str) -> None:
        try:
            incs = d[key].pop('include')
        except KeyError:
            return
        if isinstance(incs, str):
            incs = [incs]
        for i in incs:
            cls.expand_includes(d, i)
            d[key].update(d[i])
