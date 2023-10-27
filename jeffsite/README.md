# Healtchare DB Management

This README provides detailed instructions and information about the Flask application located in app.py. This application is designed to interact with SQLite databases, allowing users to perform various operations such as creating and dropping tables, adding data to tables, and viewing table data through a web interface.

## Project Features
+ Creating a Table
+ Populating Table
+ Dropping Table
+ Viewing Table Data

## Requirements
- Python 3.6 or Later
- Flask 
- SQLite

**Installation**

1. Clone GitHub Repository to your Local Machine
```powershell
git clone https://github.com/aguzzar2/Python.Projects.git
```
2. Navigate to your Repository
```powershell
cd Python.Projects
```
3. Check if Python is Installed
```powershell
python --version
``` 
4. Create a Virtual Environment 
```powershell
python3 -m venv env
```

## Activating Virtutal Environment
```powershell
./env/Scripts/activate
```
You will see something like <strong>'(env) PS C:\Users'</strong> indicating the virtual environment was created successfully! In this case (env) is the name of my environment.

## Executing
<p>This Web Application is going to be executed using the <strong>app.py</strong> file.
<p>You can run it from the parent directory by using the command: </p>

```powershell
flask --app app run
```
The app will run on the local server <strong>http://127.0.0.1:5000</strong>
<p>To quit program use <strong>CTRL+C</strong> in CLI</p>

## Leaving Virtual Environment
```powershell
deactivate
```
## Application Features
<p>You are taken to a home page with a <strong>Tables</strong> dropdown menu with the following options:</p>

    Create Table        Drop Table
    Populate Table      Show Tables
    
<p><strong>'Show Tables'</strong> will redirect to a new page where you can observe the various tables in the databases that currently exist.