from src import basics, calculator

def test_multiply():
    assert basics.multiply(3, 4) == 12

def test_run_calc():
    assert calculator.run_calculator(4, 2, '/') == 2
