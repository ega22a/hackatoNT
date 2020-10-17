from search_function import search_users
import os

f = open(os.path.abspath('token.txt'),'r')
token_vk = f.read()
def gate_function(town,sex,token=token_vk):
        town = town[:13]
        print(token)
        return search_users(town,sex,token)  
f.close()
