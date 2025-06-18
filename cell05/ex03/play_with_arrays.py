old_array = [1, 2, 3, 4, 5, 6, 3, 4] 
new_array = list(dict.fromkeys(old_array)) 
print("old_array:", old_array)
print("new_array:", new_array)