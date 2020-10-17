from search_function import search_users

token_vk = "19a97bc8cfdf0a8706433f5a0308c70613510ac6c5f3c43bdd6adf05ff2325ad7c96ace22a38cb9bf1ede"

def gate_function(town,sex,token=token_vk):
        town = town[:13]
        return search_users(town,sex,token)  
