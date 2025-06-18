# Python ETL 프레임워크

데이터 처리 파이프라인을 위한 플러그인 아키텍처 기반의 구성 가능한 ETL (Extract, Transform, Load) 시스템입니다.

## 주요 기능

- **환경 기반 구성**: 환경 변수 치환을 지원하는 YAML 기반 설정
- **고급 로깅**: 콘솔/파일 출력 및 로테이션을 지원하는 구성 가능한 로깅
- **플러그인 아키텍처**: 확장 가능한 ETL 컴포넌트를 위한 모듈식 설계
- **환경 관리**: 개발 및 운영 환경을 위한 별도 구성

## 프로젝트 구조

```
ETL/
├── config/
│   └── dev.yaml           # 개발 환경 구성
├── plugins/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py    # 구성 로더
│   └── utils/
│       ├── __init__.py
│       └── logger.py      # 로깅 유틸리티
├── test.py               # 테스트/데모 스크립트
└── .gitignore
```

## 설정

### 환경 변수 설정 (.env)
```env
ENV=dev  # 환경 이름 (기본값: dev)
```

### YAML 설정 (config/dev.yaml)
```yaml
logging:
  level: INFO              # 로그 레벨
  to_file: true           # 파일 로깅 활성화
  log_dir: ./logs         # 로그 디렉터리
  format: "[%(asctime)s] %(name)s %(levelname)s: %(message)s"  # 로그 형식
  rotate:                 # 로그 로테이션 설정
    enabled: true         # 로테이션 활성화
    when: "midnight"      # 로테이션 시점
    interval: 1           # 로테이션 간격
    backupCount: 7        # 보관할 백업 파일 수
    suffix: "%Y%m%d"      # 백업 파일 접미사
```

## 사용법

### 기본 설정
```python
from plugins.utils.logger import setup_logger, get_logger

# 로깅 초기화
setup_logger()

# 로거 인스턴스 가져오기
logger = get_logger(__name__)
logger.info('ETL 프로세스 시작')
```

### 구성 로딩
```python
from plugins.config.settings import load_settings

# 환경별 설정 로드
settings = load_settings()
```

## 시작하기

1. **의존성 설치**
   ```bash
   pip install python-dotenv pyyaml
   ```

2. **환경 변수 설정**
   ```bash
   export ENV=dev
   ```

3. **테스트 실행**
   ```bash
   python test.py
   ```

## 개발

- `plugins/` 디렉터리에 새로운 플러그인 추가
- `config/`에 환경별 구성 생성
- 일관된 출력 형식을 위한 로깅 시스템 사용
- 확장 가능한 컴포넌트를 위한 플러그인 아키텍처 준수

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.