-- MySQL Script generated by MySQL Workbench
-- 05/12/17 19:34:23
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Person` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Person` (
  `account` VARCHAR(50) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `sex` ENUM('Male', 'Female') NULL DEFAULT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `password` VARCHAR(50) NULL,
  PRIMARY KEY (`account`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Address`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Address` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Address` (
  `address` VARCHAR(50) NOT NULL,
  `Person_account` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`address`, `Person_account`),
  INDEX `fk_Address_Person_idx` (`Person_account` ASC),
  CONSTRAINT `fk_Address_Person`
    FOREIGN KEY (`Person_account`)
    REFERENCES `mydb`.`Person` (`account`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Restaurant`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Restaurant` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Restaurant` (
  `name` VARCHAR(50) NOT NULL,
  `RID` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(45) NOT NULL,
  `cuisines` ENUM('Fast Food', 'Italian', 'Mexico', 'French', 'Japanese', 'Chinese') NULL DEFAULT NULL,
  `budget` DOUBLE NULL DEFAULT 0,
  `Person_account` VARCHAR(50) NOT NULL,
  `start_time` TIME NULL DEFAULT 0,
  `end_time` TIME NULL DEFAULT 0,
  `sales` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`RID`),
  INDEX `fk_Restaurant_Person1_idx` (`Person_account` ASC),
  CONSTRAINT `fk_Restaurant_Person1`
    FOREIGN KEY (`Person_account`)
    REFERENCES `mydb`.`Person` (`account`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Dishes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Dishes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Dishes` (
  `name` VARCHAR(50) NOT NULL,
  `price` INT NOT NULL,
  `kind` VARCHAR(45) NULL DEFAULT NULL,
  `Restaurant_RID` INT NOT NULL,
  `sales` INT NULL DEFAULT 0,
  PRIMARY KEY (`name`, `Restaurant_RID`),
  INDEX `fk_Dishes_Restaurant1_idx` (`Restaurant_RID` ASC),
  CONSTRAINT `fk_Dishes_Restaurant1`
    FOREIGN KEY (`Restaurant_RID`)
    REFERENCES `mydb`.`Restaurant` (`RID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Indent`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Indent` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Indent` (
  `Restaurant_RID` INT NULL,
  `time` DATETIME NOT NULL,
  `IID` INT NOT NULL AUTO_INCREMENT,
  `Address_address` VARCHAR(50) NOT NULL,
  `Address_Person_account` VARCHAR(50) NOT NULL,
  `finished` TINYINT(1) NOT NULL DEFAULT 0,
  INDEX `fk_Person_has_Restaurant_Restaurant1_idx` (`Restaurant_RID` ASC),
  PRIMARY KEY (`IID`),
  INDEX `fk_Indent_Address1_idx` (`Address_address` ASC, `Address_Person_account` ASC),
  CONSTRAINT `fk_Person_has_Restaurant_Restaurant1`
    FOREIGN KEY (`Restaurant_RID`)
    REFERENCES `mydb`.`Restaurant` (`RID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Indent_Address1`
    FOREIGN KEY (`Address_address` , `Address_Person_account`)
    REFERENCES `mydb`.`Address` (`address` , `Person_account`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Indent_has_Dishes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Indent_has_Dishes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Indent_has_Dishes` (
  `Indent_IID` INT NOT NULL,
  `Dishes_name` VARCHAR(50) NOT NULL,
  `Dishes_Restaurant_RID` INT NOT NULL,
  `count` INT NOT NULL,
  PRIMARY KEY (`Indent_IID`, `Dishes_name`, `Dishes_Restaurant_RID`),
  INDEX `fk_Indent_has_Dishes_Dishes1_idx` (`Dishes_name` ASC, `Dishes_Restaurant_RID` ASC),
  INDEX `fk_Indent_has_Dishes_Indent1_idx` (`Indent_IID` ASC),
  CONSTRAINT `fk_Indent_has_Dishes_Indent1`
    FOREIGN KEY (`Indent_IID`)
    REFERENCES `mydb`.`Indent` (`IID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Indent_has_Dishes_Dishes1`
    FOREIGN KEY (`Dishes_name` , `Dishes_Restaurant_RID`)
    REFERENCES `mydb`.`Dishes` (`name` , `Restaurant_RID`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;

USE `mydb` ;

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`Person_Run`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Person_Run` (`account` INT, `name` INT, `sex` INT, `phone_number` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`Restaurant_Open`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Restaurant_Open` (`name` INT, `address` INT, `cuisines` INT, `budget` INT, `Person_account` INT, `sales` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`restaurant_run`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`restaurant_run` (`name` INT, `address` INT, `cuisines` INT, `start_time` INT, `end_time` INT, `sales` INT, `person_account` INT);

-- -----------------------------------------------------
-- View `mydb`.`Person_Run`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `mydb`.`Person_Run` ;
DROP TABLE IF EXISTS `mydb`.`Person_Run`;
USE `mydb`;
CREATE  OR REPLACE VIEW `Person_Run` AS
select Person.account, Person.name, Person.sex, Person.phone_number
from Person;

-- -----------------------------------------------------
-- View `mydb`.`Restaurant_Open`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `mydb`.`Restaurant_Open` ;
DROP TABLE IF EXISTS `mydb`.`Restaurant_Open`;
USE `mydb`;
CREATE  OR REPLACE VIEW `Restaurant_Open` AS
select name , address, cuisines, budget, Person_account, sales
from Restaurant
where current_time() < end_time and start_time < current_time();

-- -----------------------------------------------------
-- View `mydb`.`restaurant_run`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `mydb`.`restaurant_run` ;
DROP TABLE IF EXISTS `mydb`.`restaurant_run`;
USE `mydb`;
CREATE  OR REPLACE VIEW `restaurant_run` AS
select name, address, cuisines, start_time, end_time, sales, person_account
from Restaurant;
USE `mydb`;

DELIMITER $$

USE `mydb`$$
DROP TRIGGER IF EXISTS `mydb`.`Restaurant_BEFORE_INSERT` $$
USE `mydb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `mydb`.`Restaurant_BEFORE_INSERT` BEFORE INSERT ON `Restaurant` FOR EACH ROW
BEGIN

    if new.start_time >= new.end_time then
		set new.person_account = null;
	end if;
    
    
    
END$$


USE `mydb`$$
DROP TRIGGER IF EXISTS `mydb`.`Indent_BEFORE_INSERT` $$
USE `mydb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `mydb`.`Indent_BEFORE_INSERT` BEFORE INSERT ON `Indent` FOR EACH ROW
BEGIN

    
	update Restaurant
    set restaurant.sales = restaurant.sales + 1
    where restaurant.rid = new.restaurant_rid;
END$$


USE `mydb`$$
DROP TRIGGER IF EXISTS `mydb`.`Indent_BEFORE_DELETE` $$
USE `mydb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `mydb`.`Indent_BEFORE_DELETE` BEFORE DELETE ON `Indent` FOR EACH ROW
BEGIN
	delete from Indent_has_Dishes
    where Indent_has_Dishes.Indent_IID = old.IID;
END$$


USE `mydb`$$
DROP TRIGGER IF EXISTS `mydb`.`Indent_has_Dishes_AFTER_INSERT` $$
USE `mydb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `mydb`.`Indent_has_Dishes_AFTER_INSERT` AFTER INSERT ON `Indent_has_Dishes` FOR EACH ROW
BEGIN
    declare p int;
    
	update Dishes
    set Dishes.sales = Dishes.sales + new.count
    where Dishes.name = new.Dishes_name and Dishes.Restaurant_RID = new.Dishes_Restaurant_RID;
    

    
    select Dishes.price into p
    from Dishes
    where Dishes.name = new.Dishes_name and Dishes.Restaurant_RID = new.Dishes_Restaurant_RID;
    
    update Restaurant
    set restaurant.budget = (restaurant.budget * (sales - 1) + new.count * p) / sales
    where restaurant.RID = new.dishes_restaurant_rid;
    
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
