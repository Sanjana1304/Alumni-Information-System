## Database - MySQL

- Database Name : Alumni_information_system
- Tables : 4
  - alumni_table
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| S_NO             | int(11)      | NO   | PRI | NULL    | auto_increment |
| USER_ID          | varchar(50)  | NO   |     | NULL    |                |
| Name             | varchar(30)  | YES  |     | NULL    |                |
| E_mail           | varchar(30)  | YES  |     | NULL    |                |
| Mobile_no        | int(11)      | YES  |     | NULL    |                |
| Joined_SV        | int(11)      | YES  |     | NULL    |                |
| Left_SV          | int(11)      | YES  |     | NULL    |                |
| DOB              | date         | YES  |     | NULL    |                |
| Marital_status   | varchar(20)  | YES  |     | NULL    |                |
| Proffession      | varchar(40)  | YES  |     | NULL    |                |
| Address_line1    | varchar(50)  | YES  |     | NULL    |                |
| Address_line2    | varchar(50)  | YES  |     | NULL    |                |
| Address_line3    | varchar(50)  | YES  |     | NULL    |                |
| Life_After_SV    | varchar(100) | YES  |     | NULL    |                |
| Memories_from_SV | varchar(100) | YES  |     | NULL    |                |
| Password         | varchar(20)  | YES  |     | NULL    |                |
| USER_TYPE        | varchar(50)  | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
  - forum
  - event
  - reply_forum
