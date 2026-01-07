from functions.write_file import write_file


def test():
    # Test case 1: Current directory
    result=write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to lorem ipsum")
    print(result)
    print("")

    # Test case 2: 'pkg' directory
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to a non existing file")
    print(result)
    print("")

    # Test case 3: Invalid directory outside working_directory
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("result for writing to a dir outout of reach:")
    print(result)
    print("")


if __name__ == "__main__":
    test()