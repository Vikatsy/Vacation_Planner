import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "Vacation.db"
 
    sql_create_Projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_Flights_table = """CREATE TABLE IF NOT EXISTS flights (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    airline text NOT NULL,
                                    departureStation text NOT NULL,
                                    arrivalStation text NOT NULL,
                                    departureDateTime text NOT NULL,
                                    currencyCode text NOT NULL,
                                    basePrice integer NOT NULL,
                                    discountedPrice integer NOT NULL,
                                    administrationFeePrice integer NOT NULL,
                                    project_id integer NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects( id)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_Projects_table)
        # create flights table
        create_table(conn, sql_create_Flights_table)
    else:
        print("Error! cannot create the database connection.")


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO flightss(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_flight(conn, flight):
    """
    Create a new task
    :param conn: db connection
    :param flight: ScheduledFlight
    :return:
    """
 
    sql = ''' INSERT INTO flights(airLine, departureStation, arrivalStation, departureDateTime, 
    					  currencyCode, basePrice, discountedPrice, discountedPrice,administrationFeePrice)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    flight_values = (flight.airLine, flight.flightNumber, flight.departureStation, flight.arrivalStation, flight.departureDateTime, 
            flight.currencyCode, flight.basePrice, flight.discountedPrice, flight.administrationFeePrice)
    cur.execute(sql, flight_values)
    return cur.lastrowid

if __name__ == '__main__':
	main()        

 