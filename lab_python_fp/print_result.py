def print_result(func):
    def printer(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            print("\n".join(map(str, result)))
        elif isinstance(result, dict):
            print("\n".join(f"{k} = {v}" for k, v in result.items()))
        else:
            print(result)
        return result
    return printer

if __name__ == '__main__':
    @print_result
    def test_1():
        return 1

    @print_result
    def test_2():
        return 'iu5'

    @print_result
    def test_3():
        return {'a': 1, 'b': 2}

    @print_result
    def test_4():
        return [1, 2]

    test_1()
    test_2()
    test_3()
    test_4()
