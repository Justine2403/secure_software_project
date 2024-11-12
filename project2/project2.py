import unittest

Role_database = [
    {"id":1,
     "name":"root"},
    {"id":2,
     "name":"admin"},
    {"id":3,
     "name":"developer"},
    {"id":4,
     "name":"customer"}
]

User_database = [{
    "id":"7nWRXeFU",
    "username":"alice",
    "password":"alice123"
},{
    "id":"KnpLyeM6",
    "username":"bob",
    "password":"bob123"
},
{
    "id": "GPclfiZW",
    "username": "charlie",
    "password": "charlie123"
}
,{
    "id":"QP4pOQi9",
    "username":"daniel",
    "password":"daniel123"
},{
    "id":"6XtYUnY6",
    "username":"emily",
    "password":"emily123"
}]

def mapping(user_id):
    #Map user_id from User_database to role_id from Role_database
    # Attributing the role ID for each user depending on the table on the subject
    role_id = ""
    for user in User_database:
        if user["id"] == user_id:
            if user["id"] == "GPclfiZW": # Charlie
                role_id = 1
            if user["id"] == "QP4pOQi9": # Daniel
                role_id = 2
            if user["id"] == "7nWRXeFU": # Alice
                role_id = 3
            if user["id"] == "6XtYUnY6" or user["id"] == "KnpLyeM6": # Emily or Bob
                role_id = 4
    return role_id

def login(username,password):
    # Verify username and password from database
    # Return the user's id
    user_id = ""
    for user in User_database:
        if user["username"] == username and user["password"] == password:
            user_id = user["id"]
    return user_id

def execute(user_id, file_name, string_data, flag):
    role_id = mapping(user_id)
    # Defining the access control for each role (cf. table in the subject)
    
    if role_id == 4:  # Customer
        if file_name in ["c.txt", "d.txt"] and flag == "R":
            return read_file(file_name)
        else:
            return "Access Denied"
    
    elif role_id == 3:  # Developer
        if file_name in ["c.txt", "d.txt"]:
            if flag == "W":
                write_file(file_name, string_data)
                return "Write Success"
            elif flag == "R":
                return read_file(file_name)
        elif file_name == "b.txt" and flag == "R":
            return read_file(file_name)
        else:
            return "Access Denied"
    
    elif role_id == 2:  # Admin
        if file_name in ["b.txt", "c.txt", "d.txt"]:
            if flag == "W":
                write_file(file_name, string_data)
                return "Write Success"
            elif flag == "R":
                return read_file(file_name)
            else:
                return "Access Denied"
    
    elif role_id == 1:  # Root
        if file_name in ["a.txt", "b.txt", "c.txt", "d.txt"]:
            if flag == "W":
                write_file(file_name, string_data)
                return "Write Success"
            elif flag == "R":
                return read_file(file_name)
    
    return "Access Denied"

def read_file(file_name):
    # Read the entire content of the file
    with open(file_name, "r") as file:
        return file.read()

def write_file(file_name, string_data):
    # Append string_data to file not overwrite the whole file
    # Use "a" instead of "w"    
    with open(file_name, "a") as file:
        file.write(string_data)
  
# Empty the files to make sure that the code works from the start without overwriting
file_list = ["a.txt","b.txt", "c.txt", "d.txt"]     
for i in range (len(file_list)):
    open(file_list[i], "w").close()

# Do not modify after this line.
# a.txt, b.txt, c.txt, d.txt should all be empty before test
class TestProject1(unittest.TestCase):

    def test_CHARLIE_WRITE_TO_FILE_A_THEN_READ(self):
        self.assertEqual(execute(login("charlie", "charlie123"), "a.txt", "CCC", "W"), 'Write Success')
        self.assertEqual(execute(login("charlie", "charlie123"), "a.txt", "CCC", "R"), 'CCC')
        self.assertEqual(execute(login("daniel", "daniel123"), "a.txt", "DDD", "W"), 'Access Denied')
        self.assertEqual(execute(login("daniel", "daniel123"), "a.txt", "DDD", "R"), 'Access Denied')
        self.assertEqual(execute(login("alice", "alice123"), "a.txt", "AAA", "W"), 'Access Denied')
        self.assertEqual(execute(login("alice", "alice123"), "a.txt", "AAA", "R"), 'Access Denied')
        self.assertEqual(execute(login("bob", "bob123"), "a.txt", "BBB", "W"), 'Access Denied')
        self.assertEqual(execute(login("bob", "bob123"), "a.txt", "BBB", "R"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "a.txt", "EEE", "W"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "a.txt", "EEE", "R"), 'Access Denied')
    def test_CHARLIE_WRITE_TO_FILE_B_THEN_READ(self):
        self.assertEqual(execute(login("charlie", "charlie123"), "b.txt", "CCC", "W"), 'Write Success')
        self.assertEqual(execute(login("charlie", "charlie123"), "b.txt", "CCC", "R"), 'CCC')
        self.assertEqual(execute(login("daniel", "daniel123"), "b.txt", "DDD", "W"), 'Write Success')
        self.assertEqual(execute(login("daniel", "daniel123"), "b.txt", "DDD", "R"), 'CCCDDD')
        self.assertEqual(execute(login("alice", "alice123"), "b.txt", "AAA", "W"), 'Access Denied')
        self.assertEqual(execute(login("alice", "alice123"), "b.txt", "AAA", "R"), 'CCCDDD')
        self.assertEqual(execute(login("bob", "bob123"), "b.txt", "BBB", "W"), 'Access Denied')
        self.assertEqual(execute(login("bob", "bob123"), "b.txt", "BBB", "R"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "b.txt", "EEE", "W"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "b.txt", "EEE", "R"), 'Access Denied')
    def test_CHARLIE_WRITE_TO_FILE_C_THEN_READ(self):
        self.assertEqual(execute(login("charlie", "charlie123"), "c.txt", "CCC", "W"), 'Write Success')
        self.assertEqual(execute(login("charlie", "charlie123"), "c.txt", "CCC", "R"), 'CCC')
        self.assertEqual(execute(login("daniel", "daniel123"), "c.txt", "DDD", "W"), 'Write Success')
        self.assertEqual(execute(login("daniel", "daniel123"), "c.txt", "DDD", "R"), 'CCCDDD')
        self.assertEqual(execute(login("alice", "alice123"), "c.txt", "AAA", "W"), 'Write Success')
        self.assertEqual(execute(login("alice", "alice123"), "c.txt", "AAA", "R"), 'CCCDDDAAA')
        self.assertEqual(execute(login("bob", "bob123"), "c.txt", "BBB", "W"), 'Access Denied')
        self.assertEqual(execute(login("bob", "bob123"), "c.txt", "BBB", "R"), 'CCCDDDAAA')
        self.assertEqual(execute(login("emily", "emily123"), "c.txt", "EEE", "W"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "c.txt", "EEE", "R"), 'CCCDDDAAA')
    def test_CHARLIE_WRITE_TO_FILE_D_THEN_READ(self):
        self.assertEqual(execute(login("charlie", "charlie123"), "d.txt", "CCC", "W"), 'Write Success')
        self.assertEqual(execute(login("charlie", "charlie123"), "d.txt", "CCC", "R"), 'CCC')
        self.assertEqual(execute(login("daniel", "daniel123"), "d.txt", "DDD", "W"), 'Write Success')
        self.assertEqual(execute(login("daniel", "daniel123"), "d.txt", "DDD", "R"), 'CCCDDD')
        self.assertEqual(execute(login("alice", "alice123"), "d.txt", "AAA", "W"), 'Write Success')
        self.assertEqual(execute(login("alice", "alice123"), "d.txt", "AAA", "R"), 'CCCDDDAAA')
        self.assertEqual(execute(login("bob", "bob123"), "d.txt", "BBB", "W"), 'Access Denied')
        self.assertEqual(execute(login("bob", "bob123"), "d.txt", "BBB", "R"), 'CCCDDDAAA')
        self.assertEqual(execute(login("emily", "emily123"), "d.txt", "EEE", "W"), 'Access Denied')
        self.assertEqual(execute(login("emily", "emily123"), "d.txt", "EEE", "R"), 'CCCDDDAAA')


if __name__ == '__main__':
    unittest.main()