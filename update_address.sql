use mydb;
delimiter //
drop procedure if exists delete_address //
create procedure delete_address (in account varchar(50), in address varchar(50))
	begin
		declare cnt int;
		start transaction;
        
        
        select count(*) into cnt
        from indent
        where indent.Address_address = id and indent.Address_Person_account = account and indent.finished = 0;
        
        
        if cnt > 0 then
			rollback;
		end if;
        
        delete from address
        where indent.Address_address = id and indent.Address_Person_account;
        
        
        commit;
	end//
    
delimiter ;