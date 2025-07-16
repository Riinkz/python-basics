# 1
example = "example"
print(example.count("e"))                       # 2

# 2
encode_example = "Ruhestörung"
print(encode_example.encode())                  # b'Ruhest\xc3\xb6rung'

# 3
strip_example = "     python programming  "
print(strip_example.strip())                    # python programming

# 4
print(example.replace("e", "r"))                # rxamplr
print("py" in strip_example)                    # True
print("clothes" not in strip_example)           # True