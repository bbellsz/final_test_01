from function import calculate_express
from function import validate_express
import pytest
#central,northern,northeastern,eastern,western,southern
@pytest.mark.validate
def test_weight_a_zone_c():
    zone="central"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_a_zone_e():
    zone="eastern"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_a_zone_w():
    zone="western"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_a_zone_n():
    zone="northern"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_a_zone_ne():
    zone="northeastern"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_a_zone_s():
    zone="southern"
    weight = "a"
    expected_result = "Please input weight with float or integer."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_x_zone_x():
    zone="x"
    weight = "x"
    expected_result = "Please input weight as a float or integer, and zone is entered incorrectly."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_1():
    zone=1
    weight = -1
    expected_result = "Impossible, the weight's out of range and Please input zone with string."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_2_zone_1():
    zone=1
    weight = 2
    expected_result = "Please input zone with string."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_x():
    zone="x"
    weight = -1
    expected_result = "Impossible, the weight's out of range and zone is entered incorrectly."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_c():
    zone="central"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result
  
@pytest.mark.validate
def test_weight_m1_zone_e():
    zone="eastern"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_w():
    zone="western"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_n():
    zone="northern"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_ne():
    zone="northeastern"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_zone_s():
    zone="southern"
    weight = -1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_zone_x():
    zone="x"
    weight = 1
    expected_result = "Zone is entered incorrectly."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_0_zone_c_result_0():
    zone="central"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result
  
@pytest.mark.validate
def test_weight_0_zone_e_result_0():
    zone="eastern"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_0_zone_w_result_0():
    zone="western"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_0_zone_n_result_0():
    zone="northern"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_0_zone_ne_result_0():
    zone="northeastern"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_0_zone_s_result_0():
    zone="southern"
    weight = 0
    expected_result = 0
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_c_result_500():
    zone="central"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_e_result_500():
    zone="eastern"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_w_result_500():
    zone="western"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_n_result_500():
    zone="northern"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_ne_result_500():
    zone="northeastern"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_21_zone_s_result_500():
    zone="southern"
    weight = 21
    expected_result = 500
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_c_result_420():
    zone="central"
    weight = 10
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_e_result_420():
    zone="eastern"
    weight = 10
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_w_result_420():
    zone="western"
    weight = 10
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_n_result_460():
    zone="northern"
    weight = 10
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_ne_result_460():
    zone="northeastern"
    weight = 10
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_10_zone_s_result_460():
    zone="southern"
    weight = 10
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_c_result_420():
    zone="central"
    weight = 15
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_e_result_420():
    zone="eastern"
    weight = 15
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_w_result_420():
    zone="western"
    weight = 15
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_n_result_460():
    zone="northern"
    weight = 15
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_ne_result_460():
    zone="northeastern"
    weight = 15
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_15_zone_s_result_460():
    zone="southern"
    weight = 15
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_20_zone_c_result_420():
    zone="central"
    weight = 20
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_20_zone_e_result_420():
    zone="eastern"
    weight = 20
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_20_zone_w_result_420():
    zone="western"
    weight = 20
    expected_result = 420
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_20_zone_n_result_460():
    zone="northern"
    weight = 20
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_20_zone_ne_result_460():
    zone="northeastern"
    weight = 20
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result
@pytest.mark.validate
def test_weight_20_zone_s_result_460():
    zone="southern"
    weight = 20
    expected_result = 460
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result
    
@pytest.mark.validate
def test_weight_9_zone_c_result_200():
    zone="central"
    weight = 9
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_9_zone_e_result_200():
    zone="eastern"
    weight = 9
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_9_zone_w_result_200():
    zone="western"
    weight = 9
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_9_zone_n_result_200():
    zone="northern"
    weight = 9
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_9_zone_ne_result_200():
    zone="northeastern"
    weight = 9
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_9_zone_s_result_200():
    zone="southern"
    weight = 9
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_c_result_200():
    zone="central"
    weight = 1.1
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_e_result_200():
    zone="eastern"
    weight = 1.1
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_w_result_200():
    zone="western"
    weight = 1.1
    expected_result = 200
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_n_result_200():
    zone="northern"
    weight = 1.1
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_ne_result_200():
    zone="northeastern"
    weight = 1.1
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_1_1_zone_s_result_200():
    zone="southern"
    weight = 1.1
    expected_result = 240
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_c_result_200():
    zone="central"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_e_result_200():
    zone="eastern"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_w_result_200():
    zone="western"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_n_result_200():
    zone="northern"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_ne_result_200():
    zone="northeastern"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result

@pytest.mark.validate
def test_weight_m1_1_zone_s_result_200():
    zone="southern"
    weight = -1.1
    expected_result = "Impossible, the weight's out of range."
    actual_result = calculate_express(weight,zone)
    assert expected_result == actual_result
