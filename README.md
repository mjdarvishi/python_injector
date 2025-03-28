# Dependency Injection Library

This is a simple Python dependency injection library that provides an easy way to register and retrieve instances of classes. It allows you to decouple class dependencies and simplifies testing and maintenance of your codebase.

## Features
- Register and retrieve instances with ease.
- Manage dependencies using simple factory methods.
- Supports flexible dependency injection for classes with minimal boilerplate.

## Installation

To install this package, clone the repository and install the dependencies:

```bash
git clone https://github.com/mjdarvishi/python_injector
cd python_injector
pip install .

```

Alternatively, you can also install it directly:

```bash
pip install python-injector
```
Usage
Registering Dependencies
To register a class or service with the injector, you need to define a factory function that creates instances of the class. This is done using the Injector.register method.

```python
from injector import Injector

# Example classes
class Repository:
    pass

class RepositoryImpl(Repository):
    pass

# Registering the implementation of the Repository
injector = Injector()
injector.register(Repository, lambda: RepositoryImpl())

# Retrieving an instance of ShopRepository
repo = injector.get(Repository)
```