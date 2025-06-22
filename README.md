# DataPlanes-TKinter
Project inspired by EUROCONTROL's Aircraft Database, built in Python using the
Tkinter and SQLite3 libraries. Displays data of airplanes and allows input of
new airplane data.

## Requirements

- Python 3.10 or newer (the project was developed with Python 3.12)
- Tkinter (bundled with standard Python installations)
- SQLite3 (standard library module)

## Running the application

Run the main program from the repository root:

```bash
python RAD/main.py
```

Aircraft information is saved locally in `RAD/planes.db` and user data in
`RAD/users.db`.

## Optional: virtual environment

If you prefer to isolate the installation, create and activate a virtual
environment before running the application:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use "venv\Scripts\activate"
```

There are currently no external package requirements, but a virtual environment
keeps any future dependencies isolated from your system Python installation.
