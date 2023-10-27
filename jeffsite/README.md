# Healtchare DB Management

This README provides detailed instructions and information about the Flask application located in app.py. This application is designed to interact with SQLite databases, allowing users to perform various operations such as creating and dropping tables, adding data to tables, and viewing table data through a web interface.

## Project Features
+ Creating a Table
+ Populating Table
+ Dropping Table
+ Viewing Table Data

## Requirements
- Python 3.6 or Later (an)
- Flask 
- Native SQLite3

**Installation**

1. Clone GitHub Repository to your Machine
```powershell
git clone https://github.com/aguzzar2/Python.Projects.git
```
2. Navigate to your Repository
```powershell
cd Python.Projects
```
3. Create a Virtual Environment
```powershell
python3 -m venv env
```

## Activate Virtutal Environment
```powershell
./env/Scripts/activate
```

## Install Packages

```powershell
py -m pip install requests
```

## Running Application
Running the application requires a congifuration file.
```powershell
python app.py
```

## Configuration
Application requires a <strong>'data'</strong> folder to store SQLite files.
```powershell
cd env
mkdir data
```

## Leaving Virtual Environment
```powershell
deactivate
```