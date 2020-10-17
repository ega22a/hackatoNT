import vk_api
from time import time

start = time()




object_name = "Работа"
#sex = 0 # 0 - не имеет значения, 1 - мужчина, 2 - женщина

def search_users(town_name,sex,token):#token = ""
    vk = vk_api.VkApi(token=token)
    vk._auth_token()

    #print('Авторизовано')
    #Переменные для статистики
    banned_users = 0
    closed_users = 0
    finded_users = 0
    finded_sex_users = 0
    finded_town_users = 0
    not_finded_town_users = 0
    repeat_users = 0

    #Конечная выходная переменная
    end_json = {"id": 0,
                "name": "",
                "city": "",
                "sex": 0,
                "education": "",
                "education_area": "",
                "bdate": "",
                "points": 0}
    #
    number_phone_allow_symbols = ['+','0','1','2','3','4','5','6','7','8','9']
    json_list = ["id","name","city","sex","education","education_area","bdate",'mobile_phone',"points"]
    end_list = []

    def decor():
        #print('\n'*3)
        a = 0
        

    city_info = vk.method("database.getCities", {"q": town_name, "country_id": 1, "need_all": 0})
    #print(city_info)
    city_id = city_info["items"][0]["id"]
    town_name = city_info["items"][0]['title']
    decor()

    q = object_name + " " + town_name
    groups = vk.method("groups.search", {"city_id":city_id, "q":q, "count": 5})["items"]

    #ПЕРЕЧИСЛЕНИЕ ГРУПП

    for i in groups:
        #print("id: {}".format(i['id'])+' name: {}'.format(i['name']))
        #print()

    decor()

    #перечисление юзеров

    kash_id = []

    for i in groups:
        #print(i['name'])
        x = 100 #Множитель числа участников выборки
        offset = 0 #Больший обхват
        for k in range(0,10):
            offset = int(k * x)       #id, sex, bdate, city, contacts, education
                                    #lists
            kash_groups_people = vk.method("groups.getMembers", {"group_id":i['id'], "offset": offset, "count":x, "fields":"sex, bdate, city, contacts, education"})['items']
            #print(kash_groups_people)
            for j in kash_groups_people:
                finded_users += 1
                try:
                    #print(j["is_closed"])
                    if j['is_closed'] == False:     #Рабочая область, открыт профиль и не в бане
                        if j['sex'] != sex:                        
                            finded_sex_users += 1
                            try:
                                if j["city"]["title"] == town_name:
                                    finded_town_users += 1
                                    if j['id'] not in kash_id:
                                        #json_list = ["id","name","city","sex","education","education_area","bdate",'mobile_phone',"points"]
                                        kash_id.append(j['id'])
                                        kash_to_json = [j['id'],j['first_name']+" "+j['last_name'],town_name]
                                        kash_points = 0
                                    
                                        if j['sex'] == 2:
                                            kash_to_json.append("Мужской")
                                        else:
                                            kash_to_json.append("Женский")

                                        try:
                                            if j['faculty'] == 0:
                                                kash_to_json.append("Н/У")
                                            else:
                                                kash_to_json.append(j['faculty_name'])
                                                kash_points += 1
                                        except:
                                            kash_to_json.append("Н/Д")

                                        try:
                                            if j['university'] == 0:
                                                kash_to_json.append("Н/У")
                                            else:
                                                kash_to_json.append(j['university_name'])
                                                kash_points += 1
                                        except:
                                            kash_to_json.append("Н/Д")

                                        try:
                                            if len(str(j["bdate"])) > 1:
                                                kash_to_json.append(str(j["bdate"]))
                                                kash_points += 1
                                        except:
                                            kash_to_json.append("Н/Д")

                                        kash_mobile_phone = str(j['mobile_phone'])
                                        mobile_phone = ''
                                        if len(kash_mobile_phone) > 8:
                                            if int(kash_mobile_phone[0]) == 9:
                                                mobile_phone += '+7'
                                            if int(kash_mobile_phone[0]) == 8:
                                                mobile_phone += '+7'
                                            for ii in range(1,len(kash_mobile_phone)):
                                                #print(kash_mobile_phone[ii],kash_mobile_phone[ii] in number_phone_allow_symbols)
                                                if kash_mobile_phone[ii] in number_phone_allow_symbols:
                                                    mobile_phone += str(kash_mobile_phone[ii])
                                            #print(kash_mobile_phone, ' === ', mobile_phone)
                                        try:
                                            if len(mobile_phone) < 11:
                                                kash_to_json.append("Н/У")
                                            else:
                                                kash_to_json.append(mobile_phone)
                                                kash_points += 1
                                        except:
                                            kash_to_json.append("Н/Д")
                                        
                                        kash_to_json.append(kash_points)
                                        
                                        
                                        #print(len(kash_to_json),"   ", kash_to_json)
                                    
                                        step_kash_list = []
                                    
                                        for l in range(len(kash_to_json)):
                                            step_kash_list.append([json_list[l],kash_to_json[l]])

                                        end_list.append(dict(step_kash_list))
                                    else:
                                        repeat_users += 1
                            except:
                                #print("Город не указан \n", j)
                                not_finded_town_users += 1
                    else:
                        closed_users += 1
                except:
                    banned_users += 1

    decor()

    #print("Найдено {} пользователей, среди них {} забаненно и {} закрыли страничку. \nПо полу подошло {} пользователей.\nВ нужном городе из них {} пользователей\nГород скрыт у {} пользователей".format(finded_users,banned_users,closed_users, finded_sex_users, finded_town_users, not_finded_town_users))
    #print("Повтор пользователей в группах встретился {} раз.".format(repeat_users))

    #print("Прошло {} секунд".format(time()-start))

    decor()
    for item in end_list:
        print(item)
    #print(len(end_list))
