
insert into person (account, name, sex, phone_number, password)
values ('bsblcc', 'grrr', 'Male', '13820227110', '741011');


insert into address (address, person_account)
values ('Tianjin', 'bsblcc');



insert into restaurant (name, address, cuisines, Person_account, start_time, end_time )
values ('Shitang', 'Nankai', 0101, 'bsblcc', '8:00', '22:00');



insert into dishes (name, price, kind, restaurant_rid)
values ('Hefan', 13, 'Fast Food', 1);

call insert_indent(1, 'Tianjin' , 'bsblcc');


insert into indent_has_dishes (indent_iid, dishes_name, dishes_restaurant_rid, count)
values (1,'Hefan', 1,7);