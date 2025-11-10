debug = "DEBUG:"
# change PRODUCTION to 1 to read credentials from Heroku
PRODUCTION = 0

if not PRODUCTION:
    print(debug, "==> Using Docker")
    from config.pgconfig_docker import pg_config
else:
    print(debug, "==> Using Heroku")
    print(debug, "Verify import code is uncommented!")
    # from config.pgconfig import pg_config
    
import psycopg2

class MultiRoomClassesDAO:
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

        self.conn = psycopg2.connect(connect_url)

        if not PRODUCTION:
            cursor = self.conn.cursor()
            cursor.execute("SELECT version()")
            db_ver = cursor.fetchone()
            print(debug, "Database version:", db_ver)
            cursor.close()

        
    def getAllMultiRoomClasses(self):
        result = []
        cursor = self.conn.cursor()
        query = "SELECT cid, COUNT(DISTINCT rid) FROM (SELECT class.cid, cname, ccode, rid FROM section INNER JOIN room ON section.roomid = room.rid INNER JOIN class ON section.cid = class.cid) GROUP BY cid ORDER BY cid"

        cursor.execute(query)
#       result = cursor.fetchone()
        for item in cursor:
            result.append(item)

        return result
