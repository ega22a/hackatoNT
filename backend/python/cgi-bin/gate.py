from search_function import search_users

f = open('1.txt','r')
token_vk = f.read()
def gate_function(town,sex,token=token_vk):
        town = town[:13]
        return search_users(town,sex,token)  
