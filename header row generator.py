#please enter the input records with done as last record
string_list = []

while True:
    user_input = input("\n")
    if user_input.lower() =='done':
        break
    string_list.append(user_input)

single_row = "|".join(string_list)
print(single_row)