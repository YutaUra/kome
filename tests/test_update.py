from kome.expression import P
from kome.field import Field
from kome.table import BasicTable
from kome.update import UpdateClause


def test_update_all():
    table1 = BasicTable("table1").as_("t")
    f1 = Field("f1", table1)
    update = UpdateClause().from_(table1).set(f1, 1)
    assert update.sql == 'UPDATE "table1" AS "t" SET "t"."f1"=1'
    f2 = Field("f2", table1)
    update = update.set(f2, P("?"))
    assert update.sql == 'UPDATE "table1" AS "t" SET "t"."f1"=1,"t"."f2"=?'
    update = update.where(f2 > 5)
    assert (
        update.sql
        == 'UPDATE "table1" AS "t" SET "t"."f1"=1,"t"."f2"=? WHERE "t"."f2">5'
    )
