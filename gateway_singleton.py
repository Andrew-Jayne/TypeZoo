from typing import Self


class GatewaySingleton:
    _instance: Self | None = None

    def __init__(self) -> None:
        if self._instance is not None:
            raise RuntimeError(f"{GatewaySingleton.__name__} is already initialized")
        self._instance = self

    @classmethod
    def get_instance(cls) -> Self:
        if cls._instance is None:
            raise RuntimeError(f"{cls.__name__} has not been initialized")
        return cls._instance
