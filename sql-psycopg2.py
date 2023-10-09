import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the Artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the Name column from the artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only Queen from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s',  ["Queen"])

# query 4 - select only by "ArtistId" #51 from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 select only he albums with ArtistId #51 on the album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 - select all tracks where the composer is Queen from Track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result ( single )
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
