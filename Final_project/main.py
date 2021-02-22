import pymysql

db = pymysql.connect(host='localhost', user='root', password='user1', db='assignment3')

cur = db.cursor()

# Note: Please, Create the database and execute this code, otherwise you get an error
# You may use the test.py to create the database

# Tables customer, water_meter, meter_reader and bill

cur.execute("""CREATE TABLE IF NOT EXISTS `Customer` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS `water_meter` (
  `id` INT NOT NULL,
  `customerID` INT NOT NULL,
  `issueDate` DATETIME NULL,
  `expiryDate` DATETIME NULL,
  `supply` TINYINT NULL,
  `serviceAddress` VARCHAR(45) NULL,
  PRIMARY KEY (`id`, `customerID`),
  INDEX `cus_fk_id_idx` (`customerID` ASC) VISIBLE,
  CONSTRAINT `cus_fk_id`
    FOREIGN KEY (`customerID`)
    REFERENCES `Customer` (`id`));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS `meter_reader` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
""")

cur.execute("""CREATE TABLE IF NOT EXISTS `bill` (
  `id` INT NOT NULL,
  `amount` INT NULL,
  `units` INT NULL,
  `issueDate` DATETIME NULL,
  `dueDate` DATETIME NULL,
  `payment_method` VARCHAR(20) NULL,
  `meter_reader_id` INT NOT NULL,
  `meter_id` INT NOT NULL,
  PRIMARY KEY (`id`, `meter_reader_id`, `meter_id`),
  INDEX `meter_id_idx` (`meter_id` ASC) VISIBLE,
  INDEX `meter_reader_idx` (`meter_reader_id` ASC) VISIBLE,
  CONSTRAINT `meter_id`
    FOREIGN KEY (`meter_id`)
    REFERENCES `water_meter` (`id`),
  CONSTRAINT `meter_reader`
    FOREIGN KEY (`meter_reader_id`)
    REFERENCES `meter_reader` (`id`));
""")

# insert generic data information into MeterReader table 5 Meter reader
cur.execute("insert ignore into assignment3.meter_reader values(1, 'Reader1');")
cur.execute("insert ignore into assignment3.meter_reader values(2,'Reader2');")
cur.execute("insert ignore into assignment3.meter_reader values(3,'Reader3');")
cur.execute("insert ignore into assignment3.meter_reader values(4,'Reader4');")
cur.execute("insert ignore into assignment3.meter_reader values(5, 'Reader5');")

# insert generic data information into customer table 5 existing customer in total
cur.execute("insert ignore into assignment3.customer values(1,'Customer 1','2 Blecker St, London');")
cur.execute("insert ignore into assignment3.customer values(2,'Customer 2','23 Country St. Birmingam');")
cur.execute("insert ignore into assignment3.customer values(3,'Customer 3','45 11th St. Cardiff');")
cur.execute("insert ignore into assignment3.customer values(4,'Customer 4','42 12th St. Newport');")
cur.execute("insert ignore into assignment3.customer values(5,'Customer 5','51 5th St. Cardiff');")

# insert generic data into Water Meters
cur.execute(
    "insert ignore into assignment3.water_meter values( 1,5, '2020-01-01 00:00:00','2020-09-01 00:00:00', true, "
    "'51 5th St. Cardiff');")
cur.execute(
    "insert ignore into assignment3.water_meter values(2, 4, '2020-02-01 00:00:00','2020-08-01 00:00:00', true, "
    "'42 12th St. Newport');")
cur.execute(
    "insert ignore into assignment3.water_meter values(3, 2, '2020-03-01 00:00:00','2020-10-01 00:00:00', true, "
    "'23 Country St. Birmingam');")
cur.execute(
    "insert ignore into assignment3.water_meter values(4, 3, '2020-06-01 00:00:00','2020-12-01 00:00:00', true, "
    "'45 11th St. Cardiff');")
cur.execute(
    "insert ignore into assignment3.water_meter values(5, 1, '2020-09-01 00:00:00','2020-11-01 00:00:00', true, "
    "'2 Blecker St, London');")

# This year reading data.
cur.execute(
    "insert ignore into assignment3.water_meter values(6, 1, '2021-01-01 00:00:00','2021-09-01 00:00:00', true, "
    "'3 Blecker St, London');")
cur.execute(
    "insert ignore into assignment3.water_meter values(7, 1, '2021-01-11 00:00:00','2021-06-01 00:00:00', true, "
    "'4 Blecker St, London');")
cur.execute(
    "insert ignore into assignment3.water_meter values(8, 1, '2021-01-12 00:00:00','2021-04-01 00:00:00', true, "
    "'5 Blecker St, London');")

# insert generic data Bills .
cur.execute(
    "insert ignore into assignment3.bill values (1, 2500, 250, '2020-09-02 00:00:00','2020-09-15 00:00:00', 'cash', "
    "1, 2);")
cur.execute(
    "insert ignore into assignment3.bill values (2, 400, 40, '2020-08-02 00:00:00','2020-08-15 00:00:00', 'card', "
    "2, 1);")
cur.execute(
    "insert ignore into assignment3.bill values (3, 3000, 30, '2020-09-01 00:00:00','2020-09-15 00:00:00', '', 3, 3);"
)
cur.execute(
    "insert ignore into assignment3.bill values (4, 25000, 250, '2020-07-03 00:00:00','2020-07-15 00:00:00', "
    "'cash', 4, 5);")
cur.execute(
    "insert ignore into assignment3.bill values (5, 5000, 250, '2020-08-04 00:00:00','2020-08-15 00:00:00', "
    "'paypal', 5, 4);")

cur.execute(
    "insert ignore into assignment3.bill values (6, 6000, 350, '2021-01-13 00:00:00','2021-03-15 00:00:00', "
    "'paypal', 1, 6);")
cur.execute(
    "insert ignore into assignment3.bill values (7, 7000, 450, '2021-01-13 00:00:00','2021-03-15 00:00:00', "
    "'paypal', 1, 7);")
cur.execute(
    "insert ignore into assignment3.bill values (7, 8000, 550, '2021-01-13 00:00:00','2021-04-15 00:00:00', "
    "'paypal', 1, 8);")

# Saving all the data to the database
db.commit()

# Queries

# 1. This query is to fetch the bill amount and meter name to determine the bills sent to a specific person.
cur.execute("Select mr.name, b.id, b.amount from bill b join meter_reader mr on mr.id=b.meter_reader_id;")
print(cur.fetchall())

# 2. This query is to check for the history of water meter to check the issuance of water meter and get information
# details of all the bills and their amounts.
cur.execute("Select wm.id,wm.issueDate, b.id, b.amount from bill b join water_meter wm on wm.id=b.meter_id;")
print(cur.fetchall())

# This query is to fetch the information on how many readings a meter reader has done.
cur.execute(
    "Select mr.id,mr.name, count(*) from meter_reader mr join bill b on mr.id=b.meter_reader_id group by mr.id;")
print(cur.fetchall())
# 4. This is to fetch the complete information of the meter, it is issuance date and the total bills created on any
# meter.
cur.execute(
    "Select wm.id, wm.issueDate, count(*) from bill b join water_meter wm on wm.id=b.meter_id group by wm.id,"
    "wm.issueDate;")
print(cur.fetchall())

# 5. This is the list of customers who has a meter connection with WASA (Water supplying company)
cur.execute(
    "select * from customer where id in (Select distinct(customerID) from water_meter);")
print(cur.fetchall())

# 6. This is the list of all the meters whose bill has been generated in the system.
cur.execute(
    "select * from customer water_meter where id in (Select distinct(meter_id) from bill);")
print(cur.fetchall())

# View
# This is to get the count of total meters issued on monthly basis
cur.execute("Create view meterCount_view as select left(issuedate,7), count(*) from bill group by 1;")
db.commit()

cur.execute("select * from meterCount_view;")
print(cur.fetchall())

# This is to get the information of units consumed monthly after the month of Jan 2020 now onwards.
cur.execute(
    "Create view readingHistory_view as select left(issuedate,7), units from bill where left(issuedate,7)>='2020-01';")
db.commit()
cur.execute(
    "Select * from readingHistory_view;")
print(cur.fetchall())

# closing connection
db.close()
