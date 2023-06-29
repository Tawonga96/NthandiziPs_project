SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `Citizen`;
DROP TABLE IF EXISTS `Community`;
DROP TABLE IF EXISTS `PoliceStation`;
DROP TABLE IF EXISTS `PoliceOfficer`;
DROP TABLE IF EXISTS `Member`;
DROP TABLE IF EXISTS `Community_leader`;
DROP TABLE IF EXISTS `household`;
DROP TABLE IF EXISTS `HouseMember`;
DROP TABLE IF EXISTS `job_posting`;
DROP TABLE IF EXISTS `subscribe`;
DROP TABLE IF EXISTS `Alert`;
DROP TABLE IF EXISTS `alert_text`;
DROP TABLE IF EXISTS `alert_multimedia`;
DROP TABLE IF EXISTS `Intervention`;
DROP TABLE IF EXISTS `police_intevention`;
DROP TABLE IF EXISTS `community_intervention`;
DROP TABLE IF EXISTS `status`;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `User` (
    `uid` INTEGER(10) NOT NULL,
    `fname` VARCHAR(50) NOT NULL,
    `lname` VARCHAR(50) NOT NULL,
    `pnumber` VARCHAR(15) NOT NULL,
    `password` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50),
    `otp` BOOLEAN NOT NULL,
    `is_active` BOOLEAN NOT NULL,
    `date_joined` DATETIME NOT NULL,
    PRIMARY KEY (`uid`)
);

CREATE TABLE `Citizen` (
    `cid` INTEGER(10) NOT NULL,
    `occupation` VARCHAR(35) NOT NULL,
    PRIMARY KEY (`cid`)
);

CREATE TABLE `Community` (
    `community_id` INTEGER(10) NOT NULL,
    `district` VARCHAR(30) NOT NULL,
    `comm_name` VARCHAR(35) NOT NULL,
    `area` POLYGON,
    `date_added` DATETIME NOT NULL,
    PRIMARY KEY (`community_id`)
);

CREATE TABLE `PoliceStation` (
    `psid` INTEGER(10) NOT NULL,
    `ps_name` VARCHAR(35) NOT NULL,
    PRIMARY KEY (`psid`)
);

CREATE TABLE `PoliceOfficer` (
    `pid` INTEGER(10) NOT NULL,
    `fname` VARCHAR(35) NOT NULL,
    `lname` VARCHAR(35) NOT NULL,
    PRIMARY KEY (`pid`)
);

CREATE TABLE `Member` (
    `mid` INTEGER(10) NOT NULL,
    `cid` INTEGER(10) NOT NULL,
    `community_id` INTEGER(10) NOT NULL,
    `date_joined` DATETIME NOT NULL,
    `left_on` DATETIME,
    `citizen_typ` VARCHAR(35) NOT NULL,
    PRIMARY KEY (`mid`)
);

CREATE TABLE `Community_leader` (
    `leader_id` INTEGER(10) NOT NULL,
    `community_id` INTEGER(10) NOT NULL,
    `elected_on` DATETIME NOT NULL,
    PRIMARY KEY (`leader_id`)
);

CREATE TABLE `household` (
    `hhid` INTEGER(10) NOT NULL,
    `date_added` DATETIME NOT NULL,
    `hh_name` VARCHAR(35) NOT NULL,
    PRIMARY KEY (`hhid`)
);

CREATE TABLE `HouseMember` (
    `hm_id` INTEGER(10) NOT NULL,
    `mid` INTEGER(10) NOT NULL,
    `hhid` INTEGER(10) NOT NULL,
    `date_joined` DATETIME NOT NULL,
    PRIMARY KEY (`hm_id`)
);

CREATE TABLE `job_posting` (
    `posting_id` INTEGER(10) NOT NULL,
    `pid` INTEGER(10) NOT NULL,
    `psid` INTEGER(10) NOT NULL,
    `assigned_on` DATETIME NOT NULL,
    `is_active` BOOLEAN NOT NULL,
    PRIMARY KEY (`posting_id`)
);

CREATE TABLE `subscribe` (
    `subscription_id` INTEGER(10) NOT NULL,
    `psid` INTEGER(10) NOT NULL,
    `community_id` INTEGER(10) NOT NULL,
    `suscribed_on` DATETIME NOT NULL,
    `until` DATETIME,
    PRIMARY KEY (`subscription_id`)
);

CREATE TABLE `Alert` (
    `alert_id` INTEGER(10) NOT NULL,
    `a_time` DATETIME NOT NULL,
    `code` VARCHAR(128) NOT NULL,
    `author` INTEGER(10) NOT NULL,
    `origin` POINT,
    `a_type` VARCHAR(20) NOT NULL,
    `false_alarm` BOOLEAN NOT NULL,
    `voided_by` INTEGER(10) NOT NULL,
    `closed_at` DATETIME,
    `closed_by` INTEGER,
    PRIMARY KEY (`alert_id`)
);

CREATE TABLE `alert_text` (
    `alert_id` INTEGER(10) NOT NULL,
    `message` TEXT NOT NULL,
    PRIMARY KEY (`alert_id`)
);

CREATE TABLE `alert_multimedia` (
    `alert_id` INTEGER(10) NOT NULL,
    `path` INTEGER NOT NULL,
    `ext` VARCHAR(15),
    PRIMARY KEY (`alert_id`)
);

CREATE TABLE `Intervention` (
    `intervention_id` INTEGER(10) NOT NULL,
    `time_initiated` DATETIME NOT NULL,
    `alert_id` INTEGER(10) NOT NULL,
    PRIMARY KEY (`intervention_id`)
);

CREATE TABLE `police_intevention` (
    `intervention_id` INTEGER(10) NOT NULL,
    `initiated_by` INTEGER(10) NOT NULL,
    PRIMARY KEY (`intervention_id`)
);

CREATE TABLE `community_intervention` (
    `intervention_id` INTEGER(10) NOT NULL,
    `initiated_by` INTEGER(10) NOT NULL,
    PRIMARY KEY (`intervention_id`)
);

CREATE TABLE `status` (
    `iStatus` INTEGER(10) NOT NULL,
    `intervention_id` INTEGER(10) NOT NULL,
    `status` TEXT NOT NULL,
    `updated_on` DATETIME NOT NULL,
    PRIMARY KEY (`iStatus`)
);

ALTER TABLE `Citizen` ADD FOREIGN KEY (`cid`) REFERENCES `User`(`uid`);
ALTER TABLE `PoliceOfficer` ADD FOREIGN KEY (`pid`) REFERENCES `User`(`uid`);
ALTER TABLE `Member` ADD FOREIGN KEY (`cid`) REFERENCES `Citizen`(`cid`);
ALTER TABLE `Member` ADD FOREIGN KEY (`community_id`) REFERENCES `Community`(`community_id`);
ALTER TABLE `Community_leader` ADD FOREIGN KEY (`community_id`) REFERENCES `Community`(`community_id`);
ALTER TABLE `Community_leader` ADD FOREIGN KEY (`leader_id`) REFERENCES `Member`(`mid`);
ALTER TABLE `HouseMember` ADD FOREIGN KEY (`mid`) REFERENCES `Member`(`mid`);
ALTER TABLE `HouseMember` ADD FOREIGN KEY (`hhid`) REFERENCES `household`(`hhid`);
ALTER TABLE `job_posting` ADD FOREIGN KEY (`psid`) REFERENCES `PoliceStation`(`psid`);
ALTER TABLE `job_posting` ADD FOREIGN KEY (`pid`) REFERENCES `PoliceOfficer`(`pid`);
ALTER TABLE `subscribe` ADD FOREIGN KEY (`community_id`) REFERENCES `Community`(`community_id`);
ALTER TABLE `subscribe` ADD FOREIGN KEY (`psid`) REFERENCES `PoliceStation`(`psid`);
ALTER TABLE `Alert` ADD FOREIGN KEY (`author`) REFERENCES `Member`(`mid`);
ALTER TABLE `alert_text` ADD FOREIGN KEY (`alert_id`) REFERENCES `Alert`(`alert_id`);
ALTER TABLE `alert_multimedia` ADD FOREIGN KEY (`alert_id`) REFERENCES `Alert`(`alert_id`);
ALTER TABLE `Intervention` ADD FOREIGN KEY (`alert_id`) REFERENCES `Alert`(`alert_id`);
ALTER TABLE `police_intevention` ADD FOREIGN KEY (`initiated_by`) REFERENCES `job_posting`(`posting_id`);
ALTER TABLE `police_intevention` ADD FOREIGN KEY (`intervention_id`) REFERENCES `Intervention`(`intervention_id`);
ALTER TABLE `community_intervention` ADD FOREIGN KEY (`initiated_by`) REFERENCES `Member`(`mid`);
ALTER TABLE `community_intervention` ADD FOREIGN KEY (`intervention_id`) REFERENCES `Intervention`(`intervention_id`);
ALTER TABLE `status` ADD FOREIGN KEY (`intervention_id`) REFERENCES `Intervention`(`intervention_id`);