from pydantic import BaseModel,EmailStr
from enum import Enum
import json
class Roll(str, Enum):
    student ="student"
    educator="educator"
    administrator="administrator"
    staff="staff"
    temp="temp"

    

    
class User(BaseModel):
    roll: Roll
    username: str
    first: str
    last: str
    user_id: int
    password: str
    email: EmailStr |None = None










def spell_number(num: int, multiply_by_2: bool = False):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert (0 <= num)

    if multiply_by_2:
        num *= 2

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + spell_number(num % 100)

    if num < m:
        if num % k == 0:
            return spell_number(num // k) + ' thousand'
        else:
            return spell_number(num // k) + ' thousand, ' + spell_number(num % k)

    if num < b:
        if (num % m) == 0:
            return spell_number(num // m) + ' million'
        else:
            return spell_number(num // m) + ' million, ' + spell_number(num % m)

    if num < t:
        if (num % b) == 0:
            return spell_number(num // b) + ' billion'
        else:
            return spell_number(num // b) + ' billion, ' + spell_number(num % b)

    if num % t == 0:
        return spell_number(num // t) + ' trillion'
    else:
        return spell_number(num // t) + ' trillion, ' + spell_number(num % t)
    
    
def save_to_file(user:User) ->bool:
    with open("users.json","a") as outfile:
        json.dump(user,outfile)
        outfile.write(",\n")
    
    return True


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