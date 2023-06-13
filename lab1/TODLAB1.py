
from sqlite3 import Cursor
import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="TODLAB1"
                        )

cursor = mydb.cursor()

# Create bd
#cursor.execute("Craate database TODLAB1")

# Get all students
#query = ("SELECT * FROM students")

#cursor.execute(query)

#for i in cursor:
#    print(i)

#--------------------------
# Get student with name serhii
#query = ("SELECT * FROM students where name = \"serhii\"")
#cursor.execute(query)

#for i in cursor:
#    print(i)

#------------------------------
# update student
#update_student = """
#UPDATE students
#SET age = %s
#WHERE id= %s
#"""

#new_age = 23

#student_id = 2

#cursor.execute(update_student, (new_age, student_id))
#mydb.commit()

#--------------------------------
# Delete student
#del_stud = """
#DELETE FROM students
#WHERE id = 5
#"""

#cursor.execute(del_stud)
#mydb.commit()

#--------------------
# select with join
#select = """ SELECT students.name, courses.name
#FROM student_courses
#join  students on students.id = student_courses.student_id
#join courses on courses.id = student_courses.course_id; """
  
#cursor.execute(select);

#mydb.commit()

for i in cursor:
  print(i)

cursor.close()
mydb.close()
