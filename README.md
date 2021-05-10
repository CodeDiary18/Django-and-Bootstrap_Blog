# Django-and-Bootstrap Blog
### <Do it! 장고+부트스트랩 파이썬 웹 개발의 정석> 책을 보고 구현한 블로그

  
<img src="http://image.kyobobook.co.kr/images/book/xlarge/069/x9791163032069.jpg"  width="200">
  
  
## Folder Introduction
> ### ▶ [웹 기초](https://github.com/CodeDiary18/Do_it-Django-and-Bootstrap/tree/main/%EC%9B%B9%20%EA%B8%B0%EC%B4%88)
>> html, css, js 연습
> ### ▶ [django 웹사이트](https://github.com/CodeDiary18/Do_it-Django-and-Bootstrap/tree/main/django%20%EC%9B%B9%EC%82%AC%EC%9D%B4%ED%8A%B8)
>> Django web framework와 python, html, css, js, bootstrap을 사용하여 만든 블로그
>> ### ▷ django 웹사이트 실행방법
>> 1. [django 웹사이트] 폴더에 venv라는 가상환경을 [python -m venv venv]라는 명령어를 통해 구축
>> 2. [venv/Scripts/activate.bat]으로 가상환경 실행(계속 실행하고 있어야 함)
>> 3. [pip install -r requirements.txt] 명령어를 입력해 필요한 모듈 설치
>> 4. 아래 명령어를 순서대로 입력
>>    - [python manage.py makemigrations blog]
>>    - [python manage.py migrate blog]
>>    - [python manage.py migrate]
>> 5. [python manage.py runserver] 명령어로 서버 구동시킨 후 "127.0.0.1:8000"으로 접속
>>
>>  * 게시물을 작성해보기 위해서는 서버를 잠시 멈추고 [python manage.py createsuperuser]를 통해 관리자 계정을 만들어서 로그인하면 게시물을 작성할 수 있다.
