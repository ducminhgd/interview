# Database

## In MySQL, what is difference between BTREE and HASH indices?

*HASH* is only supported in memory table and for Memory table, *HASH* is default, otherwise *BTREE* is default.

*BTREE* is a binary tree data structure and is good for comparision operators and some discrete values: `=`, `<`, `>`, `<=`, `>=`, `BETWEEN`, `LIKE`.

*HASH* is a key-value map, and it is good for operators `=` or `<>`. Cannot optimize `ORDER BY` with *HASH*.

## What are differences between `COUNT(*)`, `COUNT(1)` and `COUNT(column_name)`?
   
`COUNT(*)` counts all rows of a result set, including `NULL` values.

`COUNT(1)`, actually likes `COUNT(*)` or `COUNT(<any number>)`, the `COUNT()` function is assigned to every row of result set, and it counts how many time that `1`, `*` or `<any number>` has been assigned.

`COUNT(column_name)` is a different story. The function count non-`NULL` values in a column of a result set.

## Explain the different types of SQL commands

There are five types of SQL commands: DDL, DML, DCL, TCL, and DQL.

1. Data Definition Language:
    - DDL changes the structure of the table like creating a table, deleting a table, altering a table, etc.
    - All the command of DDL are auto-committed that means it permanently save all the changes in the database.
    - Here are some commands: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
2. Data Manipulation Language:
    - DML commands are used to modify the database. It is responsible for all form of changes in the database.
    - The command of DML is not auto-committed that means it can't permanently save all the changes in the database. They can be rollback.
    - Some commands: `INSERT`, `DELETE`, `UPDATE`.
3. Data Control Language
    - DCL commands are used to grant and take back authority from any database user.
    - Some commands: `GRANT`, `REVOKE`.
4. Transaction Control Language
    - TCL commands can only use with DML commands like `INSERT`, `DELETE` and `UPDATE` only.
    - These operations are automatically committed in the database that's why they cannot be used while creating tables or dropping them.
    - Some commands: `COMMIT`, `ROLLBACK`, `SAVEPOINT`
5. Data Query Language
    - DQL is used to fetch the data from the database.
    - Only one command: `SELECT`.

Some people admit that there is another type called Data Administration Commands (DAC), which contains `START AUDIT` and `STOP AUDIT` commands.

## What is a `PRIMARY KEY` constraint?

A `PRIMARY KEY` constraint is a column (or combination of columns) used to designate each table row with a unique identifier.

> Note: There’s a limit of one `PRIMARY KEY` constraint per table. All columns defined within a `PRIMARY KEY` constraint must be defined as NOT NULL.

## What is a `FOREIGN KEY` constraint?

A `FOREIGN KEY` is a column or collection of fields in a table referencing a `PRIMARY KEY` in another table. The table containing the primary key is known as the parent table, and the table containing the foreign key is called the child table.

## What is a `UNIQUE` constraint?

Like the `PRIMARY KEY`, the `UNIQUE` constraint also ensures that each value is different from the others in its column. However, tables can have multiple columns with `UNIQUE` constraints, unlike the `PRIMARY KEY` constraint, limited to just one.