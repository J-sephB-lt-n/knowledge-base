---
created:
  - 2025-01-14T22:52
modified: 2025-11-10 11:38
tags:
  - python
  - design-patterns
  - software
  - software-engineering
  - dev
  - builder-pattern
  - polymorphism
type:
  - note
status:
  - abandoned
---
These are my notes I took while working through the Linkedin-Learning course [Advanced Python: Build Hands-On Projects with Design Patterns](https://www.linkedin.com/learning/advanced-python-build-hands-on-projects-with-design-patterns)

* [What are Design Patterns?](#What%20are%20Design%20Patterns?)
* [Inheritance](#Inheritance)
* [Polymorphism](#Polymorphism)
* [Builder Pattern](#Builder%20Pattern)
## What are Design Patterns?

_Design patterns_ are language-neutral solutions for common software problems.

## Inheritance

A child class:
* Keeps the attributes and methods of it's parent class
* Adds new attributes and methods it's parent does not have
* Overrides methods of the parent class 

## Polymorphism

* Depends on inheritance
* Polymorphism is the ability of an object (e.g. entity or class) to take on different forms.
Examples:

```python
# Run-time Polymorphism (Method Overriding):
# (subclass provides specific implementation of method defined in it's superclass (parent class)
class StorageClient:
	def save_file(file_contents: bytes, file_name: str):
		NotImplementedError

class LocalFilesystemClient(StorageClient):
	def save_file(file_contents: bytes, file_name: str):
		...

class RemoteBlobStorageClient(StorageClient):
	def save_file(file_contents: bytes, file_name: str):
		...

if os.environ.get["APP_CONTEXT"]=="prod":
	storage_client: StorageClient = RemoteBlobStorageClient()
else:
	storage_client: StorageClient = LocalFilesystemClient()

storage_client.save_file(myfile_contents, "temp.txt")
```

```python
# Compile-time Polymorphism (Method Overloading)
# (behaviour of a function/method changes based on the inputs)
def greet(self, name: str = None, time_of_day: str = None) -> str: 
	if name and time_of_day: 
		return f"Good {time_of_day}, {name}"
	elif name: 
		return f"Hello, {name}" 
	else: 
		return "Hello"
```

## Builder Pattern

A creational design pattern which addresses the "Telescoping Constructor" anti-pattern.

The [Builder Pattern](#Builder%20Pattern) aims to reduce the complexity which results when constructing a complex object.


## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here