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

### 환경 변수 파일 (.env)
프로젝트 루트에 `.env` 파일을 생성하여 환경 변수를 설정합니다.
**주의: .env 파일은 Git에서 추적되지 않으므로 직접 생성해야 합니다.**

```env
ENV=dev  # 환경 이름 (dev, prod 등)
```

### YAML 설정 파일 (config/)
`config/` 디렉터리에 환경별 YAML 설정 파일을 생성합니다.
**주의: config/ 디렉터리는 Git에서 추적되지 않으므로 직접 생성해야 합니다.**

#### config/dev.yaml (개발 환경)
```yaml
logging:
  level: INFO              # 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  to_file: true           # 파일 로깅 활성화 여부
  log_dir: ./logs         # 로그 파일 저장 디렉터리
  format: "[%(asctime)s] %(name)s %(levelname)s: %(message)s"  # 로그 출력 형식
  rotate:                 # 로그 파일 로테이션 설정
    enabled: true         # 로테이션 활성화 여부
    when: "midnight"      # 로테이션 시점 (S, M, H, D, W0-W6, midnight)
    interval: 1           # 로테이션 간격
    backupCount: 7        # 보관할 백업 파일 개수
    suffix: "%Y%m%d"      # 백업 파일명 접미사 (날짜 형식)
```

#### config/prod.yaml (운영 환경 예시)
```yaml
logging:
  level: WARNING
  to_file: true
  log_dir: /var/log/etl
  format: "[%(asctime)s] %(name)s %(levelname)s: %(message)s"
  rotate:
    enabled: true
    when: "midnight"
    interval: 1
    backupCount: 30
    suffix: "%Y%m%d"
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

2. **환경 설정 파일 생성**
   
   **a) .env 파일 생성**
   ```bash
   # 프로젝트 루트에 .env 파일 생성
   echo "ENV=dev" > .env
   ```
   
   **b) config 디렉터리 및 YAML 파일 생성**
   ```bash
   # config 디렉터리 생성
   mkdir -p config
   
   # 개발 환경 설정 파일 생성
   cat > config/dev.yaml << EOF
   logging:
     level: INFO
     to_file: true
     log_dir: ./logs
     format: "[%(asctime)s] %(name)s %(levelname)s: %(message)s"
     rotate:
       enabled: true
       when: "midnight"
       interval: 1
       backupCount: 7
       suffix: "%Y%m%d"
   EOF
   ```

3. **테스트 스크립트 생성 및 실행**
   ```bash
   # 테스트 스크립트 생성
   cat > test.py << EOF
   from plugins.utils.logger import setup_logger, get_logger
   
   setup_logger()
   
   logger = get_logger(__name__)
   logger.info('ETL 시스템 테스트')
   EOF
   
   # 테스트 실행
   python test.py
   ```

## 개발

- `plugins/` 디렉터리에 새로운 플러그인 추가
- `config/`에 환경별 구성 생성
- 일관된 출력 형식을 위한 로깅 시스템 사용
- 확장 가능한 컴포넌트를 위한 플러그인 아키텍처 준수

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.