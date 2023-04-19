CREATE USER IF NOT EXISTS 'replica_user' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT SELECT ON mysql.* TO 'holberton_user'@'localhost';
GRANT REPLICATION SLAVE ON tyrell_corp.* TO 'replica_user';
