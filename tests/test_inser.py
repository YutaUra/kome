from kome.expression import P
from kome.field import Field
from kome.insert import InsertClause
from kome.table import BasicTable


def test_insert_all():
    table1 = BasicTable("table1")
    f1 = Field("f1", table1)
    f2 = Field("f2", table1)
    assert (
        InsertClause().into(table1).columns(f1).values(1).sql
        == 'INSERT INTO "table1" ("f1") VALUES (1)'
    )
    assert (
        InsertClause().into(table1).columns(f1, f2).values(P("?"), 2).sql
        == 'INSERT INTO "table1" ("f1","f2") VALUES (?,2)'
    )
    assert (
        InsertClause().into(table1).columns(f1, f2).values(1, 2).values(10, "aaa").sql
        == 'INSERT INTO "table1" ("f1","f2") VALUES (1,2),(10,\'aaa\')'
    )
