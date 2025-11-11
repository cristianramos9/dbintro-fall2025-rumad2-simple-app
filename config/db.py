import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Change: create global variables to use in 'get_conn';
#         this change to make it compatible with files with classes
# To use with Heroku credentials, replace the value of the following 5 variables
cr_docker = "ReadMe.docker"
if os.path.exists(cr_docker):
    print("There is a file!:", cr_docker)
    db_dbname = "rumad2_fase2"
    db_user = "cramos"
    db_password = "uprmrumad2"
    db_host = "localhost"
    db_port = "5432"
else:
    print("FAILED!")
    db_dbname = os.getenv("DB_NAME", "rumad2")
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "postgres")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")

# Change: variable with credentials to be used with files with classes
# When using Heroku, replace the values in pg_config with corresponding variable from above.
# Example: "host" : db_host
pg_config = {
        "dbname"    :   db_dbname,
        "user"      :   db_user,
        "password"  :   db_password,
        "host"      :   db_host,
        "port"      :   db_port
        }
#g_config = {
#       "dbname"    :   "rumad2_fase2",
#       "user"      :   "cramos",
#       "password"  :   "uprmrumad2",
#       "host"      :   db_host,
#       "port"      :   db_port
#       }

# Change: added parameters to 'get_conn', psycopg2 now uses these parameters as argument;
#         this changes makes it compatible with files with classes
def get_conn(conn_dbname=db_dbname, conn_user=db_user, conn_password=db_password, conn_host=db_host, conn_port=db_port):
    # test return
    return psycopg2.connect(
        dbname=conn_dbname,
        user=conn_user,
        password=conn_password,
        host=conn_host,
        port=conn_port
    )

    # original return
#   return psycopg2.connect(
#       host=os.getenv("DB_HOST", "localhost"),
#       port=os.getenv("DB_PORT", "5432"),
#       dbname=os.getenv("DB_NAME", "rumad2"),
#       user=os.getenv("DB_USER", "postgres"),
#       password=os.getenv("DB_PASSWORD", "postgres"),
#   )

def query_one(sql, params=()):
    with get_conn() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql, params)
        return cur.fetchone()

def query_all(sql, params=()):
    with get_conn() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(sql, params)
        return cur.fetchall()

def execute(sql, params=()):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(sql, params)
        return cur.rowcount
