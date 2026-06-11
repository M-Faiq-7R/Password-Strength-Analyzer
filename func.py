def analyze_p(password):
    score = 0
    # Data required to compare
    message = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    c_alphabets = alphabets.upper()
    s_charecters = '!@#$%^&*()}|:{?><|~`'
    numbers = '0123456789'
    common_passwords = ['qwerty' , 'password' ,'nigga' , 'modilovemeloni']

    # Scoring
    if any(cp in password.lower() for cp in common_passwords):
        score = 0
        message.append("Common Password")
    else:
        if len(password) >= 12:
            score = score + 4
        elif len(password) >= 8:
            score = score + 2
        else:
            message.append("Password too short.")
            #################################
        if any(letter in password for letter in alphabets):
            score = score + 1
        else:
            message.append("No lower case letter in password.")
            #################################
        if any(letter in password for letter in c_alphabets):
            score = score + 1
        else:
            message.append("No Upper case letter in password.")
            #################################
        if any(digit in password for digit in numbers):
            score = score + 1
        else:
            message.append("No numbers in password.")
            #################################
        if any(char in password for char in s_charecters):
            score = score + 2
        else:
            message.append("No Special Characters in password.")
            #################################
        
    
    return score , message