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