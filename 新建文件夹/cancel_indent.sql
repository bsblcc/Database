use mydb;
delimiter //
drop procedure if exists cancel_indent //
create procedure cancel_indent (in iid int)
	begin
		declare cnt int;
		start transaction;
        
        delete from indent_has_dishes
        where indent_iid = iid;
        
        delete from indent
        where indent.iid = iid;
        
        
        commit;
	end//
    
delimiter ;