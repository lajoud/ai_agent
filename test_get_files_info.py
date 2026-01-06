from functions.get_files_info import get_files_info


def test():
    # Test case 1: Current directory
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    # Test case 2: 'pkg' directory
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("")

    # Test case 3: Invalid directory outside working_directory
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    # Test case 4: Another invalid directory outside working_directory
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("")


if __name__ == "__main__":
    test()