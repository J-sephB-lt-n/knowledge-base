---
created:
  - 2025-01-14T22:52
modified: 2025-01-14 23:32
tags:
  - python
  - design-patterns
  - software
  - software-engineering
  - dev
type:
  - note
status:
  - in-progress
---
These are my notes I took while working through the Linkedin-Learning course [Advanced Python: Build Hands-On Projects with Design Patterns](https://www.linkedin.com/learning/advanced-python-build-hands-on-projects-with-design-patterns)

* [What are Design Patterns?](#What%20are%20Design%20Patterns?)
## What are Design Patterns?

_Design patterns_ are language-neutral solutions for common software problems.

## Inheritance

A child class:
* Keeps the attributes and methods of it's parent class
* Adds new attributes and methods it's parent does not have
* Overrides methods of the parent class 

## Polymorphism

* Depends on inheritance
* Polymorphism refers to being able to use objects of different classes interchangeably because they share the same interface
Examples:
```python
# Run-time Polymorphism (Method Overriding):
# (subclass provides specific implementation of method defined in it's superclass (parent class)
class StorageClient:
	def save_file(file_contents: bytes, file_name: str):
		raise NotImplementedError

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
## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here