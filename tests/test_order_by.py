# from pyqueryinterafce.const import Order
# from pyqueryinterafce.query import Query
# from pyqueryinterafce.field import Field
# from pyqueryinterafce.table import Table


# def test_simple_order_by():
#     table = Table("table")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "table"."field1","table"."field2" FROM "table" ORDER BY "table"."field1" ASC'
#         == Query.from_(table).select(field1, field2).order_by(field1).sql()
#     )


# def test_simple_order_by_desc():
#     table = Table("table")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "table"."field1","table"."field2" FROM "table" ORDER BY "table"."field1" DESC'
#         == Query.from_(table).select(field1, field2).order_by(field1, Order.desc).sql()
#     )


# def test_multiple_order_by():
#     table = Table("table")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "table"."field1","table"."field2" FROM "table" ORDER BY "table"."field1" ASC,"table"."field2" ASC'
#         == Query.from_(table)
#         .select(field1, field2)
#         .order_by(field1)
#         .order_by(field2)
#         .sql()
#     )


# def test_multiple_order_type():
#     table = Table("table")
#     field1 = Field("field1", table)
#     field2 = Field("field2", table)

#     assert (
#         'SELECT "table"."field1","table"."field2" FROM "table" ORDER BY "table"."field1" DESC,"table"."field2" ASC'
#         == Query.from_(table)
#         .select(field1, field2)
#         .order_by(field1, Order.desc)
#         .order_by(field2, Order.asc)
#         .sql()
#     )
