
def read_data_from_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        headers = [header.strip() for header in lines[0].split(',')]
        for line in lines[1:]:
            values = [value.strip() for value in line.split(',')]
            data.append(dict(zip(headers, values)))
    
    return data


def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    output =[]
    for user in data:
        dict1={}
        user =user[1:-3]
        list1 = user.split(",")
        for kv in list1:
            kv = kv.replace(" ","")
            kv = kv.replace('"',"")
            finalList = kv.split(":")
           
            dict1[finalList[0]]=finalList[1]
        output.append(dict1)
        
    return output

dataex = [
    {"username": "bossB", "roll": "student", "first": "barret", "last": "newton", "user_id": "3", "password": "dde", "email": "dd@tet.com"},
    {"username": "goodd", "roll": "student", "first": "andy", "last": "newton", "user_id": "3", "password": "sdf", "email": "dd@tet.com"},
    {"username": "bergyboy", "roll": "administrator", "first": "rosco", "last": "berg", "user_id": "3", "password": "dittle", "email": "dd@tt.org"},
    {"username": "sam", "roll": "administrator", "first": "sambo", "last": "bergly", "user_id": "3", "password": "ffd", "email": "dd@tt.org"}
]




if __name__ == "__main__":
    md = read_data("users.json")
    print(dataex)
    print()
    print("bad")
    print(md)
    
     
    
  