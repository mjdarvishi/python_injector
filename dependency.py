from typing import Type, TypeVar, Dict, Callable
from app.config import Settings
T = TypeVar("T")

class Injector:
    _factories: Dict[Type, Callable[[], object]] = {}

    @classmethod
    def register(cls, type_: Type[T], factory: Callable[[], T]):
        cls._factories[type_] = factory

    @classmethod
    def get(cls, type_: Type[T]) -> T:
        if type_ in cls._factories:
            return cls._factories[type_]()
        raise ValueError(f"No registered factory for type: {type_.__name__}")

    @classmethod
    def clear(cls):
        cls._factories.clear()

    def __getitem__(self, type_: Type[T]) -> Callable[[], T]:
        return lambda: self.get(type_)

def get_settings():
    return Settings()


injector = Injector()