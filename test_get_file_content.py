from functions.get_file_content import get_file_content
from constants import MAX_CHARS

def test():
    #Test case 0: lorem ipsum
    result = get_file_content("calculator", "lorem.txt",MAX_CHARS)
    print("Result for lorem ipsum file:")
    print(len(result), result)
    print("")

    # Test case 1: Current directory
    result =get_file_content("calculator", "main.py",MAX_CHARS)
    print("Result for main.py file:")
    print(result)
    print("")

    # Test case 2: 'pkg' directory
    result=get_file_content("calculator", "pkg/calculator.py",MAX_CHARS)
    print("Result for 'calculator.py' file:")
    print(result)
    print("")

    # Test case 3: Invalid directory outside working_directory
    result = get_file_content("calculator", "/bin/cat",MAX_CHARS)
    print("Result for '/bin/cat' file:")
    print(result)
    print("")

    # Test case 4: Another invalid directory outside working_directory
    result = get_file_content("calculator", "pkg/does_not_exist.py",MAX_CHARS)
    print("Result for an non existing file:")
    print(result)
    print("")


if __name__ == "__main__":
    test()

"""
get_file_content("calculator", "main.py")
get_file_content("calculator", "pkg/calculator.py")
get_file_content("calculator", "/bin/cat") (this should return an error string)
get_file_content("calculator", "pkg/does_not_exist.py")
"""
