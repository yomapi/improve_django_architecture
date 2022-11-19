# Architecture improvement

Django를 사용하던 중 실무에서 겪은 문제점들을 해결해보기 위해 만든 레포지토리입니다.

# Config
``` yml
# configs/config_real.yml
# configs/config_example.yml 을 참고해서 설정하세요
databases:
  host: "host url"
  port: 3306
  database: "db name"
  username: "username"
  password: "passwd"
  timezone: "+09:00"

secrets:
  django: "django-something-something"
```


# Install
```
poetry install
python manage.py runserver
```

# branch 소개
모든 코드는 master에 통합되어 있습니다.
각 브랜치별로, 해결한 문제들을 정리해두었습니다.

##### improve-test-code
Service 레이어와 repository 레이어의 의존성을 끊어, 테스트 코드를 개선한 프로젝트 입니다.
자세한 내용은 블로그 글을 참고해주세요.
https://velog.io/@yomapi/1.-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%BD%94%EB%93%9C-%EA%B0%9C%EC%84%A0-service%EC%99%80-repository%EC%9D%98-%EC%9D%98%EC%A1%B4%EC%84%B1-%EB%81%8A%EA%B8%B0