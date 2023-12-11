# contains functions to validate user inputs
class Validator():
    # returns boolean list. Each boolean value represents a requirement:
    # [length, has_uppercase, has_lowercase, has_special_character, has_number]
    def new_password(input_password):
        special_char_set = {'~','`','!','@','#','$', '%','^','&','*','(',')','-','_','+','=','{','[','}',']','|','\\',';',':','\'','"',',','<','.','>','/','?'}
        length = len(input_password) >= 12
        has_uppercase = False
        has_lowercase = False
        has_special_character = False
        has_number = False

        for char in input_password:
            if not has_uppercase and char.isupper():
                has_uppercase = True
            elif not has_lowercase and char.islower():
                has_lowercase = True
            elif not has_special_character and char in special_char_set:
                has_special_character = True
            elif not has_number and char.isnumeric():
                has_number = True

        return [length, has_uppercase, has_lowercase, has_special_character, has_number]
    
    # returns true or false based on basic checks
    def email(input_email):
        special_char_set = {'~','`','!','@','#','$', '%','^','&','*','(',')','-','_','+','{','[','}',']','|',';',':',',','<','.','>','?'}

        for char in input_email:
            if not char.isalpha():
                if not char.isnumeric():
                    if char not in special_char_set:
                        return False
        
        # email addresses with doubled @ symbol also aren't valid
        if "@@" in input_email:
            return False

        return True