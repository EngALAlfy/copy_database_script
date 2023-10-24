import mysql.connector

#################################
#                               #
#                               #
#                               #
#################################

REMOTE_HOST = "136.243.174.222"
REMOTE_USER = "hurryapps_admin"
REMOTE_PASSWORD = "wdv4@Eq#!TPU"
REMOTE_DATABASE_NAME = "hurryapps_admin_nvbktr7fbv"

LOCAL_HOST = ""
LOCAL_USER = ""
LOCAL_PASSWORD = ""
LOCAL_DATABASE_NAME = ""


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