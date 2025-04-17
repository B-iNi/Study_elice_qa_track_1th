import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from utils import generate_new_user, random_string
from common import dummy_data, url_endpoint
import copy
import pytest
import requests

#테스트 주체
class TestUserSginup():
   signup_nomotopic_data = generate_new_user.generate_new_user(copy.deepcopy(dummy_data.SIGNUP_USER_NOMOTOPIC)) #원본 영향 없게 만들기기
   signup_exection_data = copy.deepcopy(dummy_data.SIGNUP_USER_EXCEPTION)
   url = url_endpoint.USER_URL

   @pytest.mark.parametrize("username, email, password, passwordConfirm", signup_nomotopic_data)
   def test_singup_nomotopic(self, username, email, password, passwordConfirm):
      try:
         payload = {
         "username": username,
         "email": email,
         "password": password,
         "passwordConfirm": passwordConfirm
        }

         response = requests.post(f'{self.url}/signup', payload)
         successfully_status_code = 200
         must_status_code = 201
         status_code = response.status_code

         must_message = "You have successfully signed up"
         response_message = response.json()["message"]

         #성공 여부 판단
         print('성공 여부 판단')
         assert successfully_status_code == status_code or status_code == must_status_code
         
         #상태 코드 판단
         print('상태 코드 판단')
         assert status_code == must_status_code

         #성공 메세지 판단
         print('리턴값 명세서 일치 판단')
         assert must_message == response_message

         print('성공 직접 조회 판단')
         user_data = requests.get(f'{self.url}?search={username}').json()[0]
         assert username == user_data["username"]
         assert email == user_data["email"]

      except Exception as e:
         pytest.fail(e)


   def test_singup_email_exection(self):
      try:
         email_formet = self.signup_exection_data["EMAIL_FORMAT"]
         response = requests.post(f'{self.url}/signup', email_formet)

         must_status_code = 400
         status_code = response.status_code

         must_message = "Email is not formatted correctly"
         response_message = response.json()["message"]

         #상태 코드 판단
         print('상태 코드 판단')
         assert status_code == must_status_code

         #성공 메세지 판단
         print('리턴값 명세서 일치 판단')
         assert must_message == response_message

      except Exception as e:
         pytest.fail(str(e))

#반드시 실패해야함. API가 잘 못만듬
   def test_singup_password_confirm_exection(self):
      try:
         payload = self.signup_exection_data["DIFFENT_PASSWORD_AND_CONFIRM"]
         payload["username"] = random_string.generate_string()
         payload["email"] = f'${random_string.generate_string()}@naver.com'
         response = requests.post(f'{self.url}/signup', payload)

         must_status_code = 400
         status_code = response.status_code

         must_message = "비밀번호와 확인용 비밀번호가 다릅니다." #임의로 합니다. 해놓은게 없어요 
         reasponse_data = response.json()

         #상태 코드 판단
         print('상태 코드 판단')
         assert status_code == must_status_code

         #성공 메세지 판단
         print('리턴값 명세서 일치 판단')
         assert must_message == reasponse_data["message"]

      except Exception as e:
         pytest.fail(str(e))


   @pytest.mark.parametrize("dummy_data", signup_exection_data["FIELD_NULL"])
   def test_singup_null_field_exection(self, dummy_data):
      try:
         print(f'\n test_data: {dummy_data}')
         response = requests.post(f'{self.url}/signup', dummy_data)

         must_status_code = 400
         status_code = response.status_code

         must_message = "All fields are required" #임의로 합니다. 해놓은게 없어요 
         reasponse_data = response.json()

         #상태 코드 판단
         print('상태 코드 판단')
         assert status_code == must_status_code

         #성공 메세지 판단
         print('리턴값 명세서 일치 판단')
         assert must_message == reasponse_data["message"]

      except Exception as e:
         pytest.fail(str(e))

   @pytest.mark.parametrize("dummy_data", signup_exection_data["UNIQ_ORVERLAP"])
   def test_z_singup_uniq_exection(self, dummy_data):
      try:
         print(f'\n test_data: {dummy_data}')
         response = requests.post(f'{self.url}/signup', dummy_data)

         must_status_code = 400 #409 <--- 명세서
         status_code = response.status_code

         must_message = "already exists" #임의로 합니다. 해놓은게 없어요 
         reasponse_data = response.json()

         #상태 코드 판단
         print('상태 코드 판단')
         assert status_code == must_status_code

         #성공 메세지 판단
         print('리턴값 명세서 일치 판단')
         assert must_message in reasponse_data["message"]

      except Exception as e:
         pytest.fail(str(e))

         