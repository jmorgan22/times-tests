from times import time_range, compute_overlap_time
from pytest import raises
def test_given_input(): 
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_time_ranges_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 11:45:00")
    result = compute_overlap_time(large, short)
    assert result == []
   
def test_backwards_time_range():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 11:00:00")