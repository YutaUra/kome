# from pyqueryinterafce.field import NumericField
# from pyqueryinterafce.table import Table


# def test_add_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     assert '"table"."field1"+"table"."field2"' == (field1 + field2).sql()


# def test_sub_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     assert '"table"."field1"-"table"."field2"' == (field1 - field2).sql()


# def test_mul_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     assert '"table"."field1"*"table"."field2"' == (field1 * field2).sql()


# def test_div_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     assert '"table"."field1"/"table"."field2"' == (field1 / field2).sql()


# def test_aliased_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     assert (
#         '"table"."field1"+"table"."field2" AS "sum"'
#         == (field1 + field2).as_("sum").sql()
#     )


# def test_complex_add_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     field3 = NumericField("field3", table)
#     assert (
#         '"table"."field1"+"table"."field2"+"table"."field3"'
#         == (field1 + field2 + field3).sql()
#     )


# def test_complex_add_mul_numeric_field():
#     table = Table("table")
#     field1 = NumericField("field1", table)
#     field2 = NumericField("field2", table)
#     field3 = NumericField("field3", table)
#     assert (
#         '"table"."field1"+"table"."field2"*"table"."field3"'
#         == (field1 + field2 * field3).sql()
#     )


# def test_complex_numeric_field():
#     table1 = Table("table1").as_("t1")
#     table2 = Table("table2").as_("t2")
#     field1 = NumericField("field1", table1)
#     field2 = NumericField("field2", table1)
#     field3 = NumericField("field3", table2)
#     assert (
#         '("t1"."field1"+"t1"."field2")*("t2"."field3"+"t1"."field2")/"t1"."field2"*"t1"."field1"'
#         == ((field1 + field2) * (field3 + field2) / field2 * field1).sql()
#     )
