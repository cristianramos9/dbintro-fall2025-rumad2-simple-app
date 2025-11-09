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

class StatsDAO:
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


    def getSectionCount(self):
        cursor = self.conn.cursor()
        query_l = ("L", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%L%'")
        query_m = ("M", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%M%'")
        query_w = ("W", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%W%'")
        query_j = ("J", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%J%'")
        query_v = ("V", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%V%'")
        query_s = ("S", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%S%'")
        query_d = ("D", "SELECT COUNT(cdays) FROM section NATURAL INNER JOIN meeting WHERE cdays LIKE '%D%'")

        query_list = [query_l, query_m, query_w, query_j, query_v, query_s, query_d]
        result = []
        rday = {}

        for query in query_list:
            cursor.execute(query[1])
            rday[query[0]] = cursor.fetchone()
            result.append(rday[query[0]])
            
        return rday
