
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
    
use mydb
delimiter //  
drop procedure if exists insert_indent//
create  procedure insert_indent(in Restaurant_RID INT, in Address_address VARCHAR(50), in Address_Person_account VARCHAR(50))

	begin
		declare st time;
        declare et time;
        start transaction;
        insert into  Indent (Indent.Restaurant_RID, Indent.time, Indent.Address_address, Indent.Address_Person_account)
        values (Restaurant_RID, current_time(), Address_address, Address_Person_account);
        
        select start_time, end_time
        into st, et
        from restaurant
        where restaurant.rid = restaurant_rid;
        
        if st > current_time() or et < current_time() then
			rollback;
		end if;
        
        commit;
        
        
        
        
        #update Restaurant
        #set Restaurant.sales = Restaurant.sales + 1, Restaurant.budget = (Restuarant.budget * (sales - 1) + cost ) / sales
        #where Restaurant.RID = Restaurant_RID;
	end//
    
delimiter ;