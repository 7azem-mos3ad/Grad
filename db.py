import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "datacamp"
)

cursor = db.cursor()

# cursor.execute("DROP TABLE users")

# ## creating the 'users' table again with the 'PRIMARY KEY'
# cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# ## storing values in a variable
# values = ("Hafeez", "hafeez")

# cursor.execute(query, values)

# db.commit()

print(cursor.rowcount, "record inserted")