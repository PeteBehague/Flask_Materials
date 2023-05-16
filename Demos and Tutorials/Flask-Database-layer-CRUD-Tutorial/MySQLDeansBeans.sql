-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: deansbeans
-- ------------------------------------------------------
-- Server version	8.0.13

SET FOREIGN_KEY_CHECKS = 0;
SET NAMES utf8 ;

DROP SCHEMA IF EXISTS `deansbeans` ;
CREATE SCHEMA IF NOT EXISTS `deansbeans` ;
Use `deansbeans` ;
--
-- Table structure for table `colours`
--

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customers` (
  `customerid` int(11) NOT NULL AUTO_INCREMENT,
  `customername` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `addressline1` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `addressline2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `addressline3` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `postcode` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `securityquestion` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `securityquestionanswer` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`customerid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` (`customerid`, `customername`, `addressline1`, `addressline2`, `addressline3`, `postcode`, `phone`, `email`, `securityquestion`, `securityquestionanswer`) VALUES (1,'Billie Blender','1 the High Street','Sunnyville',NULL,'SN1 1TW','01234567890','Billie@Blender.com','Favourite roast','Classic'),(2,'Graham Grounds','3 Reachout Street','Forthestarsto','Berks','FT3 7QE','02456123987','Graham@Grounds.co.uk','Favourite Coffee Additive','Maple Syrup'),(3,'Philippa Filter','33 Loopdloop Road','Inverto','Lancs','IN5 7DD','07555182736','Philippa@Filter.gov','Favourite Style','Americano'),(4,'Kofi Kreme','74 Cirrus Avenue','Clouding','E Sussex','CL9 0PQ','07400563824','Kofi@Kreme.co.uk','A word that rhymes with bean','Sheen');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `degreesofroast`
--

DROP TABLE IF EXISTS `degreesofroast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `degreesofroast` (
  `degreeOfroastid` int(11) NOT NULL AUTO_INCREMENT,
  `roasttype` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`degreeOfroastid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `degreesofroast`
--

LOCK TABLES `degreesofroast` WRITE;
/*!40000 ALTER TABLE `degreesofroast` DISABLE KEYS */;
INSERT INTO `degreesofroast` (`degreeOfroastid`, `roasttype`) VALUES (1,'Raw'),(2,'Light'),(3,'Medium'),(4,'Dark'),(5,'Burnt'),(6,'Cremated');
/*!40000 ALTER TABLE `degreesofroast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `formats`
--

DROP TABLE IF EXISTS `formats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `formats` (
  `formatid` int(11) NOT NULL AUTO_INCREMENT,
  `formatdescription` varchar(50) NOT NULL,
  PRIMARY KEY (`formatid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formats`
--

LOCK TABLES `formats` WRITE;
/*!40000 ALTER TABLE `formats` DISABLE KEYS */;
INSERT INTO `formats` (`formatid`, `formatdescription`) VALUES (1,'Whole Beans'),(2,'Coarse Ground'),(3,'Medium Ground'),(4,'Fine Ground'),(5,'Dust'),(6,'Nespresso (Pod)'),(7,'Dolce Gusto (Pod)'),(8,'Tassimo (Pod)'),(9,'Lavazza (pod)');
/*!40000 ALTER TABLE `formats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderitems`
--

DROP TABLE IF EXISTS `orderitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `orderitems` (
  `orderitemid` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `purchaseprice` decimal(18,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `formatid` int(11) DEFAULT NULL,
  `degreeOfroastid` int(11) DEFAULT NULL,
  PRIMARY KEY (`orderitemid`),
  KEY `FK_orderitems_orders` (`orderid`),
  KEY `FK_orderitems_products` (`productid`),
  KEY `FK_orderitems_formats` (`formatid`),
  KEY `FK_orderitems_degreesOfroast` (`degreeOfroastid`),
  CONSTRAINT `FK_orderitems_degreesOfroast` FOREIGN KEY (`degreeOfroastid`) REFERENCES `degreesofroast` (`degreeOfroastid`),
  CONSTRAINT `FK_orderitems_formats` FOREIGN KEY (`formatid`) REFERENCES `formats` (`formatid`),
  CONSTRAINT `FK_orderitems_orders` FOREIGN KEY (`orderid`) REFERENCES `orders` (`orderid`),
  CONSTRAINT `FK_orderitems_products` FOREIGN KEY (`productid`) REFERENCES `products` (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderitems`
--

LOCK TABLES `orderitems` WRITE;
/*!40000 ALTER TABLE `orderitems` DISABLE KEYS */;
INSERT INTO `orderitems` (`orderitemid`, `orderid`, `productid`, `purchaseprice`, `quantity`, `formatid`, `degreeOfroastid`) VALUES (1,1,1,8.17,1,1,1),(2,1,2,12.00,1,1,5),(3,1,6,5.00,2,9,6),(4,2,2,12.00,6,3,5),(5,2,4,9.95,1,4,2),(6,3,1,8.17,1,4,3),(7,3,10,9.00,2,4,4),(8,3,16,127.49,3,5,2),(9,4,1,8.17,1,6,3),(10,4,7,4.17,2,7,4),(11,4,14,1.99,4,8,2);
/*!40000 ALTER TABLE `orderitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `orders` (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `customerid` int(11) NOT NULL,
  `orderdate` date NOT NULL,
  `ordertotal` decimal(18,2) NOT NULL,
  `orderstatus` int(11) NOT NULL,
  PRIMARY KEY (`orderid`),
  KEY `FK_orders_customers` (`customerid`),
  CONSTRAINT `FK_orders_customers` FOREIGN KEY (`customerid`) REFERENCES `customers` (`customerid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` (`orderid`, `customerid`, `orderdate`, `ordertotal`, `orderstatus`) VALUES (1,1,'2019-06-12',30.17,1),(2,2,'2019-07-01',81.95,2),(3,2,'2019-09-02',408.64,1),(4,2,'2019-10-28',24.47,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `products` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `recommendedretailprice` decimal(18,2) NOT NULL,
  `WholesalePrice` decimal(18,2) NOT NULL,
  `discounttype` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `discountpercentage` int(11) DEFAULT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` (`productid`, `productname`, `description`, `recommendedretailprice`, `WholesalePrice`, `discounttype`, `discountpercentage`) VALUES (1,'Lava Java','Lava Java is made from molten beans generated by geothermal energy and expelled through fractures in planetary crust or eruptions, usually at temperatures from 700 to 1,200 °C (1,292 to 2,192 °F). The structures resulting from subsequent solidification and cooling are then harvested, washed and tumbled before being reconstituted back into beans and then treated like any other bean. Bagged in our own factories. ',8.17,4.05,NULL,NULL),(2,'Arabica Erotica','The queen of coffee, possibly the best aphrodisiac out there. Hint\'s of Dior, Canel, Klien and Versace...',12.00,6.00,'B',NULL),(3,'Old Knobler','Made with a selected single piece of roasted English oak (sustainably resourced).  this solid coffee is both distinctive and durable. Usually grown for it’s cob nuts, the natural beauty and taste hardwood gives to coffee is one of the industy\'s best kept secrets. With a honey coloured hue this light yet strong coffee is a durable accessory long associated with the English countryside. With a complex frame, this coffee is a reliable companion with flavours that last and linger on the tongue. ',11.00,5.59,'P',10),(4,'Justa Robusta','A simple, medium roast robusta coffee. Your stock \"go to\" coffee for your day to day requirements. ',9.95,4.22,'B',NULL),(5,'Robusta Crusta','Puts hairs on your chest (and probably other body parts too)',10.99,5.49,'P',5),(6,'Maple Bacon','If you like bacon, you’ll have to try this lightly roasted coffee drink! Especially geared toward the morning coffee drinker (for those who like their eggs and bacon), this roast comes from Boca Java and has strong piggy bacon overtones. Probably best enjoyed with your fried eggs, beans and toast. These beans are 100% Vegan. ',5.00,2.30,'T',NULL),(7,'Weasel Puke','This one is definitely not for the faint-hearted and the name may already be making you feel a little queasy. These coffee beans are eaten by weasels which leaves a residue in their mouths. This residue is carefully removed (weasels have very sharp teeth), cleansed, roasted and bagged ready for you to enjoy. ',4.17,2.05,'T',NULL),(8,'Old Warthog','Warthog hide is traditionally beaten with hickory sticks before being soaked in a wash of cured leaf juice. You can smell the roasting beans from a good 500 metres away',8.29,4.01,'F',NULL),(9,'Star Wars Vader’s Dark Side','Get in touch with the dark side of the force with this truly dark brew. After one shot of this you\'ll know who your father is.',5.00,2.50,'F',NULL),(10,'Death Wish','One mug of this will fully stoke your anxiety, insomnia, dizziness, digestive system, muscle breakdown, addiction, blood pressure and heart rate, but fatigue will be a thing of the past.',9.00,4.50,NULL,NULL),(11,'Fix','One of the strongest coffees on the market. Never mind the taste, just wait for the caffeine hit...aaahhh',6.95,5.00,NULL,NULL),(12,'Mother’s Little Helper','A strong brew best disguised with a lot of milky froth. Expect hints of quinine, tonic and a dash of lemon.',5.00,2.50,NULL,NULL),(13,'Vanilla Flavored Monkey Spit','Before roasting these beans are sucked on by monkeys and then when they’re finished they spit them out. The beans are then collected and are prized for their spectacular vanilla flavor. The farmer in Taiwan got sick of his beans being eaten by monkeys and so decided to actually try one himself to see what he was missing. Needless to say he liked it, and decided to share Vanilla flavored Monkey Spit Coffee with the world. Enjoy!',5.00,2.50,NULL,NULL),(14,'The Cheap and Nasty','A really cheap and nasty coffee with a really rather alarming after taste. You have been warned',1.99,0.99,NULL,NULL),(16,'Kopi Luwak','Made from the faeces of cats that eat the coffee beans, it contains a bunch of excellent enzymes, supposedly good for you. The poo is washed before it’s roasted and the roasting is done at over 220 Deg C (the raw bean version is still available but not recommended). For poo coffee, it’s really pricey; expect to pay from £30 a cup',127.49,63.99,NULL,NULL),(17,'The Cockney Knees-Up','A brew that\'s guaranteed to get you moving in the same way a good old fashioned sing song in an east-end pub used to do. Hints of apples and pears.',8.00,4.00,NULL,NULL),(18,'Beery Nice Espresso','A medium roasted robusta bean that\'s been boiled and marianated in the finest northern ale. Not to be taken before any kind of car journey if you\'re the one behind the wheel.',8.43,4.22,NULL,NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;


-- Dump completed on 2020-11-09  9:22:03
