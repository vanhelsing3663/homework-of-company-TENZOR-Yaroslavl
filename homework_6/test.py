import password_validate as passwd
import sum_args
import fib

'''Test'''


def test_password_check_password_len():
    assert passwd.password('a') == False


def test_password_check_digits_count():
    assert passwd.password('qwertyuiolhfdmvcd jsvndmsv') == False


def test_password_check_not_only_digits():
    assert passwd.password('00000000000000012010303103001031001301') == False


def test_password_checker_validate_passwd():
    assert passwd.password('konnovk12345p') == True


def test_password_checker_validate_passwd_2():
    assert passwd.password('kirill200320230dsds') == True


def test_sum_of_all_1_2_3():
    assert sum_args.adder([1, 2, 3]) == 6


def test_sum_of_all_08_077():
    assert sum_args.adder([0.8, 0.77]) == 1.57


def test_sum_of_all_nothing():
    assert sum_args.adder([]) == 0


def test_fibo_11():
    assert Fibonachi.fibonacci(11) == 89


def test_fibo_4():
    assert Fibonachi.fibonacci(4) == 3


def test_fibo_9():
    assert Fibonachi.fibonacci(9) == 34
