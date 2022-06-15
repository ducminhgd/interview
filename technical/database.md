# Database

## In MySQL, what is difference between BTREE and HASH indices?

    *HASH* is only supported in memory table and for Memory table, *HASH* is default, otherwise *BTREE* is default.

    *BTREE* is a binary tree data structure and is good for comparision operators and some discrete values: `=`, `<`, `>`, `<=`, `>=`, `BETWEEN`, `LIKE`.

    *HASH* is a key-value map, and it is good for operators `=` or `<>`. Cannot optimize `ORDER BY` with *HASH*.

## What are differences between `COUNT(*)`, `COUNT(1)` and `COUNT(column_name)`?
   
    `COUNT(*)` counts all rows of a result set, including `NULL` values.

    `COUNT(1)`, actually likes `COUNT(*)` or `COUNT(<any number>)`, the `COUNT()` function is assigned to every row of result set, and it counts how many time that `1`, `*` or `<any number>` has been assigned.

    `COUNT(column_name)` is a different story. The function count non-`NULL` values in a column of a result set.