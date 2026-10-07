# # Attribute error
# try:
#     n = 10
#     n.append(5)
#     print(n)
# except AttributeError as a:
#     print(f"integer doesn't have append method {a}")
    
# # Import error
# try:
#     from math import xyz
#     print(xyz)
# except ImportError as i:
#     print(f"module not found {i}")

# # File not Found Error
# try:
#     f = open('data.txt')
#     print(f.read())
# except FileNotFoundError as f:
#     print(f"cannot find the specified file {f}")

# File Exists error
# try:
#     f = open("data1.txt","x")
# except FileExistsError as f:
#     print(f"when trying to create a file that already exists using create mode {f}")

# # ModuleNotFoundError
# try:
#     import abcxyz
# except ModuleNotFoundError as m:
#     print(f"cannot find the module we are trying to import;>{m}")