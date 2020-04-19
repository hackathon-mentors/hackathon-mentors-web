CREATE DATABASE `hackathonmentors` IF NOT EXISTS;
CREATE USER 'hackathonmentors_user'@'%' IDENTIFIED BY 'hackathonmentors_pass';
GRANE ALL PRIVILEGES ON `hackathonmentors`.* to 'hackathonmentors_user'@'%';
FLUSH PRIVILEGES;
