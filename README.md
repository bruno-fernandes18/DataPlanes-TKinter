# DataPlanes-TKinter

DataPlanes-TKinter is a Python project inspired by EUROCONTROL's Aircraft Database, built using the Tkinter and SQLite3 libraries. It provides a graphical interface to display and manage airplane data, allowing users to consult existing data, add new entries, and make updates.

## Getting Started

To use this project, run the `main.py` file in a Python terminal. This will launch the graphical interface, where users can access the main features: browsing the database, adding new airplane data, updating existing records, and deleting entries.

## Features

### 1. User Authentication: Register, Login, Logoff

Access authentication options via the menu in the top-right corner of the main interface. Users can register a new account, log in, and log off.

### 2. Data Checking: Display Airplane Data

Accessed through the **Database** button, this feature loads all airplanes in the database into a tuple format, and shows detailed information for the selected entry, which the first by default. The database includes organized categories based on official documentation guidelines. *Note*: The "Similar Aircrafts" feature is currently not implemented.

### 3. Data Creation: Create New Airplane Data and Set Images

Use the **Add Plane** button to open the airplane creation form. Enter valid information for each field to add a new airplane to the database. Additionally, you can upload an image (320x180 PNG format) to represent the aircraft by specifying the file path.

### 4. Data Manipulation: Manage Airplane Data

Accessed through the **Manage Plane** button, this feature opens a screen displaying all airplanes in the database along with options to delete or update selected entries. When an aircraft is selected, its details are displayed, allowing you to modify or remove the record as needed.
