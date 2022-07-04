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

## Explain the different types of JOIN.

There are for types of joins: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `OUTTER JOIN`.

- `INNER JOIN`: get the intersected data of two data sets.
- `LEFT JOIN`: get the intesected data of two data set and the left data set of `JOIN`.
- `RIGHT JOIN`: get the intesected data of two data set and the right data set of `JOIN`.
- `OUTTER JOIN`: get data of both data sets, except the intersected data.

## What’s the difference between a `WHERE` clause and a `HAVING` clause?

`WHERE` is the first condition that is applied to filter data from database and return a result set. `HAVING` is applied as the second condition to return only the groups within the result set that met the first condition.

## What’s the difference between a `TRUNCATE` command and a `DELETE` command?

|     Differences     |                            `DELETE`                             |                   `TRUNCATE`                   |
| ------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| Type                | DML                                                             | DDL                                            |
| Function            | Used to remove specific rows or tuples from tables or relations | Used to delete all rows or tuples from a table |
| `WHERE`             | Can contain `WHERE` clause                                      | Cannot contain `WHERE` clause                  |
| Transaction logging | Row deletions are logged                                        | Deleted data pages are not logged              |

The `TRUNCATE` command is faster than `DELETE`, but unlike the `DELETE` command, data cannot be rolled back after using it to recover data that has been mistakenly deleted.

## What are `UNION`, `UNION ALL`, `MINUS`, and `INTERSECT` set operators?

The `UNION` operation combines the results of two or more `SELECT` statements. For example, getting the `UNION` of sets A and B, this operation would return all rows from both sets, excluding any duplicate rows.

The `UNION ALL` operation does the same thing as `UNION`, but includes duplicate rows in its result set.

The `MINUS` operation combines the results of two `SELECT` statements but only returns rows with values that belong to the first set of the result.

The `INTERSECT` operation combines the results of two `SELECT` statements but only returns the rows with matching values in both sets.

## What are Normalization and Denormalization?

**Normalization** refers to the methods used to remove redundancies and inconsistencies in a database.

**Denormalization** refers to methods used to improve the performance of queries.

Normalization introduces more tables to a database, whereas Denormalization reduces the number of tables.

## What are scalar functions?

Scalar functions are defined by the user and return a single value (i.e., int, char, float, etc.) based on the input value.

Common SQL scalar functions:
- `CONCAT()` concatenates two or more character strings.
- `FORMAT()` sets the format to display a collection of values.
- `LEN()` calculates the total length of a given column.
- `MID()` extracts substrings from a collection of string values.
- `ROUND()` rounds the integer value for a numeric field.
- `NOW()` returns the current date and time.
- `RAND()` calculates a random collection of numbers of a given length.

## What are aggregate functions?

In SQL, aggregate functions (also known as group functions) are applied to a group of values (or all values) to calculate and return a single value.

## What is a stored procedure?

Instead of writing the same SQL query multiple times, you can save it as a stored procedure and call on it whenever necessary to execute it.

## What is an index?

An SQL index is a lookup table used by the database search engine to find and retrieve data quickly. An index can help make `SELECT` and `WHERE` clauses faster but can slow down the use of `UPDATE` and `INSERT` statements.

## What is an SQL Server cursor? How do you use it?

When you want to process result sets one row at a time, you can use a database cursor, a control structure that allows you to traverse records in a database. Cursors can be used to point to individual rows in a group of rows.

## What are the different types of indexes?

- **Clustered indexes** are clustered together with the main body of data. A clustered index sorts and stores rows of data in a table or view sequentially, based on key values of the table to match the order of the index. There can only be one clustered index per table.
- **Non-clustered** indexes are separate from, and cannot be used to store or sort data in the main table. The key values of the index, and not the table are used to define the order of a non-clustered index.
- **Column store indexes** are a standard form of index that efficiently stores data in a column-based format, rather than row-oriented.
- **Filtered indexes** are used to index a section of rows within a table.
- **Hash indexe**s are arrays, and use the Hash function F(K, N), where K is critical and N is the number of slots containing a pointer and row.
- **Unique indexes** assign unique values to every row of data, so that the index key does not contain any duplicates.

## What are ACID properties?

The **ACID** properties refer to properties that must be followed for transactions in a database management system to remain consistent.
- **Atomicity**: The entire transaction takes place at once or not at all.
- **Consistency**: A database must be consistent before and after a transaction takes place.
- **Isolation**: Transactions occur independently and can run concurrently with others.
- **Durability**: Updates to the database must be stored in and written to disk so that transaction records can persist in the event of a system failure.

## What is a schema?

An SQL schema is an abstract representation of logically structured data elements. Database schemas in SQL are defined at the logical level by a database user known as the schema owner.

## What is an alias command?

The alias (`AS`) command makes columns or tables easier to read by giving them temporary names for the duration of a query.

## What is the difference between `CHAR` and `VARCHAR` datatypes in SQL?

The character or `CHAR` datatype stores fixed length character strings.
The variable character or `VARCHAR` datatype stores variable length character strings.

CHAR has better performance than `VARCHAR`, but `VARCHAR` can be useful for anticipating data values without a set length.

## What is collation? What are the different collation sensitivity?

Collation is a configuration setting that specifies how a database sorts and compares data. Different collation rules can be configured to determine the correct character sequence used to sort the character data.

Collation sensitivity can be used to specify how different characters are treated.
- **Accent sensitivity** differentiates between **a** and **á**.
- **Case sensitivity** differentiates between **A** and **a**.
- **Kana sensitivity** differentiates between Japanese Hiragana and Katakana.
- **Width sensitivity** treats characters of different widths (single-byte and double-byte) differently.