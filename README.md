# holbertonschool-AirBnB_clone

## Description:
This is the first step of the project that simulates an AirBnB website clone.
In this step we create an implement only the console.
This console is a command interpreter that will be a tool to validate the storage engine by creating our own data model and managing (create, update, destroy, etc) objects via a console/command interpreter to strore and persist objects to a file (JSON file).

## Files
List of files used in this project:

| File                   | Description                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| **`AUTHORS`**          | List of contributors                                                                                        |
| **`console.py`**       | program called console.py that contains the entry point of the command interpreter.|
| **`base_model.py`**   | Contains a class BaseModel that defines all common attributes/methods for other classes.                                                           |
| **`file_storage.py`** | Contains a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances|
| **`user.py`**     | Define a class User.|
| **`state.py`** | Define a class State.                         |
| **`place.py`**     | Define a class Place.                                      |
| **`review.py`**| Define a class Review.                                                                    |
 |**`city.py`** | Define a class City. |
 |**`amenity.py`** | Define a class Amenity. |
|**`README.md`** | Current file. Contains information about this project. |

## Console
## Commands
The console supports the following commands:
| Command                   | Description                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| **`quit`**          | Exit the console|
| **`EOF`**       | Exit the console with ctrl + D |
| **`help`**   |Prints information about specific command|
| **`create`** |Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.|
| **`show`**     | Prints the string representation of an instance based on the class name and id. |
| **`destroy`** |Deletes an instance based on the class name and id (save the change into the JSON file). |
| **`all`**     | Prints all string representation of all instances based or not on the class name|
| **`update`**| Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |

<h3 align="center">Using the Console</h3>
The console works both in interactive mode and non-interactive mode. It prints a prompt (hbnb) and waits for the user for input.

### Interactive mode:

To use the console in interactive mode, run the 
file `console.py`:

```
$ ./console.py
```
While running in interactive mode, the console displays a prompt (hbnb) for input:

```
$ ./console.py
(hbnb) 
```
## Command examples:
* quit
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb)
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* EOF
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb)
(hbnb) EOF
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* help
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) help quit
Quit command to exit the program.
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* create
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py
(hbnb) create User
71be6abd-fadf-4d24-bb00-8ec5afa3e232
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* show
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) show User 71be6abd-fadf-4d24-bb00-8ec5afa3e232
[User] (71be6abd-fadf-4d24-bb00-8ec5afa3e232) {'id': '71be6abd-fadf-4d24-bb00-8ec5afa3e232', 'created_at': datetime.datetime(2024, 3, 3, 23, 0, 17, 572211), 'updated_at': datetime.datetime(2024, 3, 3, 23, 0, 17, 572219)}
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* destroy
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) destroy User 71be6abd-fadf-4d24-bb00-8ec5afa3e232
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* all
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) all User
[User] (f8a32bfe-bf0d-40d6-9e9a-2d7f746bcca8) {'id': 'f8a32bfe-bf0d-40d6-9e9a-2d7f746bcca8', 'created_at': datetime.datetime(2024, 3, 3, 22, 54, 32, 645813), 'updated_at': datetime.datetime(2024, 3, 3, 22, 54, 32, 645820)}
[User] (d7e85368-b81c-4f68-a767-3cf8dc90d406) {'id': 'd7e85368-b81c-4f68-a767-3cf8dc90d406', 'created_at': datetime.datetime(2024, 3, 3, 22, 55, 44, 108019), 'updated_at': datetime.datetime(2024, 3, 3, 22, 55, 44, 108026)}
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
* update
```
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) create User
c4b1fae1-1634-4f43-a29f-4a59b4378887
(hbnb) update User c4b1fae1-1634-4f43-a29f-4a59b4378887 first_name "holbertonAirBnB"
(hbnb) show User c4b1fae1-1634-4f43-a29f-4a59b4378887
[User] (c4b1fae1-1634-4f43-a29f-4a59b4378887) {'id': 'c4b1fae1-1634-4f43-a29f-4a59b4378887', 'created_at': datetime.datetime(2024, 3, 3, 23, 5, 49, 755518), 'updated_at': datetime.datetime(2024, 3, 3, 23, 6, 52, 69466), 'first_name': '"holbertonAirBnB"'}
(hbnb) quit
root@114be2fa5e5843c691b07ffff598bf79-2377118072:~/holbertonschool-AirBnB_clone#
```
### Non-interactive mode:
To run the console in non-interactive mode enter any command in an execution of the file console.py at the command line.
```bash
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```
## Authors
* **German Aquino** [Github](https://github.com/German1127)
* **Joaquin Fernandez** [Github](https://github.com/Joaquinfer7688)

