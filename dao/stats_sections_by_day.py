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

class SectionsByDayDAO:
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
            rday[query[0]] = cursor.fetchone()[0]
            result.append(rday[query[0]])
            
        return rday


    def getSectionCountUsingYear(self, year):
#       cursor = self.conn.cursor()
        year = "'" + year + "'"
#       print(debug,"before query:", year, type(year))
        query_l = ("L", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%L%'"))
        query_m = ("M", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%M%'"))
        query_w = ("W", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%W%'"))
        query_j = ("J", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%J%'"))
        query_v = ("V", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%V%'"))
        query_s = ("S", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%S%'"))
        query_d = ("D", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s) WHERE cdays LIKE %s" % (str(year), "'%D%'"))

        query_list = [query_l, query_m, query_w, query_j, query_v, query_s, query_d]
#       query_list = [query_l]
        result = []
        rday = {}
#       print(debug, "query list:", query_list)
        

        for query in query_list:
            cursor = self.conn.cursor()
#           print(debug, "query:", query)
            cursor.execute(query[1])
            rday[query[0]] = cursor.fetchone()[0]
            result.append(rday[query[0]])
#           print(debug, "after cursor.execute:", year, rday)
            cursor.close()
#       print(debug, "after query:", year, "type:", type(year))
            
        return rday


    def getSectionCountUsingSemester(self, semester):
#       cursor = self.conn.cursor()
        semester = "'" + semester + "'"
#       print(debug,"before query:", semester, type(semester))
        query_l = ("L", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%L%'"))
        query_m = ("M", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%M%'"))
        query_w = ("W", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%W%'"))
        query_j = ("J", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%J%'"))
        query_v = ("V", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%V%'"))
        query_s = ("S", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%S%'"))
        query_d = ("D", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE semester LIKE %s) WHERE cdays LIKE %s" % (str(semester), "'%D%'"))

        query_list = [query_l, query_m, query_w, query_j, query_v, query_s, query_d]
        result = []
        rday = {}
#       print(debug, "query list:", query_list)
        

        for query in query_list:
            cursor = self.conn.cursor()
#           print(debug, "query:", query)
            cursor.execute(query[1])
            rday[query[0]] = cursor.fetchone()[0]
            result.append(rday[query[0]])
#           print(debug, "after cursor.execute:", semester, rday)
            cursor.close()
#       print(debug, "after query:", semester, "type:", type(semester))
            
        return rday


    def getSectionCountUsingYearSemester(self, year, semester):
        year = "'" + year + "'"
        semester = "'" + semester + "'"
        query_l = ("L", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%L%'"))
        query_m = ("M", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%M%'"))
        query_w = ("W", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%W%'"))
        query_j = ("J", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%J%'"))
        query_v = ("V", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%V%'"))
        query_s = ("S", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%S%'"))
        query_d = ("D", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%D%'"))

        query_list = [query_l, query_m, query_w, query_j, query_v, query_s, query_d]
        result = []
        rday = {}

        for query in query_list:
            cursor = self.conn.cursor()
            cursor.execute(query[1])
            rday[query[0]] = cursor.fetchone()[0]
            result.append(rday[query[0]])
            cursor.close()

#       print(debug, "year & semester", result)
            
        return rday


    def getSectionCountUsingParameter(self, year, semester):
        if year:
            year = "'" + year + "'"
        else:
            year = 'NULL'
        if semester:
            semester = "'" + semester + "'"
        else:
            semester = 'NULL'

        days_sub = ["'%L%'", "'%M%'", "'%W%'", "'%J%'", "'%V%'", "'%S%'", "'%D%'", ]
        print("days:", days_sub[6][2])

        query_l = ("L", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE (%s IS NULL OR years LIKE %s) AND (%s IS NULL OR semester LIKE %s)) WHERE cdays LIKE %s" % (str(year), year, str(semester), str(semester), "'%L%'"))
        query_m = ("M", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%M%'"))
        query_w = ("W", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%W%'"))
        query_j = ("J", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%J%'"))
        query_v = ("V", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%V%'"))
        query_s = ("S", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%S%'"))
        query_d = ("D", "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE years LIKE %s AND semester LIKE %s) WHERE cdays LIKE %s" % (str(year), str(semester), "'%D%'"))

        result = []
        rday = {}

        for day in days_sub:
            main_query = "SELECT COUNT(cdays) FROM (SELECT * FROM section NATURAL INNER JOIN meeting WHERE (%s IS NULL OR years LIKE %s) AND (%s IS NULL OR semester LIKE %s)) WHERE cdays LIKE %s" % (year, year, semester, semester, "'%" + day[2]  + "%'")
            cursor = self.conn.cursor()
            cursor.execute(main_query)
            rday[day[2]] = cursor.fetchone()[0]
            result.append(rday[day[2]])
            cursor.close()

#       query_list = [query_l, query_m, query_w, query_j, query_v, query_s, query_d]
        query_list = [query_l]

#       for query in query_list:
#           cursor = self.conn.cursor()
#           cursor.execute(query[1])
#           rday[query[0]] = cursor.fetchone()[0]
#           result.append(rday[query[0]])
#           cursor.close()

#       print(debug, "year & semester", result)
            
        return rday

