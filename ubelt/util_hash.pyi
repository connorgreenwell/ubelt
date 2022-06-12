from typing import Union
from typing import Tuple
from typing import Callable
from ubelt.util_const import NoParam
from ubelt.util_const import NoParamType
from typing import List
from os import PathLike
from typing import Any, TypeVar

Hasher = TypeVar("Hasher")
HASH_VERSION: int
DEFAULT_ALPHABET: Any


def b(s):
    ...


DEFAULT_HASHER: Any


class _Hashers:
    algos: Any
    aliases: Any

    def __init__(self) -> None:
        ...

    def available(self):
        ...

    def __contains__(self, key):
        ...

    def lookup(self, hasher):
        ...


class HashableExtensions:
    keyed_extensions: Any
    iterable_checks: Any

    def __init__(self) -> None:
        ...

    def register(self, hash_types: Union[type, Tuple[type]]) -> Callable:
        ...

    def lookup(self, data):
        ...

    def add_iterable_check(self, func):
        ...


class _HashTracer:
    sequence: Any

    def __init__(self) -> None:
        ...

    def update(self, bytes) -> None:
        ...

    def hexdigest(self):
        ...


def hash_data(data: object,
              hasher: Union[str, Hasher, NoParamType] = NoParam,
              base: Union[List[str], str, NoParamType] = NoParam,
              types: bool = False,
              convert: bool = False,
              extensions: HashableExtensions = None) -> str:
    ...


def hash_file(fpath: PathLike,
              blocksize: int = 1048576,
              stride: int = 1,
              maxbytes: Union[int, None] = None,
              hasher: Union[str, Hasher, NoParamType] = NoParam,
              base: Union[List[str], str, NoParamType] = NoParam):
    ...
