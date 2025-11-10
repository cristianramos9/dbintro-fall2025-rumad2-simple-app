import csv
import json
from pprint import pprint

import psycopg2

# change PRODUCTION to 1 to use Heroku
PRODUCTION = 0
DEBUG = 0

# =========================================================
# EXTRACT DATA ============================================
# =========================================================

# read the data from already processed source files (in csv format)

def extractToDictFrom(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_data = csv.DictReader(file)

        # extract columns as list of keys
        csv_keys = csv_data.fieldnames
        if not DEBUG:
            print("===KEYS===========================")
            print("type:", type(csv_keys), "\nvalue:", csv_keys, "\nlenght:", len(csv_keys))

        records = []

        # read each record from the extracted data
        for record in csv_data:
            # save each record to a list
            records.append(record)

    return records



class_records = extractToDictFrom('class.csv')
meeting_records = extractToDictFrom('meeting.csv')
requisite_records = extractToDictFrom('requisite.csv')
room_records = extractToDictFrom('room.csv')
section_records = extractToDictFrom('section.csv')

if DEBUG:
    print("===CLASS_RECORDS===========================")
    print(class_records)
    print("Total class records:", len(class_records))

if DEBUG:
    print("===MEETING_RECORDS===========================")
    print(meeting_records)
    print("Total meeting records:", len(meeting_records))
    print(meeting_records[3]['starttime'], ":", type(meeting_records[3]['starttime']))

if DEBUG:
    print("===REQUISITE_RECORDS===========================")
    print(requisite_records)
    print("Total requisite records:", len(requisite_records))

if DEBUG:
    print("===ROOM_RECORDS===========================")
    print(room_records)
    print("Total room records:", len(room_records))

if DEBUG:
    print("===SECTION_RECORDS===========================")
    print(section_records)
    print("Total section records:", len(section_records))


# =========================================================
# LOAD DATA ===============================================
# =========================================================

# load the extracted data to the database
debug = "DEBUG:"
print("===DATABASE======================================")
if not PRODUCTION:
    db_info_path = "../ReadMe.docker"
    print(debug, "==> Reading Docker credentials.")
else:
    db_info_path = "../ReadMe"
    print(debug, "==> Reading Heroku credentials.")
    
with open(db_info_path, mode='r', encoding='utf-8') as file:
    credentials = json.load(file)

# prepare connection url using credentials
db_credentials = f"dbname={credentials['database']} \
                   user={credentials['user']} \
                   password={credentials['password']} \
                   host={credentials['host']} \
                   port={credentials['port']}"

if not DEBUG:
    # verify connection to database by getting its version
    def getInfo():
        conn = psycopg2.connect(db_credentials)
        cursor = conn.cursor()

        cursor.execute("SELECT version()")

        db_ver = cursor.fetchone()
        print("Database version:", db_ver)

        cursor.close()
        conn.close()

    # Get database version
    getInfo()

# drop all tables stored in a list
def dropTables(table_list: list):
    conn = psycopg2.connect(db_credentials)

    # iterate through table list
    for table in table_list:
        if table == "":
            # ignore if empty
            continue
        else:
            cursor = conn.cursor()
            query = f"DROP TABLE IF EXISTS {table};"
            cursor.execute(query)
#            print(cursor.statusmessage)
            cursor.close()
            # commit changes
            conn.commit()

    conn.close

# create tables from the schema list
def createTablesFrom(schema_list: list):
    conn = psycopg2.connect(db_credentials)

    # iterate through schema list
    for schema in schema_list:
        if schema == "":
            # ignore if empty
            continue
        else:
            cursor = conn.cursor()
            query = f"CREATE TABLE IF NOT EXISTS {schema};"
            cursor.execute(query)
#            print(cursor.statusmessage)
            cursor.close()
            # commit changes
            conn.commit()

    conn.close

def insertDataInto(table_name: str, data_to_insert: list):
    conn = psycopg2.connect(db_credentials)
    insert_table = ""
    insert_values = ()

    # iterate through schema list
    for record in data_to_insert:
        if table_name == "":
            # ignore if empty
            continue
        elif table_name == 'class':
            # prepare class
            insert_table = "class (cid, cname, cdesc, term, years, cred, ccode, csyllabus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            insert_values = (record['cid'], \
                             record['cname'], \
                             record['cdesc'], \
                             record['term'], \
                             record['years'], \
                             int(record['cred']), \
                             record['ccode'], \
                             record['csyllabus'])

        elif table_name == 'meeting':
            due_date = "2025-11-01 "
            record['starttime'] = f"{due_date}{record['starttime']}"
            record['endtime'] = f"{due_date}{record['endtime']}"
            
#           print(debug, record['starttime'], "is a", type(record['starttime']))
#           print(debug, record['endtime'], "is a", type(record['endtime']))

            # prepare class
            insert_table = "meeting (mid, ccode, starttime, endtime, cdays) VALUES (%s, %s, %s, %s, %s)"
            insert_values = (record['mid'], \
                             record['ccode'], \
                             record['starttime'], \
                             record['endtime'], \
                             record['cdays'])

        elif table_name == 'requisite':
            # prepare class
            insert_table = "requisite (classid, reqid, prereq) VALUES (%s, %s, %s)"
            insert_values = (record['classid'], \
                             record['reqid'], \
                             record['prereq'])

        elif table_name == 'room':
            # prepare class
            insert_table = "room (rid, building, room_number, capacity) VALUES (%s, %s, %s, %s)"
            insert_values = (record['rid'], \
                             record['building'], \
                             record['room_number'], \
                             int(record['capacity']))

        elif table_name == 'section':
            # prepare class
            insert_table = "section (sid, roomid, mid, cid, semester, years, capacity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_values = (record['sid'], \
                             int(record['roomid']), \
                             int(record['mid']), \
                             int(record['cid']), \
                             record['semester'], \
                             record['years'], \
                             int(record['capacity']))

        cursor = conn.cursor()
        query = f"INSERT INTO {insert_table};"
        cursor.execute(query, insert_values)
#        print(cursor.statusmessage)
        cursor.close()
        # commit changes
        conn.commit()

    conn.close

schema_class = "class (cid SERIAL PRIMARY KEY, \
                       cname VARCHAR, \
                       ccode VARCHAR, \
                       cdesc VARCHAR, \
                       term VARCHAR, \
                       years VARCHAR, \
                       cred INT, \
                       csyllabus VARCHAR)"
schema_meeting = "meeting (mid SERIAL PRIMARY KEY, \
                           ccode VARCHAR, \
                           starttime TIMESTAMP, \
                           endtime TIMESTAMP, \
                           cdays VARCHAR(5))"
schema_requisite = "requisite (classid INTEGER REFERENCES class(cid), \
                               reqid INTEGER REFERENCES class(cid), \
                               prereq BOOLEAN, \
                               PRIMARY KEY (classid, reqid))"
schema_room = "room (rid SERIAL PRIMARY KEY, \
                     building VARCHAR, \
                     room_number VARCHAR, \
                     capacity INT)"
schema_section = "section (sid SERIAL PRIMARY KEY, \
                           roomid INTEGER REFERENCES room(rid), \
                           cid INTEGER REFERENCES class(cid), \
                           mid INTEGER REFERENCES meeting(mid), \
                           semester VARCHAR, \
                           years VARCHAR, \
                           capacity INT)"

schemas = [schema_class, schema_meeting, schema_requisite, schema_room, schema_section]
tables = ['requisite', 'section', 'class', 'meeting', 'room']

dropTables(tables)
createTablesFrom(schemas)
insertDataInto('class', class_records)
insertDataInto('meeting', meeting_records)
insertDataInto('requisite', requisite_records)
insertDataInto('room', room_records)
insertDataInto('section', section_records)


