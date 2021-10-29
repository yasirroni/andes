import os
import andes
import numpy as np

import unittest
from andes.utils.snapshot import save_ss, load_ss


class TestSnapshot(unittest.TestCase):
    """
    Test ANDES snapshot.
    """

    def test_save_ss(self):
        ss = andes.run(andes.get_case("kundur/kundur_full.xlsx"))
        ss.TDS.config.tf = 2
        ss.TDS.run()

        save_ss('test_ss.pkl', ss)
        os.remove('test_ss.pkl')

    def load_ss(self):
        test_dir = os.path.dirname(__file__)
        ss = load_ss(os.path.join(test_dir, 'kundur_full_2s.pkl'))
        ss.TDS.config.tf = 2
        ss.TDS.run()

        np.testing.assert_almost_equal(ss.GENROU.omega.v,
                                       np.array([1.00474853, 1.00456209, 1.00316554, 1.00298933]))
