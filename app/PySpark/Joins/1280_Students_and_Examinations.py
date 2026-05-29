"""Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table. Each row of this table contains the ID and the name of one student in the school.

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table. Each row of this table contains the name of one subject in the school.

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates. Each student from the Students table takes every course from the Subjects table. Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The result format is in the following example.

Example 1:

Input: Students table:

+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:

+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:

+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
Output:

+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
Explanation: The result table should contain all students and all subjects. Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time. Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam. Alex did not attend any exams. John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time."""


from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_session import get_spark

spark = get_spark("1280")


students_data = [
    (1, "Alice"),
    (2, "Bob"),
    (13, "John"),
    (6, "Alex")
]

students_schema = StructType([
    StructField("student_id", IntegerType(), True),
    StructField("student_name", StringType(), True)
])

students_df = spark.createDataFrame(students_data, students_schema)
students_df.show()


subjects_data = [
    ("Math",),
    ("Physics",),
    ("Programming",)
]

subjects_schema = StructType([
    StructField("subject_name", StringType(), True)
])

subjects_df = spark.createDataFrame(subjects_data, subjects_schema)
subjects_df.show()


examinations_data = [
    (1, "Math"),
    (1, "Physics"),
    (1, "Programming"),
    (2, "Programming"),
    (1, "Physics"),
    (1, "Math"),
    (13, "Math"),
    (13, "Programming"),
    (13, "Physics"),
    (2, "Math"),
    (1, "Math")
]

examinations_schema = StructType([
    StructField("student_id", IntegerType(), True),
    StructField("subject_name", StringType(), True)
])

examinations_df = spark.createDataFrame(examinations_data, examinations_schema)
examinations_df.show()


#transformations
examinations_df_renamed = examinations_df.withColumnsRenamed({'student_id': 'st_id', 'subject_name': 'sub_name'})

students_subjects_df = students_df \
    .join(subjects_df)

result_df = students_subjects_df \
    .join(examinations_df_renamed
          , on=((examinations_df_renamed['st_id'] == students_subjects_df['student_id'])
                &
                (examinations_df_renamed['sub_name'] == students_subjects_df['subject_name']))
          , how='left')\
    .withColumn('exam_count',F.when(F.isnull('st_id'),0).otherwise(1))\
    .groupBy('student_id','student_name','subject_name')\
    .agg(F.sum('exam_count').alias('attended_exams'))\
    .orderBy(F.col('student_id').asc(), F.col('student_name').asc())


result_df.show()