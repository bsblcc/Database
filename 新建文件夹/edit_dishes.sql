use mydb;
delimiter //  
drop procedure if exists edit_dishes//
create procedure edit_dishes(in account varchar(50), in restName varchar(50), in disName varchar(50), in kind varchar(50), in price int)

	begin
		declare cnt int;
		start transaction;
        
            
            
            
			select count(*) into cnt
            from indent join restaurant on indent.restaurant_rid = restaurant.rid
            where indent.finished = 0 and restaurant.name = restName and restaurant.person_account = account;
            
            if cnt = 0 then
				update dishes
                set dishes.name = disName, dishes.price = price, dishes.kind = kind
				where dishes.restaurant_rid in 
					(select restaurant.rid
					from restaurant
					where restaurant.person_account = account and restaurant.name = restName)
					and  dishes.name = disName;
				commit;
			else
				rollback;
			end if;
			
        
        
        
	end//
    
delimiter ;