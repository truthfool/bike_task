1. Install python in your system
2. Create virtual env using `python -m venv {env_name}`
3. Activate virtual env using `source ./{env_name}/bin/activate`
4. Run `pip install requirements.txt`
5. Install mysql in your system
6. Use the below steps to create DB and user. 
`
To create a user, password, and database in MySQL, you can use the following SQL commands. Note that you should have appropriate privileges to create users and databases.

Login to MySQL:

`mysql -u root -p`

You'll be prompted to enter the root password.

Create a Database:

sql

`CREATE DATABASE your_database_name;`

Replace your_database_name with the desired name for your database.

Create a User:

sql

`CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';`

Replace your_username with the desired username and your_password with the desired password.

Grant Privileges:

sql

`GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';`

This grants all privileges on the specified database to the user.

Flush Privileges and Exit:

sql

`FLUSH PRIVILEGES;`
`EXIT;`

This ensures that the changes take effect, and it exits the MySQL shell.
`

7. Run the python script using `python script.py`. This will ask you the username, password and db name you create in step 