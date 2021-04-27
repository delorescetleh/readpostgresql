#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="chirpstack_as_events", user="chirpstack_as_events",
                        password="dbpassword", host="127.0.0.1", port="5432")
print("Open database successfully")

# cur = conn.cursor()
# mydata = {"test": 123}
# cur.execute('''insert into LORADATA (TIMESTAMP,DATA) values  (NOW(),"12345");''')
# print("Table created successfully")

conn.commit()
conn.close()
