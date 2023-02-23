# AirBnB clone - The console

<a href="https://ibb.co/jzpFN45"><img src="https://i.ibb.co/cwmdBTv/Screenshot-2023-02-23-100629.png" alt="Screenshot-2023-02-23-100629" border="0"></a>
---

# Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.

* !!!!! please click on the photo to view !!!!

[![Alt text](https://img.youtube.com/vi/E12Xc3H2xqo/0.jpg)](https://www.youtube.com/watch?v=E12Xc3H2xqo)



# First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

<a href="https://ibb.co/PQ5ZhJ3"><img src="https://i.ibb.co/py3vzNG/Screenshot-2023-02-23-114150.png" alt="Screenshot-2023-02-23-114150" border="0"></a>
# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# Resources
Read or watch:

* [cmd module](https://intranet.hbtn.io/rltoken/_mUwX-Mn69bDBP5iTQmCJA)
packages concept page
* [uuid module](https://intranet.hbtn.io/rltoken/4HNpF8nsTMociNaTgMYAeQ)
* [datetime](https://intranet.hbtn.io/rltoken/xnmMG0Qin2K9CxXdmQoZkA)
* [unittest module](https://intranet.hbtn.io/rltoken/MKNUT1FRSdUiGIpwMmrtgw)
* [args/kwargs](https://intranet.hbtn.io/rltoken/mY-8n8I-ohQIjkUOqcK6Rw)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/9PsyQoeiVNhWGcj_1PkZJg)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
# Requirements
Python Scripts:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests:

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# More information

<a href="https://ibb.co/qmm1sSb"><img src="https://i.ibb.co/P11ChLB/Screenshot-2023-02-23-114130.png" alt="Screenshot-2023-02-23-114130" border="0"></a>
<a href="https://ibb.co/PQ5ZhJ3"><img src="https://i.ibb.co/py3vzNG/Screenshot-2023-02-23-114150.png" alt="Screenshot-2023-02-23-114150" border="0"></a>

# AirBnB Clone Project to give detail

This project is an implementation of a command-line interface that emulates the functionalities of the AirBnB platform.

The main goal of this project is to provide an easy way to manage data models, using a persistent storage system, a JSON file.

The project has the following modules:

models: This module contains the classes for the different data models used in the project (User, Place, Review, City, Amenity, and State).
tests: This module contains the unit tests for the models and the console.
engine: This module contains the FileStorage class used to manage the JSON file.

# How to start it
To start the command interpreter, run the following command:
````
./console.py
````
# You will see a prompt like this one:
````
(hbnb)
````
# How to use it

The command interpreter provides the following commands:

* create: Creates a new instance of a class, saves it to the JSON file, and prints its id.
* show: Prints the string representation of an instance based on the class name and id.
* destroy: Deletes an instance based on the class name and id and saves the change into the JSON file.
* all: Prints all string representation of all instances based or not on the class name.
* update: Updates an instance based on the class name and id by adding or updating attribute and saves the change into the JSON file.
* quit or EOF: Exits the command interpreter.
* help: Shows the documentation of the commands.

To get more information about a command, type help followed by the command name.

# Examples

To create a new User instance:
````
(hbnb) create User
````
To show the User instance with id 1234-1234-1234:
````
(hbnb) show User 1234-1234-1234
````
To destroy the User instance with id 1234-1234-1234:
````
(hbnb) destroy User 1234-1234-1234
````
To show all instances of the User class:
````
(hbnb) all User
````
To update the email attribute of the User instance with id 1234-1234-1234:
````
(hbnb) update User 1234-1234-1234 email "aibnb@mail.com"
````
# Requirements
The project has been developed using Python 3.4.3.

There are no additional requirements needed to run the command interpreter.
# Testing
To run the tests, execute the following command:
````
python3 -m unittest discover tests
````
Or if you prefer to see the verbose output:
````
python3 -m unittest discover -v tests
````
# the importance in this project
Serialization and Deserialization flow:

In this project, serialization and deserialization are used to store the data in a JSON file and to retrieve the data from the JSON file. The data is first stored in an object, which is then converted into a dictionary using the to_dict() method. This dictionary is then converted into a JSON string using the json.dumps() method and written to a file using the File I/O operations. When the data needs to be retrieved from the JSON file, the JSON string is first read from the file and then converted into a dictionary using the json.loads() method. This dictionary is then used to create an object using the class constructor.

Packages / Modules / Cyclical imports / How to import / Prevent execution /Etc.:

The project is divided into several modules, each of which contains a set of related classes and functions. The main module is console.py, which is the command interpreter that interacts with the user. Other modules include models, engines, and tests. To prevent cyclic imports, the imports are done within the functions rather than at the top of the module. To import a module, the import statement is used followed by the name of the module. To import a specific class or function from a module, the from statement is used followed by the name of the module and the name of the class or function. To prevent execution when importing a module, the if name == 'main': statement is used at the bottom of the module.


Layered architecture:
The project follows a layered architecture, which is a design pattern that separates the concerns of the different components of the system into distinct layers. The layers include the presentation layer, the application layer, and the data layer. The presentation layer is the console.py module, which is responsible for interacting with the user. The application layer includes the models and engines modules, which are responsible for implementing the business logic of the system. The data layer includes the file_storage.py module, which is responsible for storing and retrieving the data from the JSON file.

Interfaces (storage):
The file_storage.py module provides an interface for storing and retrieving data from the JSON file. The interface includes the methods all(), new(), save(), reload(), delete(), and update(), which are used to retrieve all the objects, create a new object, save the objects to the file, reload the objects from the file, delete an object, and update an object respectively. This interface allows the other modules to interact with the data layer without having to know the implementation details.

 ## Author

*  https://github.com/melekmoalla