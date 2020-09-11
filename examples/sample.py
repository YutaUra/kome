from pyqueryinterafce.query import Query


class Table_2:
    def __init__(self) -> None:
        self.table_name = "aa"

    def sql(self):
        return "ok"


Query.from_(Table_2())