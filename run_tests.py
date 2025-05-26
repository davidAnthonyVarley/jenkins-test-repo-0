import os

def test1():
    return True

def test2():
    return True

def test3():
    return True

def test4():
    return True

def test5():
    return True

def test6():
    return True

def test7():
    return True

def test8():
    return True

def test9():
    return True

def test10():
    return False
    #return True

def run_tests(tests):
    num_successful_tests = 0
    for test in tests:
        if ( test()):
            num_successful_tests+=1
    
    return num_successful_tests


def update_env_file(filename, key, value):
    # Read lines
    lines = []
    found = False
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(f"{key}="):
                lines.append(f"{key}={value}\n")
                found = True
            else:
                lines.append(line)
        # Add if key not found
        if not found:
            lines.append(f"{key}={value}\n")
        # Write back
        with open(filename, 'w') as file:
            file.writelines(lines)







tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10]

num_tests = len(tests)
number_of_successful_tests = run_tests(tests)

print("num_tests:",num_tests)
print("number_of_successful_tests:",number_of_successful_tests)

update_env_file('.env', 'NUMBER_OF_TESTS', str(num_tests))
update_env_file('.env', 'SUCCESSFUL_TESTS', str(number_of_successful_tests))






