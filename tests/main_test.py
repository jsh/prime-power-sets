from unittest.mock import patch

from identical_means import main


def test_main_no_duplicates(capsys):
    with patch("identical_means.get_and_validate_args", return_value=(5, 2)):
        with patch(
            "identical_means.generate_bit_count_sequence",
            return_value=[1.0, 2.0, 3.0, 4.0, 5.0],
        ):
            main()
            captured = capsys.readouterr()
            assert captured.out == ""


def test_main_with_duplicates_no_disjoint(capsys):
    with patch("identical_means.get_and_validate_args", return_value=(5, 2)):
        with patch(
            "identical_means.generate_bit_count_sequence",
            return_value=[1.0, 1.0, 3.0, 1.0, 5.0],
        ):
            with patch("identical_means.find_disjoint_pairs", return_value=[]):
                main()
                captured = capsys.readouterr()
                assert captured.out == ""


def test_main_with_output(capsys):
    with patch("identical_means.get_and_validate_args", return_value=(14, 2)):
        main()
        captured = capsys.readouterr()
        assert captured.out == "mean=1259.0, subsets=[7554, 8813, 16367]\n"
