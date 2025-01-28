---
created:
  - 2025-01-16T22:07
modified: 2025-01-17 08:56
tags:
  - strategy
  - strategy-pattern
  - design-patterns
  - software-engineering
  - dev
type:
  - note
status:
  - in-progress
---
Main body of note goes here

```python
import logging
import os
from abc import ABC, abstractmethod
from typing import Optional

logging.basicConfig(
	level=logging.INFO, 
	format="%(levelname)s - %(module)s - %(message)s"
)
logger = logging.getLogger(__name__)

############################
# without strategy pattern #
############################
class Context:
	def __init__(self, app_context: Optional[str]) -> None:
		self._app_context: Optional[str] = app_context
		
	def launch_process(self) -> None:
		if self._app_context == "prod":
			logger.info("launched process P")
		elif self._app_context == "staging":
			logger.info("launched process S")
		else:	
			logger.info("launched process D")

if __name__ == "__main__":
	context = Context(app_context=os.environ.get("APP_CONTEXT"))
	context.launch_process()
	# INFO - __main__ - launched process: strategy D

##################################
# strategy pattern using classes #
##################################
class Strategy(ABC):
	@abstractmethod
	def run(self) -> str:
		raise NotImplementedError

class ConcreteStrategyP(Strategy):
	def run(self) -> str:
		return "P"

class ConcreteStrategyS(Strategy):
	def run(self) -> str:
		return "S"

class ConcreteStrategyD(Strategy):
	def run(self) -> str:
		return "D"

class Context:
	def __init__(self) -> None:
		self._strategy: Optional[Strategy] = None

	@property
	def strategy(self) -> Strategy:
		if not self._strategy:
			raise ValueError("no strategy selected")
		return self._strategy

	@strategy.setter
	def strategy(self, strategy: Strategy) -> None:
		logger.info("set strategy to %s", strategy.__class__.__name__)
		self._strategy = strategy
	
	def launch_process(self) -> None:
		logger.info("launched process %s", self._strategy.run())

if __name__ == "__main__":
	context = Context()
	match os.environ.get("APP_CONTEXT"): 
		case "prod": 
			context.strategy = ConcreteStrategyP() 
		case "staging": 
			context.strategy = ConcreteStrategyS() 
		case _: 
			context.strategy = ConcreteStrategyD()
	# INFO - __main__ - set strategy to ConcreteStrategyD
	context.launch_process()
	# 
```
## References
* https://www.freecodecamp.org/news/a-beginners-guide-to-the-strategy-design-pattern/
* https://refactoring.guru/design-patterns/strategy/python/example
## Related
* [Dependency Injection](Dependency%20Injection.md)