use mydb;
delimiter //  
drop procedure if exists delete_dishes//
create procedure delete_dishes(in account varchar(50), in restName varchar(50), in disName varchar(50))

	begin
		declare cnt int;
		start transaction;
        
            
            
            
			select count(*) into cnt
            from indent join restaurant on indent.restaurant_rid = restaurant.rid
            where indent.finished = 0 and restaurant.name = restName and restaurant.person_account = account;
            
            if cnt = 0 then
				delete from dishes
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