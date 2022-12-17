/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - mychat
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`mychat` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mychat`;

/*Table structure for table `frds` */

DROP TABLE IF EXISTS `frds`;

CREATE TABLE `frds` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `frds` */

insert  into `frds`(`fid`,`mid`,`uid`,`status`) values (33,2,3,'friend');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `pswd` varchar(50) DEFAULT NULL,
  `stime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`email`,`pswd`,`stime`) values (2,'dwarakha@mail.com','sanoop','Ofline'),(3,'chakku@gmail.com','chakku@123','Ofline'),(4,'arun@gmail.com','arun','Ofline'),(13,'njan@gmail.com','123456789','Ofline');

/*Table structure for table `msg` */

DROP TABLE IF EXISTS `msg`;

CREATE TABLE `msg` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `msg_frm` int(11) DEFAULT NULL,
  `msg_to` int(11) DEFAULT NULL,
  `msg` varchar(500) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `msg` */

insert  into `msg`(`mid`,`msg_frm`,`msg_to`,`msg`,`time`) values (4,2,3,'b','2020-05-03 22:57:39'),(5,3,2,'jj','2020-05-03 23:03:44'),(6,3,2,'b','2020-05-03 23:10:01'),(7,2,3,'jj','2020-05-03 23:59:24'),(8,3,2,'hi','2020-05-04 00:05:20'),(9,3,2,'hi','2020-05-04 00:06:35'),(12,3,2,'hi','2020-05-04 22:39:09'),(13,2,3,'hi','2020-05-04 22:39:53'),(14,3,0,'hi','2020-05-04 22:40:06'),(15,2,3,'hi','2020-05-04 22:40:16'),(20,3,0,'hi','2020-05-04 23:02:57'),(21,3,0,'hi','2020-05-04 23:02:57'),(22,2,3,'hil','2020-05-04 23:02:57'),(23,3,0,'hi','2020-06-06 10:47:54'),(24,2,0,'b','2020-06-09 21:08:42');

/*Table structure for table `profile` */

DROP TABLE IF EXISTS `profile`;

CREATE TABLE `profile` (
  `uid` int(11) NOT NULL,
  `propic` varchar(500) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `mobil` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `bio` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `profile` */

insert  into `profile`(`uid`,`propic`,`mail`,`mobil`,`dob`,`bio`) values (2,'pending','dwarakha@mail.com','9685741230','1999-12-03','My name is sanoop'),(3,'pending','chakku@gmail.com','7515243698','1999-06-15','My name is chakku'),(4,'pending','arun@gmail.com','5856143298','1999-06-14','My name is arun'),(13,'pending','njan@gmail.com','7854129630','1999-06-13','My name is njan  ');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`lid`,`name`,`gender`,`email`) values (2,'Sanoop ps ','Male','dwarakha@mail.com'),(3,'Chakku','Female','chakku@gmail.com'),(4,'Arun','Male','arun@gmail.com'),(13,'njan','Female','njan@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
