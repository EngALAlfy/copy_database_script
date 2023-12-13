import mysql.connector

#################################
#                               #
#                               #
#                               #
#################################

REMOTE_HOST = "hurryapps.com"
REMOTE_USER = "hurryapps_admin"
REMOTE_PASSWORD = "wdv4@Eq#!TPU"
REMOTE_DATABASE_NAME = "hurryapps_admin_nvbktr7fbv"

LOCAL_HOST = ""
LOCAL_USER = ""
LOCAL_PASSWORD = ""
LOCAL_DATABASE_NAME = ""

def dump_table_structure(cursor, table_name):
        # Retrieve the table structure using a SHOW CREATE TABLE query
        query = f"SHOW CREATE TABLE {table_name}"
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        # The second element of the result contains the CREATE TABLE statement
        create_table_statement = result[1]

        print(f"Table structure for {table_name}:\n")
        print(create_table_statement)


try:
    # Connect to the remote database
    remote_db = mysql.connector.connect(
        host=REMOTE_HOST,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        database=REMOTE_DATABASE_NAME
    )

    # Connect to the local database
    # local_db = mysql.connector.connect(
    #     host=LOCAL_HOST,
    #     user=LOCAL_USER,
    #     password=LOCAL_PASSWORD,
    #     database=LOCAL_DATABASE_NAME
    # )

    # Create a cursor
    cursor = remote_db.cursor()

    # Disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    # Execute the query to get all tables
    cursor.execute("SHOW TABLES")

    # Fetch all the tables as a list
    tables = cursor.fetchall()

    # Convert the list of tuples to a list of strings
    tables = [table[0] for table in tables]

    dump_table_structure(cursor=cursor , table_name=tables[0])
except mysql.connector.Error as err:
    print(f"Error: {err}")
else:
    # Enable foreign key checks (don't forget to do this after your operations)
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    # Close the cursor and the connection
    cursor.close()
    remote_db.close()

# Print the list of tables
print(tables)