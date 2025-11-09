debug = "DEBUG:"
# change PRODUCTION to 1 to read credentials from Heroku
PRODUCTION = 0

if not PRODUCTION:
    print(debug, "==> Using Docker")
    from config.pgconfig_docker import pg_config
else:
    print(debug, "==> Using Heroku")
    print(debug, "Verify import code is uncommented!")
    # from config.pgconfig import pgconfig

import psycopg2

class RequisiteDAO:
    def __init__(self):
        # initialize database
        connect_url = "dbname=%s \
                       user=%s \
                       password=%s \
                       host=%s \
                       port=%s" % \
                      (pg_config['dbname'], \
                       pg_config['user'], \
                       pg_config['password'], \
                       pg_config['host'], \
                       pg_config['port'])

        # connect to database
        self.conn = psycopg2.connect(connect_url)

        # test connection by getting database version
        if not PRODUCTION:
            cursor = self.conn.cursor()
            cursor.execute("SELECT version()")
            db_ver = cursor.fetchone()
            print(debug, "Database version:", db_ver)
            cursor.close()


    def insertRequisite(self, classid, reqid, prereq):
        cursor = self.conn.cursor()
        query = "INSERT INTO requisite (classid, reqid, prereq) VALUES (%s, %s, %s) RETURNING (classid, reqid)"
        cursor.execute(query, (classid, reqid, prereq))

        pk = cursor.fetchone()

        print(debug, "pk", pk, type(pk), len(list(pk)))
        print(debug, "eval(pk[0])", eval(pk[0]), pk[0], type(eval(pk[0])), len(eval(pk[0])))

        self.conn.commit()

        return pk


    def getRequisiteByIDs(self, classid, reqid):
        cursor = self.conn.cursor()
        query = "SELECT classid, reqid, prereq FROM requisite WHERE classid IN (SELECT cid FROM class) AND reqid IN (SELECT cid FROM class) and classid = %s AND reqid = %s"
        cursor.execute(query, (classid, reqid))

        result = cursor.fetchone()
        
        return result


    def deleteRequisiteByIDs(self, classid, reqid):
        cursor = self.conn.cursor()
        query = "DELETE FROM requisite WHERE classid IN (SELECT cid FROM class) AND reqid IN (SELECT cid FROM class) and classid = %s AND reqid = %s"
        cursor.execute(query, (classid, reqid))

        rowcount = cursor.rowcount

        self.conn.commit()

        return rowcount == 1
