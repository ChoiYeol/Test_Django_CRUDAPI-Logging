DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysqlclient librarly 설치
        'NAME': 'world',
        'USER': 'root',
        'PASSWORD': '0814', # mariaDB 설치 시 입력한 root 비밀번호 입력
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

SECRET_KEY = 'django-insecure-y%8+@b8w9snp8#1n1!95)ddzlie3m)=p_l3^!#4((@s_%#-(3^'
