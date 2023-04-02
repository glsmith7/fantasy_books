import hello.hello as hl   # The code to test

def test_increment():
    assert hl.increment(3) == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert hl.decrement(3) == 2
