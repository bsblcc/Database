use mydb;

delimiter //
drop procedure if exists add_dishes //
create procedure add_dishes(in account varchar(50), in restName varchar(50), in disName varchar(50), in price int, in kind varchar(50))

	begin
    
        declare id int;
		start transaction;
        
        
        
        select rid into id
        from restaurant
        where restaurant.Person_account = account and restaurant.name = restName;
        
        
        
        insert into dishes (name, price, kind, restaurant_rid)
        values (disName, price, kind, id);
        
        
        commit;
	end//
    
delimiter ;