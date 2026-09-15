import unittest

from daos.jury_dao import JuryDao
from models.jury import Jury


class TestJuryDao(unittest.TestCase):

    def setUp(self):
        self.jury_dao = JuryDao()

    def test_real_all_juries(self):
        juries = self.jury_dao.read_all()

        self.assertIsInstance(juries, list)
        self.assertGreater(len(juries), 0)

        for jury in juries:
            self.assertIsInstance(jury, Jury)
            self.assertIsNotNone(jury.id)

        self.assertEqual(juries[0].first_name, "Didier")
        self.assertFalse(juries[0].is_president)
        self.assertEqual(juries[2].last_name, "Ben Jelloun")
