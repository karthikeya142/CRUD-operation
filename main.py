import edit_usr_data
import retrive_old_data
from delete_usr_data import delete_user_data
from edit_usr_data import read_user_data, edit_user_data
import retrive_old_data


read_user_data()
retrive_old_data.retri_user_data_()
edit_name = input("\n Enter name which you want add data for: ")
edit_user_data(edit_name)
delete_name = input("\n Enter name which you want  delete: ")
delete_user_data(delete_name)
read_user_data()
