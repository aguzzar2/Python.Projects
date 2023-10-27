from flask import Flask,\
redirect, session, url_for, request,\
render_template, flash, jsonify

import sqlite3, traceback, os
from random import *

from werkzeug.datastructures import ImmutableMultiDict

###############################
'GLOBALS'
db2_columns = ['basic', 'standard', 'premium']
animals = "animals.txt"
sql_types = ['text', 'integer', 'double', 'float', 'character',\
              'date', 'decimal','int', 'char', 'dec', 'varchar',\
                'enum']
global_db = "t_db2.db"
dynamic_db = ''
data_folder = "env/data/"
###############################



###############################
'miscellaneous'
class queryTable(object):
    def __init__(self, name):
        self.name = name

def importFile(f_name):
    word_list = []
    file = open(f_name, 'r')
    contents = file.readlines()
    for word in contents:
        word_list.append(word[:-1])
    return word_list
###############################




###############################
'CHECK IF FILE || TABLE EXISTS'
###############################

def checkDB(file_name):
    try:
        file = open(data_folder+file_name, 'r')
        file.close()
        print("made it trough DB check")
        return True
    except:
        print("inside checkDB: \n file does not exist")
        return False

def checkTable(file,table):
    if checkDB(file):
        static_db = sqlite3.connect(data_folder+file)
        try:
            cur = static_db.cursor()
            res = cur.execute("SELECT name FROM sqlite_master")
            fetch = res.fetchall()
            if fetch is None:
                print("there are no tables")
                static_db.close()
                return False
            else:
                for t in range(len(fetch)):
                    if table in fetch[t]:
                        print("table exists")
                        return True
                return False
        except:
            static_db.close()
    else:
        print("unable to come up with anything")
        return False
#################################
'END CHECK IF FILE/ TABLE EXISTS'
#################################




###################
'TABLE INFORMATION'
###################
def getTables(db):
    static_db = sqlite3.connect(data_folder+db)
    try:
        cur = static_db.cursor()
        res = cur.execute("select name from sqlite_master")
        info = res.fetchall()
        tables_list = [table[0] for table in info]
        return tables_list
    except:
        static_db.close()
def getTableColumnInfo(file, table_name):
    static_db = sqlite3.connect(data_folder+file)
    try:
        cur = static_db.cursor()
        #sqlite3 doesn't have information.schema to get table names
        #... so have to pull the entire first row
        ex_string = "PRAGMA table_info({})".format(table_name)
        res = cur.execute(ex_string)
        info = res.fetchall()
        columns_names = [column[1] for column in info]
        column_types = [column[2] for column in info]
        both = [column[1:3] for column in info]

        static_db.close()
        return columns_names, column_types, both
    except:
        static_db.close()

def getTableData(file, table_name):
    static_db = sqlite3.connect(data_folder+file)
    try:
        cur = static_db.cursor()
        ex_string = 'select * from {}'.format(table_name)
        res = cur.execute(ex_string)
        info = res.fetchall()
        static_db.close()

        return info
    except:
        static_db.close()
######################
'END TABLE INFORMATION'
######################




############
'EDIT TABLE'
############
def createValueString(col_info, entry):
    value_string = "values("
    for val in range(len(col_info)):
        if len(col_info) == 1:
            if 'text' in col_info[val]:
                value_string += "'$$$')"
            else:
                rn = randrange(1,141423134)
                value_string += f"{rn})"
            return value_string
        elif val == 0:
            if 'text' in col_info[val]:

                value_string += "'XXX', "
            else:
                rn = randrange(1,100)
                value_string += f"{entry}, "
        elif val == len(col_info) - 1:
            
            if 'text' in col_info[val]:
                value_string += "'$$$')"
            else:
                rn = randrange(1,141423134)
                value_string += f"{rn})"
        else:
            if 'text' in col_info[val]:

                value_string += "'$$$', "
            else:
                rn = randrange(1,141423134)
                value_string += f"{rn}, "
    return value_string

def addToTable(file, table_name):
    table = sqlite3.connect(data_folder+file)
    try:
        cur = table.cursor()
        try:
            _, _, c_info = getTableColumnInfo(file, table_name)
        except Exception as e:
            traceback.print_exc()
            print(str(e))
        for entry in range(500):
            value_string = createValueString(c_info, entry)
            print(value_string)
            cur.execute(("INSERT into {} {}").format(table_name, value_string))
            table.commit()
        table.close()        
    except:
        table.close()
################
'END EDIT TABLE'
################

###################
'IMPORT TABLE'
###################
def importTable():
    return 0
###################
'END IMPORT TABLE'
###################


###################
'CREATE/DROP TABLE'
###################

'getKey and getType are aux for creatTable'
def getName():
    get_name = input("Column Name: ").lower()
    if not get_name.isalpha():
        print("no spaces in column name")
        getName()
    return get_name

def getType():
    
    get_type = input("Column Type: ").lower()
    if not get_type.isalpha():
        print("no spaces in column name")
        getType()
    elif get_type not in sql_types:
        print("incorrect type")
        getType()
    return get_type

def createTable(file):
    'instantiate new table w/ num fields'
    if not checkDB(file):
        return False
    
    table_name = input("Table Name: ").lower()

    if checkTable(file, table_name):
        print("table already exists")
        return False
    columns = int(input("Number of Columns: "))

    if columns < 1: 
        return "Table must have at least one column"
    
    print("connect:"+data_folder+file)
    static_db = sqlite3.connect(data_folder+file)
    try:
        cur = static_db.cursor()

        create_table_string = "CREATE TABLE "+table_name+"("
        
        for column in range(columns):
            get_name = getName()
            get_type = getType()

            if column == columns - 1:
                create_table_string += get_name + ' ' + get_type + ')'
            else:
                create_table_string += get_name + ' ' + get_type + ', '

        cur.execute(create_table_string)
        static_db.commit()
        static_db.close()
        addToTable(file, table_name)

    except:
        static_db.close()

def dropTable(file, table_name):
    if not checkDB(file):
        print("file doesn't exist")
        return False
    else:
        if not checkTable(file, table_name):
            print("table doesn't exist")
            return False
    static_db = sqlite3.connect(data_folder+file)
    try:
        cur = static_db.cursor()

        cur.execute("DROP TABLE {}".format(table_name))
        static_db.commit()
        static_db.close()
    except:
        static_db.close()
#######################
'END CREATE/DROP TABLE'
#######################


# START FLASK SESSION

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'env/data'
app.config['SECRET_KEY'] = 'sk' # flash

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods = ['GET', 'POST'])
def index():
    try:

        if request.method == 'GET':
            # get_input = input("What table do you want?")
            if request.args.get('createTable'):
                # print("create")
                createTable(db)
                # return redirect("/table")
            elif request.args.get('popTable'):
                get_table = input("Table Name: ")
                addToTable(db,get_table)
            elif request.args.get('dropTable'):
                print("drop")
                get_table = input ("Table to drop: ")
                dropTable(db,get_table)
            elif request.args.get('showTable'):
                return redirect("/table")
    except Exception as e:
        print(str(exec(e)))
    
    return render_template('/index.html')

@app.route('/table', methods = ['GET', 'POST'])
def show_table():
    title = "raw"
    dir_path = 'env/data'
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        else:
            file = request.files['file']
            if file.filename == '':
                flash('No select file')
            if file:
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                flash('File successfully uploaded')
                return redirect('/table')
            


    elif request.method == 'GET':
        if request.args.get('returnHome'):
            return redirect(url_for('index'))
        
        get_db = request.args.get('requestDB')
        requested_table = request.args.get('requestTable')
        selected_db = session.get('selected_db', None)

        if get_db:
            session['selected_db'] = get_db
            print("selected_db is: "+selected_db)
            tables_list = getTables(selected_db)
            if not checkDB(selected_db):
                return render_template("/table_display.html",table_list = tables_list, db_list = files)
            else:
                try: 
                    return render_template("/table_display.html", 
                            title = title,
                            table_list = tables_list,
                            db_list = files)

                except Exception as e:
                    traceback.print_exc()
                    print(str(e))   
                    return render_template("/table_display.html", table_name = "exception")


       
            
    if requested_table and selected_db:
        print("selected_db is: "+selected_db)
        print("requested_table is: "+requested_table)

        tables_list = getTables(selected_db)
        if not checkTable(selected_db, requested_table):
            print("not checkTable")
            return render_template("/table_display.html",table_list = tables_list, db_list = files)
        else:
            try: 
                print("inside of try")
                data = getTableData(selected_db, requested_table)
                columns, _ , _ = getTableColumnInfo(selected_db, requested_table)
                return render_template("/table_display.html", 
                        title = title,
                        table = requested_table,
                        table_name = requested_table,
                        table_data = data,
                        table_columns = columns,
                        table_list = tables_list,
                        db_list = files)

            except Exception as e:
                traceback.print_exc()
                print(str(e))   
                return render_template("/table_display.html", table_name = "exception")
    
    else: 
        print("Rendering EMPTY TABLE")
        return render_template("/table_display.html",table_list = ["empty table"], db_list = files)

    
        
@app.route('/fetch-table-data', methods=['GET'])
def fetch_table_data():
    # Your server-side logic to retrieve and return table data goes here
    # You can access the selected database and table values using request.args
    selected_db = request.args.get('requestDb')
    selected_table = request.args.get('requestTable')

    # Perform database queries or other processing based on the selected values
    # ...

    # Return a JSON response with the data you want to send back to the client
    response_data = {"message": "Data fetched successfully", "tableData": ...}
    print(response_data)
    return jsonify(response_data)

    
# @app.route('/table_query', methods = ['GET', 'POST'])
# def display_table(table):
#     # if request.method == 'POST': 

#     #     if 'drop' in request.form:
#     #         print("show table")
#     #         drop_table = request.form['drop']
#     #         if checkTable(db, drop_table):
#     #             dropTable(db, drop_table)
#     #     if 'show' in request.form:
#     #         table_name = request.form['show']

#     if request.method == 'GET':
#         if request.args.get('createTable'):
#             print("create")
#             create_table(db)
#         elif request.args.get('dropTable'):
#             print("drop")
#         elif request.args.get('showTable'):
#             show_table()

    
#     return render_template("/table.html")


if __name__ == '__main__':
    app.run(debug=True)
    
