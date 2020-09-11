from kome.const import OrderType
from kome.f import count
from kome.field import Field
from kome.select import SelectClause
from kome.table import BasicTable


def test_select_all():
    table1 = BasicTable("table").as_("t")
    a1 = Field("a1", table1)
    a2 = Field("a2", table1)
    select = SelectClause().from_(table1).select(a1, a2)
    assert select.sql == 'SELECT "t"."a1","t"."a2" FROM ("table" AS "t")'
    select = select.distinct()
    assert select.sql == 'SELECT DISTINCT "t"."a1","t"."a2" FROM ("table" AS "t")'
    table2 = BasicTable("table2")
    select = select.left_join(table2, a1 == 4)
    assert (
        select.sql
        == 'SELECT DISTINCT "t"."a1","t"."a2" FROM ("table" AS "t") LEFT JOIN ("table2") ON "t"."a1"=4'
    )
    table3 = BasicTable("table3")
    a4 = Field("a4", table3)
    select = select.inner_join(table3, a1 == "abc", (a4,))
    assert (
        select.sql == 'SELECT DISTINCT "t"."a1","t"."a2","table3"."a4" '
        'FROM ("table" AS "t") '
        'LEFT JOIN ("table2") ON "t"."a1"=4 '
        'INNER JOIN ("table3") ON "t"."a1"=\'abc\''
    )
    select = select.group_by(a1, a2, a4)
    assert (
        select.sql == 'SELECT DISTINCT "t"."a1","t"."a2","table3"."a4" '
        'FROM ("table" AS "t") '
        'LEFT JOIN ("table2") ON "t"."a1"=4 '
        'INNER JOIN ("table3") ON "t"."a1"=\'abc\' '
        'GROUP BY "t"."a1","t"."a2","table3"."a4"'
    )
    select = select.having(count(a1) == count(a2))
    assert (
        select.sql == 'SELECT DISTINCT "t"."a1","t"."a2","table3"."a4" '
        'FROM ("table" AS "t") '
        'LEFT JOIN ("table2") ON "t"."a1"=4 '
        'INNER JOIN ("table3") ON "t"."a1"=\'abc\' '
        'GROUP BY "t"."a1","t"."a2","table3"."a4" '
        'HAVING COUNT("t"."a1")=COUNT("t"."a2")'
    )
    select = select.order_by(a1).order_by(a2, OrderType.desc)
    assert (
        select.sql == 'SELECT DISTINCT "t"."a1","t"."a2","table3"."a4" '
        'FROM ("table" AS "t") '
        'LEFT JOIN ("table2") ON "t"."a1"=4 '
        'INNER JOIN ("table3") ON "t"."a1"=\'abc\' '
        'GROUP BY "t"."a1","t"."a2","table3"."a4" '
        'HAVING COUNT("t"."a1")=COUNT("t"."a2") '
        'ORDER BY "t"."a1" ASC,"t"."a2" DESC'
    )
    select = select.limit(10)
    assert (
        select.sql == 'SELECT DISTINCT "t"."a1","t"."a2","table3"."a4" '
        'FROM ("table" AS "t") '
        'LEFT JOIN ("table2") ON "t"."a1"=4 '
        'INNER JOIN ("table3") ON "t"."a1"=\'abc\' '
        'GROUP BY "t"."a1","t"."a2","table3"."a4" '
        'HAVING COUNT("t"."a1")=COUNT("t"."a2") '
        'ORDER BY "t"."a1" ASC,"t"."a2" DESC '
        "LIMIT 10"
    )


# def test_simple_select():
#     table = Table("table")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "table"."field1","table"."field2" FROM "table"'
#         == Query.from_(table).select(field1, field2).sql()
#     )


# def test_select_with_aliased_table():
#     table = Table("table").as_("t")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "t"."field1","t"."field2" FROM "table" AS "t"'
#         == Query.from_(table).select(field1, field2).sql()
#     )


# def test_select_distinct():
#     table = Table("table").as_("t")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT DISTINCT "t"."field1","t"."field2" FROM "table" AS "t"'
#         == Query.from_(table).select(field1, field2).distinct().sql()
#     )
