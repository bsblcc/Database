use mydb;
delimiter //
drop procedure if exists delete_address //
create procedure delete_address (in account varchar(50), in address varchar(50))
	begin
		declare cnt int;
		start transaction;
        
        
        select count(*) into cnt
        from indent
        where indent.Address_address = address and indent.Address_Person_account = account and indent.finished = 0;
        
        
        if cnt = 0 then
			delete from address
			where address.address = address and Address.Person_account = account;
            commit;
		else
			rollback;
		end if;
        
        
        
        
        
	end//
    
delimiter ;