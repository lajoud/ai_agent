from functions.run_python_file import run_python_file

def test():
    # Test case 1: Current directory
    result=run_python_file("calculator", "main.py")
    print("Result for run_python main.py, (should print the calculator's usage instructions) ")
    print(result)
    print("")

    # Test case 2: 'pkg' directory
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Should run the calculator... which gives a kinda nasty rendered result")
    print(result)
    print("")

    # Test case 3: Invalid directory outside working_directory
    result = run_python_file("calculator", "tests.py")
    print("should run the calculator's tests successfully")
    print(result)
    print("")

    # Test case 4: 
    result = run_python_file("calculator", "../main.py")
    print("this should return an error")
    print(result)
    print("")
    
    # Test case 5: 
    result = run_python_file("calculator", "nonexistent.py")
    print("this should return an error")
    print(result)
    print("")
    
    # Test case 6: 
    result = run_python_file("calculator", "lorem.txt")
    print("this should return an error")
    print(result)
    print("")
    
if __name__ == "__main__":
    test()