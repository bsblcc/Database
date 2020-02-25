use mydb;

delimiter //
drop procedure if exists insert_restaurantOwner //
create procedure insert_restaurantOwner(in account varchar(50), in name varchar(50), in psw varchar(50), in phn varchar(50), in sex ENUM('Male', 'Female'), 
								in restName varchar(50), in st time, in et time, in restAddress varchar(50), in cuisines ENUM('Fast Food', 'Italian', 'Mexico', 'French', 'Japanese', 'Chinese'))

	begin
		
        start transaction;
        
		insert into person (account, name, password, phone_number, sex)
        values (account, name, psw, phn ,sex);
        
        insert into restaurant (name, address, Person_account, start_time, end_time, cuisines)
        values (restName, restAddress, account, st, et, cuisines);
        
        commit;
	end//
    