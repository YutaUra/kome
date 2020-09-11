from kome.delete import DeleteClause
from kome.field import Field
from kome.table import BasicTable


def test_delete_all():
    table1 = BasicTable("table1")
    assert DeleteClause().from_(table1).all().sql == 'DELETE FROM "table1"'
    f1 = Field("f1", table1)
    assert (
        DeleteClause().from_(table1).where(f1 == 10).sql
        == 'DELETE FROM "table1" WHERE "table1"."f1"=10'
    )
    table2 = BasicTable("table2").as_("t")
    f2 = Field("f2", table2)
    assert (
        DeleteClause().from_(table2).where(f2 == 10).sql
        == 'DELETE "t" FROM "table2" AS "t" WHERE "t"."f2"=10'
    )
    assert (
        DeleteClause().from_(table2).where(f2 == 10).sql
        == 'DELETE "t" FROM "table2" AS "t" WHERE "t"."f2"=10'
    )
