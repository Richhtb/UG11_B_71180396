def check_data_type(obj, type_check):
    type_check = type_check.lower()
    type_obj = str(type(obj)).split()[1].replace("'","").replace('>','')
    if type_obj == type_check:
        print('Jawaban Anda benar')
        return True
    print(f'Jawaban Anda salah, seharusnya adalah: {type_obj}')
    return False    
print(check_data_type("Kevin","STr")) 
print(check_data_type("Kevin","str")) 
print(check_data_type(12345,"str")) 
print(check_data_type("9347","int"))
print(check_data_type(9876,"int")) 