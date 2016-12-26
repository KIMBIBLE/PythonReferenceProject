import sqlite3

conn = sqlite3.connect("myDatabase.db")
cursor = conn.cursor()

# insert some data
cursor.execute("""Insert INTO albums
                VALUES('glow', 'Andy Hunter', '12/27/2016',
                       'Xplore Records', 'MP3')"""
               )

# save data to database
conn.commit()

# insert multiple recored using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TF\
Kmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
