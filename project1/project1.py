import hashlib

User_database = [{
    "username":"alice",
    "hashed_pwd":"ba56bc223884c4f9b0757f497c9676ba"
},{
    "username":"bob",
    "hashed_pwd":"85cc5de8c37b686c2839b4252c5c3413"
},
{
    "username": "charlie",
    "hashed_pwd": "9f9fc5784d2739d1be341586fb5513ef"
},
{
    "username": "daniel",
    "hashed_pwd": "aaf41498cc721410a036ec4eabd3af74"
}
,{
    "username": "emily",
    "hashed_pwd": "64f693351e8e0f3c7fc51d1220a5512f"
}]

def login(username,password):
    # Do not modify this function.
    is_logged_in = False
    salt = "abcde"
    db_password = password + salt
    for user in User_database:
        if username == user["username"]:
            if hashlib.md5(db_password.encode()).hexdigest() == user["hashed_pwd"]:
                is_logged_in = True
    return is_logged_in


def main():
    # Transform text file into a list that contains all the passwords
    # The text file need to be in the same folder than this python script
    my_file = open("best1050.txt", "r") 
    pwd = my_file.read() 
    pwd_into_list = pwd.split("\n") 

    # Run through the different username
    for user in User_database: 
        # Try each password from the list of password
        for password in pwd_into_list: 
            # If the password is correct for the username
            if login(user["username"], password): 
                # Print the password
                print(user["username"]+"'s password is", password)
    return 

if __name__ == '__main__':
    main()

