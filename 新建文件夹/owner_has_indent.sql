CREATE VIEW `owner_has_indent` (owner_account , restaurant_name , customer_account , address , time , iid , finished) AS
    SELECT 
        person.account,
        restaurant.name,
        indent.address_person_account,
        indent.address_address,
        indent.time,
        indent.iid,
        indent.finished
    FROM
        person
            JOIN
        restaurant ON person.account = restaurant.person_account
            NATURAL JOIN
        indent;