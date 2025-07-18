1. Django
    - 특징
        풀스택 프레임워크: 대부분의 기능이 기본적으로 내장되어 있다.
        MTV 패턴 사용: Model(데이터 구조와 DB 연결), Template(HTML 출력 화면), View(요청 처리)
        보안 기능 우수
        빠른 개발에 적합
    -장점
        강력한 백오피스 UI 자동 생성
        커뮤니티가 큼
        문서가 풍부함
    -단점
        기본 구조에서 벗어나기 힘듦
        단순 프로젝트에는 과함

2. Flask
    - 특징
        마이크로 프레임워크: 핵심 기능만 제공하고, 나머지는 플러그인 구성임
        유연성이 높고 간단함
    - 장점
        구조가 단순해서 빠르게 습득 가능함
        원하는 대로 구성 가능함
    - 단점
        라이브러리 추가를 요하는 기능이 많음
        대형 프로젝트에서는 버거워짐

3. FastAPI
    - 특징
        OpenAPI를 자동으로 문서화햐는 기능을 가짐
        Pydantic 기반
        타입 검사 지원, 자동 유효성 검사 가능
    - 장점
        빠르다
        API를 활용한 백엔드 개발에 용이하다
        타입 검사 기능을 통해 버그 방지에 유리하다
    - 단점
        전통적인 HTML 기반 웹페이지에는 부적합하다
        역사가 오래되지 않아 위 두 프레임워크에 비해 커뮤니티가 작고 자료가 적다. 