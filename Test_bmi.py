import ET0735_Lab2.bmi as bmi

def test_bmi_normal_weight():
    weight=63
    height=1.74
    assert (bmi.calculate_bmi(weight,height)==0)


def test_bmi_over_weight():
    weight = 100
    height = 1.74
    assert (bmi.calculate_bmi(weight, height) == 1)


def test_bmi_under_weight():
    weight = 56
    height = 1.74
    assert (bmi.calculate_bmi(weight, height) == -1)

