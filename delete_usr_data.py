import json
import os.path


def delete_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found!")
        return
    with open("user_data.json",'r') as file:
        user_list = json.load(file)
        file.close()
    user_found = False
    for user_data in user_list:
        if user_data['name'] == name:
            user_list.remove(user_data)
            user_found = True
            break
    if not user_found:
        print("User Not Found")

    with open('user_data.json','w') as file:
        json.dump(user_list,file)
        print("\n User data deleted successfully")
