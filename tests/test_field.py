# from pyqueryinterafce.interface.field import Field
# from pyqueryinterafce.interface.table import Table


# def test_simple_field():
#     table = Table("table")
#     field = Field("field", table)
#     assert '"table"."field"' == field.sql()


# def test_field_with_alised_table():
#     table = Table("table").as_("t")
#     field = Field("field", table)
#     assert '"t"."field"' == field.sql()