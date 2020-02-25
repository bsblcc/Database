
use mydb;
use mydb;
alter table restaurant
add unique key(person_account, name);
delimiter //
drop procedure if exists get_Self_Indent //
create procedure get_Self_Indent(in account varchar(50))

	begin
		
		drop temporary table if exists Self_Indent;
		create temporary table Self_Indent
        (
			restaurant_rid int,
            time datetime,
            iid int,
            address_address varchar(50),
            address_person_account varchar(50)
        );
        
        insert into Self_Indent(restaurant_rid, time, iid, Address_address, address_person_account)
        select restaurant_rid, time, iid, Address_address, address_person_account
        
        from indent
        where Indent.Address_Person_Account = account;
	end//
    
delimiter ;
    