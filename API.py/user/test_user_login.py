import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from common import dummy_data, url_endpoint
import copy
import pytest
import requests

#테스트 주체
class TestUserLogin():
   login_nomotopic_data = copy.deepcopy(dummy_data.LOGIN_USER) #원본 영향 없게 만들기기
   login_exection_data = copy.deepcopy(dummy_data.LOGIN_USER_EXCEPTION)
   url = url_endpoint.USER_URL

   @pytest.mark.parametrize("dummy_data", login_nomotopic_data)
   def test_login_nomotopic(self, dummy_data):
      try:
         payload = {
            "email": dummy_data["email"],
            "password": dummy_data["password"]
         }

         response = requests.post(self.url+'/login', payload)
         must_status_code = 200
         
         assert must_status_code == response.status_code
         assert "requests.cookies.RequestsCookieJar" in str(type(response.cookies))

         me = requests.get(self.url+'/me', cookies=response.cookies).json()
         print(f'\n {me}')
         assert dummy_data["email"] == me["email"] 
         assert dummy_data["username"] == me["username"]

      except Exception as e:
         pytest.fail(str(e))

   def test_login_password_mismatch(self):
      login_user = self.login_exection_data["PASSWORD_MISMATCH"]
      
      response = requests.post(self.url+'/login', login_user)
      must_status_code = 400 
      must_message = 'Incorrect password'

      assert must_status_code == response.status_code
      assert must_message == response.json()["message"]
      assert "RequestsCookieJar[]" in str(response.cookies)

   def test_login_password_mismatch(self):
      login_user = self.login_exection_data["UNREGISTERED"]
      
      response = requests.post(self.url+'/login', login_user)
      must_status_code = 404 
      must_message = 'User not found'

      assert must_status_code == response.status_code
      assert must_message == response.json()["message"]
      assert "RequestsCookieJar[]" in str(response.cookies)



      
  