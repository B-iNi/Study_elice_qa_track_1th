import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from utils import random_string
import copy
from common import user_respone_format

def generate_new_user(signup_nomotopic_data):
   for i in range(0, 3):
      new_user_data = copy.deepcopy(user_respone_format.SIGNUP_FORMAT)
      new_user_data["username"] = random_string.generate_string()
      new_user_data["email"] = f'{random_string.generate_string()}@naver.com'
      password = random_string.generate_string()
      new_user_data["password"] = password
      new_user_data["passwordConfirm"] = new_user_data["password"] = password
      signup_nomotopic_data.append((new_user_data["username"], new_user_data["email"], new_user_data["password"],new_user_data["passwordConfirm"]))
    
   return signup_nomotopic_data
   