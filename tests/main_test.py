from unittest.mock import patch

from identical_means import main


def test_main_no_duplicates(capsys):
    with patch("identical_means.parse_args", return_value=(5, 2)):
        with patch(
            "identical_means.generate_bit_count_sequence",
            return_value=[1.0, 2.0, 3.0, 4.0, 5.0],
        ):
            main()
            captured = capsys.readouterr()
            assert captured.out == ""


def test_main_with_duplicates_no_disjoint(capsys):
    with patch("identical_means.parse_args", return_value=(5, 2)):
        with patch(
            "identical_means.generate_bit_count_sequence",
            return_value=[1.0, 1.0, 3.0, 1.0, 5.0],
        ):
            with patch("identical_means.find_disjoint_pairs", return_value=[]):
                main()
                captured = capsys.readouterr()
                assert captured.out == ""


def test_main_with_output(capsys):
    with patch("identical_means.parse_args", return_value=(10000, 2)):
        main()
        captured = capsys.readouterr()
        assert captured.out == "(1259.0, [7554, 8813])\n"


# def test_main_with_duplicates_and_disjoint(capsys):
#     with patch('identical_means.parse_args', return_value=(5, 2)):
#         with patch('identical_means.generate_bit_count_sequence', return_value=[1.0, 1.0, 3.0, 1.0, 5.0]):
#             with patch('identical_means.find_exact_float_duplicates_with_indices', return_value=[(1.0, [0, 1, 3])]):
#                 with patch('identical_means.find_disjoint_pairs', return_value([(0, 1)])):
#                     main()
#                     captured = capsys.readouterr()
#                     assert captured.out == "(1.0, [0, 1, 3])\n"
