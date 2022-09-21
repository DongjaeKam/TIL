# django 설치


##  venv 만들 폴더 생성 ( mkdir )
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django (main)
$ mkdir prac-django
```

## 만든 폴더로 들어가기 (cd)
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django (main)
$ cd prac-django
```
##  venv 생성 (python -m venv)
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-dja
$ python -m venv prac-django-venv
```

## 서버 활성화 ( source (서버이름)/Scripts/activate
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-dja
$ source prac-django-venv/Scripts/activate
(prac-django-venv)
```
 
## 서버 비활성화 ( deactivate )
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-dja
$ deactivate
```

## django 설치
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-dja
$ pip install django==3.2.13
```

```
아래 메세지 같이 뜨면 된다.
안정성 이슈 때문에 이전 버전으로 설치

Collecting django==3.2.13
  Using cached Django-3.2.13-py3-none-any.whl (7.9 MB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting pytz
  Using cached pytz-2022.2.1-py2.py3-none-any.whl (500 kB)
 ~/Desktop/TIL/Web/web_dj2ngo/prac-django (main)
```

## 장고 프로젝트 생성 ( django-admin startproject [프로젝트 이름] .)
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-django (main)
$ django-admin startproject firstpjt .

```

## 프로젝트 폴더에서 vscode 실행 ( 안해도 된다 )
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-django (main)
$ code .
```

## 서버실행
```
K@DESKTOP-V4PQF16 MINGW64 ~/Desktop/TIL/Web/web_django/prac-django (main)
$ python manage.py runserver
```

## 브라우저에서 확인 (아래 주소 접속, 로컬 주소에 8000포트 접속)

- http://127.0.0.1:8000/   
- localhost:8000

