CREATE DATABASE IF NOT EXISTS `hackathonmentors`;
CREATE USER IF NOT EXISTS 'hackathonmentors_user'@'%' IDENTIFIED BY 'hackathonmentors_pass';
GRANT ALL PRIVILEGES ON `hackathonmentors`.* to 'hackathonmentors_user'@'%';
FLUSH PRIVILEGES;
