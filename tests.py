import unittest
from main import decimal_to_binary, binary_addition

class DecimalToBinary(unittest.TestCase):
    def test_zero(self):
        expected = []
        actual = decimal_to_binary(0)
        self.assertEqual(expected, actual)

    def test_one(self):
        expected = [True]
        actual = decimal_to_binary(1)
        self.assertEqual(expected, actual)

    def test_five(self):
        expected = [True, False, True]
        actual = decimal_to_binary(5)
        self.assertEqual(expected, actual)

    def test_lots (self):
        for case in [
            (91858, [True, False, True, True, False, False, True, True, False, True, True, False, True, False, False, True, False]),
            (77955, [True, False, False, True, True, False, False, False, False, True, False, False, False, False, False, True, True]),
            (34851, [True, False, False, False, True, False, False, False, False, False, True, False, False, False, True, True]),
            (65873, [True, False, False, False, False, False, False, False, True, False, True, False, True, False, False, False, True]),
            (21826, [True, False, True, False, True, False, True, False, True, False, False, False, False, True, False]),
            (61056, [True, True, True, False, True, True, True, False, True, False, False, False, False, False, False, False]),
            (46096, [True, False, True, True, False, True, False, False, False, False, False, True, False, False, False, False]),
            (62182, [True, True, True, True, False, False, True, False, True, True, True, False, False, True, True, False]),
            (55226, [True, True, False, True, False, True, True, True, True, False, True, True, True, False, True, False]),
            (66182, [True, False, False, False, False, False, False, True, False, True, False, False, False, False, True, True, False]),
            (13722, [True, True, False, True, False, True, True, False, False, True, True, False, True, False]),
            (71258, [True, False, False, False, True, False, True, True, False, False, True, False, True, True, False, True, False]),
            (28357, [True, True, False, True, True, True, False, True, True, False, False, False, True, False, True]),
            (70776, [True, False, False, False, True, False, True, False, False, False, True, True, True, True, False, False, False]),
            (22362, [True, False, True, False, True, True, True, False, True, False, True, True, False, True, False]),
            (58369, [True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, True]),
            (15985, [True, True, True, True, True, False, False, True, True, True, False, False, False, True]),
            (64636, [True, True, True, True, True, True, False, False, False, True, True, True, True, True, False, False]),
            (12795, [True, True, False, False, False, True, True, True, True, True, True, False, True, True]),
            (21061, [True, False, True, False, False, True, False, False, True, False, False, False, True, False, True]),
            (369, [True, False, True, True, True, False, False, False, True]),
            (56540, [True, True, False, True, True, True, False, False, True, True, False, True, True, True, False, False]),
            (49588, [True, True, False, False, False, False, False, True, True, False, True, True, False, True, False, False]),
            (61793, [True, True, True, True, False, False, False, True, False, True, True, False, False, False, False, True]),
            (68173, [True, False, False, False, False, True, False, True, False, False, True, False, False, True, True, False, True]),
            (23579, [True, False, True, True, True, False, False, False, False, False, True, True, False, True, True]),
            (35703, [True, False, False, False, True, False, True, True, False, True, True, True, False, True, True, True]),
            (97819, [True, False, True, True, True, True, True, True, False, False, False, False, True, True, False, True, True]),
            (74074, [True, False, False, True, False, False, False, False, True, False, True, False, True, True, False, True, False]),
            (62656, [True, True, True, True, False, True, False, False, True, True, False, False, False, False, False, False]),
            (90181, [True, False, True, True, False, False, False, False, False, False, True, False, False, False, True, False, True]),
            (19528, [True, False, False, True, True, False, False, False, True, False, False, True, False, False, False]),
            (72659, [True, False, False, False, True, True, False, True, True, True, True, False, True, False, False, True, True]),
            (23049, [True, False, True, True, False, True, False, False, False, False, False, True, False, False, True]),
            (30112, [True, True, True, False, True, False, True, True, False, True, False, False, False, False, False]),
            (66568, [True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False]),
            (50, [True, True, False, False, True, False]),
            (52081, [True, True, False, False, True, False, True, True, False, True, True, True, False, False, False, True]),
            (87220, [True, False, True, False, True, False, True, False, False, True, False, True, True, False, True, False, False]),
            (3128, [True, True, False, False, False, False, True, True, True, False, False, False]),
            (58129, [True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, True]),
            (96226, [True, False, True, True, True, False, True, True, True, True, True, True, False, False, False, True, False]),
            (21980, [True, False, True, False, True, False, True, True, True, False, True, True, True, False, False]),
            (90277, [True, False, True, True, False, False, False, False, False, True, False, True, False, False, True, False, True]),
            (46452, [True, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False]),
            (26440, [True, True, False, False, True, True, True, False, True, False, False, True, False, False, False]),
            (55240, [True, True, False, True, False, True, True, True, True, True, False, False, True, False, False, False]),
            (89555, [True, False, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True]),
            (99899, [True, True, False, False, False, False, True, True, False, False, False, True, True, True, False, True, True]),
            (26046, [True, True, False, False, True, False, True, True, False, True, True, True, True, True, False]),
            (66140, [True, False, False, False, False, False, False, True, False, False, True, False, True, True, True, False, False]),
            (33805, [True, False, False, False, False, True, False, False, False, False, False, False, True, True, False, True]),
            (76277, [True, False, False, True, False, True, False, False, True, True, True, True, True, False, True, False, True]),
            (13132, [True, True, False, False, True, True, False, True, False, False, True, True, False, False]),
            (62104, [True, True, True, True, False, False, True, False, True, False, False, True, True, False, False, False]),
            (45469, [True, False, True, True, False, False, False, True, True, False, False, True, True, True, False, True]),
            (37502, [True, False, False, True, False, False, True, False, False, True, True, True, True, True, True, False]),
            (77459, [True, False, False, True, False, True, True, True, False, True, False, False, True, False, False, True, True]),
            (1778, [True, True, False, True, True, True, True, False, False, True, False]),
            (31053, [True, True, True, True, False, False, True, False, True, False, False, True, True, False, True]),
            (5698, [True, False, True, True, False, False, True, False, False, False, False, True, False]),
            (56693, [True, True, False, True, True, True, False, True, False, True, True, True, False, True, False, True]),
            (3707, [True, True, True, False, False, True, True, True, True, False, True, True]),
            (93648, [True, False, True, True, False, True, True, False, True, True, True, False, True, False, False, False, False]),
            (96001, [True, False, True, True, True, False, True, True, True, False, False, False, False, False, False, False, True]),
            (90006, [True, False, True, False, True, True, True, True, True, True, False, False, True, False, True, True, False]),
            (56352, [True, True, False, True, True, True, False, False, False, False, True, False, False, False, False, False]),
            (72351, [True, False, False, False, True, True, False, True, False, True, False, False, True, True, True, True, True]),
            (1767, [True, True, False, True, True, True, False, False, True, True, True]),
            (75065, [True, False, False, True, False, False, True, False, True, False, False, True, True, True, False, False, True]),
            (93312, [True, False, True, True, False, True, True, False, False, True, False, False, False, False, False, False, False]),
            (50993, [True, True, False, False, False, True, True, True, False, False, True, True, False, False, False, True]),
            (70250, [True, False, False, False, True, False, False, True, False, False, True, True, False, True, False, True, False]),
            (13179, [True, True, False, False, True, True, False, True, True, True, True, False, True, True]),
            (29351, [True, True, True, False, False, True, False, True, False, True, False, False, True, True, True]),
            (96723, [True, False, True, True, True, True, False, False, True, True, True, False, True, False, False, True, True]),
            (37518, [True, False, False, True, False, False, True, False, True, False, False, False, True, True, True, False]),
            (80451, [True, False, False, True, True, True, False, True, False, False, True, False, False, False, False, True, True]),
            (51005, [True, True, False, False, False, True, True, True, False, False, True, True, True, True, False, True]),
            (21488, [True, False, True, False, False, True, True, True, True, True, True, False, False, False, False]),
            (25640, [True, True, False, False, True, False, False, False, False, True, False, True, False, False, False]),
            (84693, [True, False, True, False, False, True, False, True, False, True, True, False, True, False, True, False, True]),
            (371, [True, False, True, True, True, False, False, True, True]),
            (40609, [True, False, False, True, True, True, True, False, True, False, True, False, False, False, False, True]),
            (40218, [True, False, False, True, True, True, False, True, False, False, False, True, True, False, True, False]),
            (80642, [True, False, False, True, True, True, False, True, True, False, False, False, False, False, False, True, False]),
            (4451, [True, False, False, False, True, False, True, True, False, False, False, True, True]),
            (38878, [True, False, False, True, False, True, True, True, True, True, False, True, True, True, True, False]),
            (87980, [True, False, True, False, True, False, True, True, True, True, False, True, False, True, True, False, False]),
            (13449, [True, True, False, True, False, False, True, False, False, False, True, False, False, True]),
            (28785, [True, True, True, False, False, False, False, False, True, True, True, False, False, False, True]),
            (7190, [True, True, True, False, False, False, False, False, True, False, True, True, False]),
            (92388, [True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, False, False]),
            (83682, [True, False, True, False, False, False, True, True, False, True, True, True, False, False, False, True, False]),
            (46214, [True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False]),
            (48404, [True, False, True, True, True, True, False, True, False, False, False, True, False, True, False, False]),
            (87605, [True, False, True, False, True, False, True, True, False, False, False, True, True, False, True, False, True]),
            (89922, [True, False, True, False, True, True, True, True, True, False, True, False, False, False, False, True, False]),
            (23472, [True, False, True, True, False, True, True, True, False, True, True, False, False, False, False]),
            (26849, [True, True, False, True, False, False, False, True, True, True, False, False, False, False, True])
        ]:
            with self.subTest(case):
                integer, expected = case
                actual = decimal_to_binary(integer)
                self.assertEqual(expected, actual)


class DecimalBinaryAddition(unittest.TestCase):
    def test_zero_zero (self):
        expected = []
        actual = binary_addition(decimal_to_binary(0), decimal_to_binary(0))
        self.assertEqual(expected, actual)

    def test_zero_one (self):
        expected = [True]
        actual = binary_addition(decimal_to_binary(0), decimal_to_binary(1))
        self.assertEqual(expected, actual)

    def test_two_two (self):
        expected = [True, False, False]
        actual = binary_addition(decimal_to_binary(2), decimal_to_binary(2))
        self.assertEqual(expected, actual)

    def test_lots (self):
        for case in [
            (61476, 97124, [True, False, False, True, True, False, True, False, True, True, True, False, False, False, True, False, False, False]),
            (35145, 1905, [True, False, False, True, False, False, False, False, True, False, True, True, True, False, True, False]),
            (13032, 11963, [True, True, False, False, False, False, True, True, False, True, False, False, False, True, True]),
            (86350, 6512, [True, False, True, True, False, True, False, True, False, True, False, True, True, True, True, True, False]),
            (23331, 8697, [True, True, True, True, True, False, True, False, False, False, True, True, True, False, False]),
            (48143, 8761, [True, True, False, True, True, True, True, False, False, True, False, False, True, False, False, False]),
            (36658, 53321, [True, False, True, False, True, True, True, True, True, False, True, True, True, True, False, True, True]),
            (95839, 41570, [True, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, True]),
            (113, 91549, [True, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, False]),
            (90915, 23200, [True, True, False, True, True, True, True, False, True, True, True, False, False, False, False, True, True]),
            (28288, 18180, [True, False, True, True, False, True, False, True, True, False, False, False, False, True, False, False]),
            (58940, 61721, [True, True, True, False, True, False, True, True, True, False, True, False, True, False, True, False, True]),
            (39928, 84447, [True, True, True, True, False, False, True, False, True, True, True, False, True, False, True, True, True]),
            (45391, 44779, [True, False, True, True, False, False, False, False, False, False, False, True, True, True, False, True, False]),
            (12958, 45850, [True, True, True, False, False, True, False, True, True, False, True, True, True, False, False, False]),
            (57128, 77700, [True, False, False, False, False, False, True, True, True, False, True, False, True, False, True, True, False, False]),
            (43334, 90425, [True, False, False, False, False, False, True, False, True, False, False, True, True, True, True, True, True, True]),
            (36047, 91697, [True, True, True, True, True, False, False, True, True, False, False, False, False, False, False, False, False]),
            (74846, 31719, [True, True, False, True, False, False, False, False, False, False, True, False, False, False, True, False, True]),
            (70362, 48189, [True, True, True, False, False, True, True, True, True, False, False, False, True, False, True, True, True]),
            (2312, 49904, [True, True, False, False, True, False, True, True, True, True, True, True, True, False, False, False]),
            (42004, 1842, [True, False, True, False, True, False, True, True, False, True, False, False, False, True, True, False]),
            (51212, 32539, [True, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, True]),
            (47209, 42978, [True, False, True, True, False, False, False, False, False, False, True, False, False, True, False, True, True]),
            (64486, 64479, [True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, False, True]),
            (80740, 27096, [True, True, False, True, False, False, True, False, True, False, False, True, True, True, True, False, False]),
            (81791, 71336, [True, False, False, True, False, True, False, True, True, False, False, False, True, False, False, True, True, True]),
            (93428, 89483, [True, False, True, True, False, False, True, False, True, False, False, True, True, True, True, True, True, True]),
            (61985, 95680, [True, False, False, True, True, False, False, True, True, True, True, True, True, False, False, False, False, True]),
            (60934, 60261, [True, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, True]),
            (4698, 39434, [True, False, True, False, True, True, False, False, False, True, True, False, False, True, False, False]),
            (50218, 74554, [True, True, True, True, False, False, True, True, True, False, True, True, False, False, True, False, False]),
            (1372, 85712, [True, False, True, False, True, False, True, False, False, False, False, True, False, True, True, False, False]),
            (37070, 46381, [True, False, True, False, False, False, True, False, True, True, True, True, True, True, False, True, True]),
            (24595, 4527, [True, True, True, False, False, False, True, True, True, False, False, False, False, True, False]),
            (39095, 56650, [True, False, True, True, True, False, True, True, False, False, False, False, False, False, False, False, True]),
            (89168, 3526, [True, False, True, True, False, True, False, True, False, False, False, False, True, False, True, True, False]),
            (9639, 84509, [True, False, True, True, False, True, True, True, True, True, True, False, False, False, True, False, False]),
            (29241, 7328, [True, False, False, False, True, True, True, False, True, True, False, True, True, False, False, True]),
            (79594, 46997, [True, True, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True]),
            (40443, 92799, [True, False, False, False, False, False, True, False, False, False, False, True, True, True, True, False, True, False]),
            (61569, 1507, [True, True, True, True, False, True, True, False, False, True, True, False, False, True, False, False]),
            (91654, 4810, [True, False, True, True, True, True, False, False, False, True, True, False, True, False, False, False, False]),
            (56069, 86206, [True, False, False, False, True, False, True, False, True, True, True, True, False, False, False, False, True, True]),
            (87148, 92471, [True, False, True, False, True, True, True, True, False, True, True, False, True, False, False, False, True, True]),
            (6456, 25587, [True, True, True, True, True, False, True, False, False, True, False, True, False, True, True]),
            (93841, 99672, [True, False, True, True, True, True, False, False, True, True, True, True, True, False, True, False, False, True]),
            (13622, 12834, [True, True, False, False, True, True, True, False, True, False, True, True, False, False, False]),
            (92835, 7309, [True, True, False, False, False, False, True, True, True, False, False, True, True, False, False, False, False]),
            (82248, 30753, [True, True, False, True, True, True, False, False, True, False, True, True, False, True, False, False, True]),
            (6328, 68387, [True, False, False, True, False, False, False, True, True, True, True, False, True, True, False, True, True]),
            (7961, 89886, [True, False, True, True, True, True, True, True, False, False, False, True, True, False, True, True, True]),
            (9284, 24237, [True, False, False, False, False, False, True, False, True, True, True, True, False, False, False, True]),
            (38406, 15181, [True, True, False, True, False, False, False, True, False, True, False, True, False, False, True, True]),
            (37427, 53044, [True, False, True, True, False, False, False, False, True, False, True, True, False, False, True, True, True]),
            (44742, 14468, [True, True, True, False, False, True, True, True, False, True, False, False, True, False, True, False]),
            (13759, 95531, [True, True, False, True, False, True, False, True, False, True, True, True, False, True, False, True, False]),
            (49295, 85287, [True, False, False, False, False, False, True, True, False, True, True, False, True, True, False, True, True, False]),
            (65688, 66362, [True, False, False, False, False, False, False, False, True, True, True, True, False, True, False, False, True, False]),
            (77974, 29205, [True, True, False, True, False, False, False, True, False, True, False, True, False, True, False, True, True]),
            (47116, 26178, [True, False, False, False, True, True, True, True, False, False, True, False, False, True, True, True, False]),
            (1256, 72407, [True, False, False, False, True, True, True, True, True, True, False, True, True, True, True, True, True]),
            (68308, 98100, [True, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False]),
            (84335, 78614, [True, False, False, True, True, True, True, True, False, False, True, False, False, False, False, True, False, True]),
            (82090, 73198, [True, False, False, True, False, True, True, True, True, False, True, False, False, True, True, False, False, False]),
            (2868, 36513, [True, False, False, True, True, False, False, True, True, True, False, True, False, True, False, True]),
            (40828, 34687, [True, False, False, True, False, False, True, True, False, True, True, True, True, True, False, True, True]),
            (22037, 96341, [True, True, True, False, False, True, True, True, False, False, True, True, False, True, False, True, False]),
            (64730, 42905, [True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True]),
            (59662, 12782, [True, False, False, False, True, True, False, True, False, True, True, True, True, True, True, False, False]),
            (57076, 33103, [True, False, True, True, False, False, False, False, False, False, True, False, False, False, False, True, True]),
            (89729, 46174, [True, False, False, False, False, True, False, False, True, False, True, True, False, True, True, True, True, True]),
            (90531, 69681, [True, False, False, True, True, True, False, False, False, True, True, True, False, True, False, True, False, False]),
            (74341, 84281, [True, False, False, True, True, False, True, False, True, True, True, False, False, True, True, True, True, False]),
            (12075, 68457, [True, False, False, True, True, True, False, True, False, True, False, False, True, False, True, False, False]),
            (17240, 37967, [True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True]),
            (45023, 15261, [True, True, True, False, True, False, True, True, False, True, True, True, True, True, False, False]),
            (26719, 75818, [True, True, False, False, True, False, False, False, False, True, False, False, False, True, False, False, True]),
            (7273, 1817, [True, False, False, False, True, True, True, False, False, False, False, False, True, False]),
            (51150, 37807, [True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True]),
            (97079, 67217, [True, False, True, False, False, False, False, False, False, True, True, True, False, False, True, False, False, False]),
            (61923, 94511, [True, False, False, True, True, False, False, False, True, True, False, False, False, True, False, False, True, False]),
            (28311, 11467, [True, False, False, True, True, False, True, True, False, True, True, False, False, False, True, False]),
            (2615, 52944, [True, True, False, True, True, False, False, True, False, False, False, False, False, True, True, True]),
            (61917, 93489, [True, False, False, True, False, True, True, True, True, True, False, False, False, False, True, True, True, False]),
            (43872, 65507, [True, True, False, True, False, True, False, True, True, False, True, False, False, False, False, True, True]),
            (11313, 60798, [True, False, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True]),
            (555, 15830, [True, False, False, False, False, False, False, False, False, False, False, False, False, False, True]),
            (81399, 45326, [True, True, True, True, False, True, True, True, True, False, False, False, False, False, True, False, True]),
            (93525, 83788, [True, False, True, False, True, True, False, True, False, False, True, False, True, False, False, False, False, True]),
            (52181, 55257, [True, True, False, True, False, False, False, True, True, True, False, True, False, True, True, True, False]),
            (61414, 52776, [True, True, False, True, True, True, True, True, False, False, False, False, False, True, True, True, False]),
            (16905, 87916, [True, True, False, False, True, True, False, False, True, False, True, True, True, False, True, False, True]),
            (38499, 87520, [True, True, True, True, False, True, True, False, False, False, True, False, False, False, False, True, True]),
            (80556, 85249, [True, False, True, False, False, False, False, True, True, True, True, False, True, False, True, True, False, True]),
            (66462, 85861, [True, False, False, True, False, True, False, False, True, True, False, False, False, False, False, False, True, True]),
            (13700, 28492, [True, False, True, False, False, True, False, False, True, True, False, True, False, False, False, False]),
            (90422, 33777, [True, True, True, True, False, False, True, False, True, False, False, True, False, False, True, True, True]),
            (65822, 74710, [True, False, False, False, True, False, False, True, False, False, True, True, True, True, False, True, False, False]),
            (7760, 72533, [True, False, False, True, True, True, False, False, True, True, False, True, False, False, True, False, True]),
        ]:
            with self.subTest(case):
                a, b, expected = case
                actual = binary_addition(decimal_to_binary(a), decimal_to_binary(b))
                self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
