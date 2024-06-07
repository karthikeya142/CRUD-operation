
import  json
import os
def read_user_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_list = json.load(file)
            for user_data in user_list:
                print("Name:", user_data["name"])
                print("Email:", user_data["email"])
                print("Contact:", user_data["contact"])
                print("")
    else:
        print("No User data found")
        return
