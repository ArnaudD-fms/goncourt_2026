from typing import List
from daos.dao import Dao
from models.jury import Jury


class JuryDao(Dao[Jury]):
    def read_all(self) -> List[Jury]:
        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT * FROM go_jury
            """
            cursor.execute(sql)
            records = cursor.fetchall()

        juries = []
        for record in records:
            jury = Jury(
                record["ju_first_name"],
                record["ju_last_name"],
                record["ju_joining_date"],
                record["ju_is_president"]
            )
            jury.id = record["ju_id_jury"]
            juries.append(jury)

        return juries

