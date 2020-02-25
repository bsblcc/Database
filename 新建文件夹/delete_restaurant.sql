use mydb;

delimiter //
drop procedure if exists delete_restaurant //
create procedure delete_restaurant(in account varchar(50), in name varchar(50))

	begin
		declare cnt int;
        declare id int;
		start transaction;
        
        select rid into id
        from restaurant
        where restaurant.Person_account = account and restaurant.name = name;
        
        
        select count(*) into cnt
        from indent
        where indent.Restaurant_RID = id and indent.finished = 0;
        
        
        if cnt = 0 then
			delete from restaurant
			where restaurant.rid = id;
        
			commit;
		else
			
            rollback;
			
		end if;
	end//
    
delimiter ;