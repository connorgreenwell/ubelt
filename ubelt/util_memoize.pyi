from typing import Callable
from typing import Union
from _typeshed import Incomplete


def memoize(func: Callable) -> Callable:
    ...


class memoize_method:
    __func__: Incomplete

    def __init__(self, func) -> None:
        ...

    def __get__(self, instance: object, cls: Union[type, None] = None):
        ...

    def __call__(self, *args, **kwargs):
        ...


def memoize_property(fget):
    ...
