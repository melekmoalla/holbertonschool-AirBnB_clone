<div align=center>  
    <img  
    style="text-align:center"  
    src="https://raw.githubusercontent.com/coding-max/hbtn_config/main/assets/head_low-level.png"  
    alt="Holberton School"/>  
</div>

# File Storage

File Storage module is responsible for storing objects in a file using JSON serialization/deserialization.

# Classes

* FileStorage

# FileStorage Class
* This class provides the functionality to read and write the contents of the objects created by classes derived from the BaseModel class to and from a file in JSON format.

# Properties
* __file_path: private instance string: represents the path to the JSON file (ex: file.json)
* __objects: private instance dictionary: empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)

# Methods

* all(self) -> Dict[str, Dict[str, Any]]: returns the dictionary __objects
* new(self, obj: BaseModel) -> None: sets in __objects the obj with key <obj class name>.id
* save(self) -> None: serializes __objects to the JSON file (path: __file_path)
* reload(self) -> None: deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing)

# Usage

<a href="https://ibb.co/VYdLkz4"><img src="https://i.ibb.co/JjNcSGJ/Screenshot-2023-02-23-115944.png" alt="Screenshot-2023-02-23-115944" border="0"></a>

# Notes

This class is not intended to be used by the user directly, but through the classes derived from BaseModel.

The all, new, save, and reload methods are meant to be used internally by the BaseModel and other classes that derive from it.

The FileStorage class is used to create an instance of itself and create an instance of the BaseModel class. The methods of the FileStorage class are used to store and retrieve the object to/from the JSON file.
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