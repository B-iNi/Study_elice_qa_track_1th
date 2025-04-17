


"""
정상적인 케이스
"""
SIGNUP_USER_NOMOTOPIC = []



"""
1. EMAIL 형식이 아닌 경우
2. 비밀번호와 비밀번호 확인 필드 값이 다른 경우
3. USERNAME이 비어있는 경우
4. EMAIL이 비어있는 경우
5. PASSWORD가 비어있는 경우
6. PASSWORD 확인이 비어있는 경우
7. 이메일 문자열 길이 초과인 경우 
8. USERNAME 문자열 길이 초과인 경우 
9. USERNAME 중복인 경우
10. EMAIL 중복인 경우
"""
SIGNUP_USER_EXCEPTION= {
  "EMAIL_FORMAT": {
    "username": "중첩방지닉네임엘리스",
    "email": "string",  
    "password": "string",
    "passwordConfirm": "string"
    }, 
  "DIFFENT_PASSWORD_AND_CONFIRM": {
    "username": "중첩방지닉네임엘리스dnklasdnklasdnkl",
    "email": "dnkdsnklscmnoplcvsamoadnklasdnklasdpcasjmop@naver.com",
    "password": "string",
    "passwordConfirm": "string2212"
    }, 
  "FIELD_NULL":[
    {
    #"username": None,
    "email": "dnkdasn23232kdas@naver.com",
    "password": "string",
    "passwordConfirm": "string"
    },
    {
    "username": "중첩방지닉네임엘리스dnkdnkldnkldasnklasdnkl",
    #"email": None,
    "password": "string",
    "passwordConfirm": "string"
    },
    {
    "username": "중첩방지닉네임엘리스dnkdnkldnkldasnklasdnkl",
    "email": "dnkdasn23232kdas@naver.com",
    #"password": None,
    "passwordConfirm": "string"
    },
    {
    "username": "중첩방지닉네임엘리스dnkdnkldnkldasnklasdnkl",
    "email": "dnkdasn23232kdas@naver.com",
    "password": "string",
    #"passwordConfirm": None
    }], 
  "UNIQ_ORVERLAP":[
    {
    "username": "회원가입유니크중첩방지엘리스스",
    "email": "dsdsad323233232323232@naver.com",
    "password": "string",
    "passwordConfirm": "string"
    },
    {
    "username": "중첩방지닉네임엘리스",
    "email": "dnkldsnklasdnkldasnklsadopw3opdasjo@naver.com",
    "password": "string",
    "passwordConfirm": "string"
    }], 
}

"""
정상로그인유저정보
"""
LOGIN_USER = [
  {
  "username": "QA-엘리스30",
  "email": "qaelice30asdmkldsamkldsamkldasmka@naver.com",
  "password": "string",
},
{
  "username": "QA-엘리스31",
  "email": "qaelice31asdmkldsamkldsamkldasmka@naver.com",
  "password": "string",
},
{
  "username": "QA-엘리스32",
  "email": "qaelice32asdmkldsamkldsamkldasmka@naver.com",
  "password": "string",
}]

"""
로그인 예외처리 

1.유저 존재 하지 않는 이메일로 접근 시도
2. 패스워드 틀렸을 때
3. 필드 누락 

"""
LOGIN_USER_EXCEPTION = {
  "UNREGISTERED": {
    "email": "qaelice30asdmkldsamkldsamkldasmkadnkldsanklsadnklsadnklsdamklmwo2213213321@naver.com",
    "password": "string",
  },
  "PASSWORD_MISMATCH":  {
    "email": "qaelice31asdmkldsamkldsamkldasmka@naver.com",
    "password": "sadnklasdnklasdnklasdnklsdankldasnklsadnklas",
  },
  "FIELD_NULL": [
  {
    "email": None,
    "password": "string",
  },
  {
    "email": None,
    "password": "string",
  }]
}