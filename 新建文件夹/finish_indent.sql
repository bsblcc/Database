use mydb;

delimiter //
drop procedure if exists finish_indent //
create procedure finish_indent(in iid int)

	begin
    
        declare s int;
		start transaction;
        
        update indent
        set indent.finished = 1
        where indent.iid = iid;
        
        update restaurant natural join indent
        set restaurant.sales = restaurant.sales + 1
        where indent.iid = iid;
        
        update indent natural join restaurant join dishes on restaurant.rid = dishes.Restaurant_RID
        set dishes.sales = dishes.sales + 1
        where indent.iid = iid;
        
        select sum(dishes.price * indent_has_dishes.count) into s
		from indent natural join restaurant join indent_has_dishes on indent_has_dishes.Indent_IID = indent.iid join dishes  on dishes.name = indent_has_dishes.Dishes_name
		where indent.iid = iid;
        
        if s is null then
			rollback;
		end if;
        
        update restaurant natural join indent
        set restaurant.turnover = 
			case
				when restaurant.sales = 0 then null
				when restaurant.turnover is null then s
				else restaurant.turnover + s
			end
		where indent.iid = iid;
        
        
        
        commit;
	end//
    
delimiter ;