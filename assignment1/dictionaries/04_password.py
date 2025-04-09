import hashlib

def hash_password(password):
    # Convert password to bytes, then hash using SHA256
    return hashlib.sha256(password.encode()).hexdigest()


stored_logins = {
    "laiba@example.com": hash_password("laiba123"),
    "ali@example.com": hash_password("mypassword"),
    "fatima@example.com": hash_password("securepass"),
}

def login(email, password_to_check):
    # Hash the password provided by the user
    hashed_input = hash_password(password_to_check)

    # Check if email exists and hashed password matches
    return stored_logins.get(email) == hashed_input

# Testing the login function
print(login("laiba@example.com", "laiba123"))    
print(login("ali@example.com", "wrongpass"))     
print(login("unknown@example.com", "abc123"))    

