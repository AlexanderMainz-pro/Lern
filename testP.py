input_str = input()
first_str, second_str = input_str.split()
tri_str = first_str[:len(second_str)]
index_str = tri_str[1::2]
index_str2 = second_str[1::2]
result = index_str == index_str
print(result)
