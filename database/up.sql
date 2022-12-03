
create table medical(
    id int(11) unsigned NOT NULL auto_increment,
    name varchar(255),
    address varchar(255),
    number_phone varchar(255),
    website varchar(255),
    typeID int(11),
    primary key (id)

)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


create table users
(
    telegID  int(11) unsigned NOT NULL,
    username varchar(255),
    name varchar(255),
    PRIMARY KEY (telegID)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;