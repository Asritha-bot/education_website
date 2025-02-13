import mysql.connector 

mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "asritha@2002" , database = "education_site" )
#print(mydb)
mycursor = mydb.cursor()

# mycursor.execute( "CREATE DATABASE education_site " )

#mydb.commit()

# mycursor.execute("""
#     CREATE TABLE subjects (
#     subject_id INT PRIMARY KEY AUTO_INCREMENT,
#     subject_name VARCHAR(100) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#     )
# """)
# mycursor.execute("""
#     CREATE TABLE lessons (
#         lesson_id INT ,
#         subject_id INT,
#         lesson_number INT NOT NULL,
#         lesson_title VARCHAR(200) NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#         FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
#     )
# """)

# mycursor.execute("""
#     CREATE TABLE Topics_info(
#         subject_id INT,
#         lesson_number INT,
#         Topic_id INT,   
#         Topic_text VARCHAR(200) NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#         FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
#     )
#  """)

# mycursor.execute("""
#     CREATE TABLE Info(
#         subject_id INT,
#         lesson_number INT,
#         Topic_id INT,   
#         Info_text LONGTEXT NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#         FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
#     )
#  """)



# sql = """
#     INSERT INTO lessons (subject_id, lesson_id, lesson_number, lesson_title) 
#     VALUES (%s, %s, %s, %s)
# """

# vals = [
#     (1, 1, 1, 'The Thief Story'),
#     (1, 2, 2,' A Letter to God'),
#     (1, 3, 3, 'The Rattrap'),
#     (1, 4, 4, 'The Hack Driver'),
#     (1, 5, 5, 'The Secret of Health')
# ]

# mycursor.executemany(sql, vals)
# mydb.commit()

# sql = """
#      INSERT INTO lessons (subject_id, lesson_id, lesson_number, lesson_title) 
#      VALUES (%s, %s, %s, %s)
#  """

# vals = [
#      (2, 1, 1, 'Real Numbers'),
#      (2, 2, 2, 'Polynomials'),
#      (2, 3, 3, ' Triangles'),
#      (2, 4, 4, 'Probability'),
#      (2, 5, 5, 'Statistics')
#    ]

# mycursor.executemany(sql, vals)
# mydb.commit()

# sql = """
#      INSERT INTO Topics_info (subject_id, lesson_number, topic_id, topic_text) 
#      VALUES (%s, %s, %s, %s)
#  """

# vals = [
#      (2, 5, 1, 'Exercise-1'),
#      (2, 5, 2, 'Exercise-2'),
#      (2, 5, 3, 'Exercise-3'),

#    ]

# mycursor.executemany(sql, vals)
# mydb.commit()

sql = """
     INSERT INTO info(subject_id, lesson_number, topic_id, Info_text)
     VALUES (%s, %s, %s, %s)
 """
val = (
     2,5,3,
     """"
     ### Exercise 3: Statistics
 
 Here are some typical problems you might encounter in the third exercise of the Statistics chapter for 10th class mathematics:
 
 1. **Ogive (Cumulative Frequency Graph):**
    - Draw an ogive for the given data. For example:
      - Given the class intervals and frequencies, create a cumulative frequency table and draw the ogive.
 
 2. **Mean, Median, and Mode of Grouped Data:**
    - Calculate the mean, median, and mode of grouped data using the appropriate formulas. For example:
      - Find the mean, median, and mode for the following data: Class Intervals: 0-10, 10-20, 20-30, 30-40; Frequencies: 4, 6, 8, 2.
 
 3. **Quartiles and Percentiles:**
    - Calculate the quartiles and percentiles of the given data. For example:
      - Find the first quartile (Q1), third quartile (Q3), and 50th percentile (P50) for the given data set.
 
 4. **Variance and Standard Deviation:**
    - Calculate the variance and standard deviation of a given set of data. For example:
      - Find the variance and standard deviation for the following data: 5, 10, 15, 20, 25.
 
 5. **Comparing Two Data Sets:**
    - Compare two sets of data using measures of central tendency and dispersion. For example:
      - Compare the mean, median, and standard deviation of two different data sets.
 
 Would you like detailed explanations or solutions for any specific type of problem from this exercise? Let me know!
     
     	 """
)
mycursor.execute(sql, val)
mydb.commit()
