from discount import calculate_discount

def test_vip_customer():

    assert(calculate_discount(60000000) == 90)

def test_normal_customer():

    assert(calculate_discount(300000000) == 10)