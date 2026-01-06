---
created:
  - 2025-01-05T15:05
modified: 2025-12-30 21:09
tags:
  - dependency-injection
type:
  - note
status:
  - in-progress
---
`Dependency Injection` is a software design pattern intended to decrease coupling and increase cohesion.  

| Contents                                                                                  |
| ----------------------------------------------------------------------------------------- |
| [Inversion of Control](#Inversion%20of%20Control)                                         |
| [Dependency Injection](#Dependency%20Injection)                                           |
| [Dependency Injection Example in Python](#Dependency%20Injection%20Example%20in%20Python) |

## Inversion of Control

_Inversion of Control_ is a software principle (design pattern) which separates the _what_ (required functionality) from the _how_ (the way the functionality is achieved) by making control code (e.g. **main.py**) call abstractions rather than directly managing dependencies and implementation details itself i.e. implementation is delegated to a framework or external component.

[Inversion of Control](#Inversion%20of%20Control) achieves:
- Loose coupling and modularity (components don't depend on each other directly, and components can be swapped out without breaking the code)
- Testability (easier to test individual components in isolation, easy to change behaviour of the application by switching out components)
- Flexibility (easier to adapt code to new requirements)
- Reusability (components can be reused in different parts of the application)

[Dependency Injection](#Dependency%20Injection) is one way of achieving [Inversion of Control](#Inversion%20of%20Control).
## Dependency Injection

_Dependency Injection_ is a software design pattern. 
_Dependency Injection_ involves classes being given their dependencies (objects or services required in order for the class to function) rather than the class creating them itself.

See [Dependency Injection Example in Python](#Dependency%20Injection%20Example%20in%20Python)
## Dependency Injection Example in Python

```python
# inventory_service.py
from abc import ABC, abstractmethod

import httpx

class InventoryService(ABC):
	@abstractmethod
	def get_stock_level(self, sku: str) -> int:
		raise NotImplementedError

	@abstractmethod
	def set_stock_level(self, sku: str, quantity: int) -> bool:
		raise NotImplementedError

class RemoteInventoryService(InventoryService):
	def get_stock_level(self, sku: str) -> int:
		return int(
			httpx.get(
				url="https://invent.ory/get-stock-level",
				params={"sku": sku},
			).text
		)

	def set_stock_level(self, sku: str, quantity: int) -> bool:
		response = httpx.post(
			url="https://invent.ory/set-stock-level",
			json={"sku": sku, "quantity": quantity},
		)
		if response.status_code == 200:
			return True
		return False

class LocalInventoryService(InventoryService):
	def __init__(self):
		self.inventory: dict[str, int] = {}

	def get_stock_level(self, sku:str) -> int:
		if sku not in self.inventory:
			return 0
		return self.inventory[sku]

	def set_stock_level(self, sku: str, quantity: int) -> bool:
		self.inventory[sku] = quantity
		return True

# main.py
import os

import inventory_service

if __name__ == "__main__":
	inventory: inventory_service.InventoryService
	if os.environ.get("APP_CONTEXT") == "prod":
		inventory = inventory_service.RemoteInventoryService()
	else:
		inventory = inventory_service.LocalInventoryService()
	inventory.set_stock_level("A69b420", 80085)
	print( inventory.get_stock_level("A69b420") ) # 80085
	print( inventory.get_stock_level("d035n073x157") ) # 0
```

Same example, but using python package [dependency-injector](https://pypi.org/project/dependency-injector/):

```python
# inventory_service.py
from abc import ABC, abstractmethod

import httpx

from dependency_injector import containers, providers

class InventoryService(ABC):
	# same body as previous example #

class RemoteInventoryService(InventoryService):
	# same body as previous example #

class LocalInventoryService(InventoryService):
	# same body as previous example #

class InventoryContainer(containers.DeclarativeContainer):
	config = providers.Configuration()
	service = providers.Factory(
		RemoteInventoryService 
		if config.APP_CONTEXT == "prod" 
		else LocalInventoryService, 	
	)

# main.py
import inventory_service
	
if __name__ == "__main__":
	inventory_container = inventory_service.InventoryContainer()
	inventory_container.config.APP_CONTEXT.from_env("APP_CONTEXT") # or from config file etc.
	inventory_container.wire(modules=[__name__])
	inventory: inventory_service.InventoryService = inventory_container.service()
	inventory.set_stock_level("A69b420", 80085)
	print( inventory.get_stock_level("A69b420") ) # 80085
	print( inventory.get_stock_level("d035n073x157") ) # 0
```
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here
* [Software Architecture Concepts](Software%20Architecture%20Concepts.md)