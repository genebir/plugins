# Python ETL Framework

A configurable ETL (Extract, Transform, Load) system with plugin architecture for data processing pipelines.

## Features

- **Environment-based Configuration**: YAML-based settings with environment variable substitution
- **Advanced Logging**: Configurable logging with console/file output and rotation support
- **Plugin Architecture**: Modular design for extensible ETL components
- **Environment Management**: Separate configurations for development and production

## Project Structure

```
ETL/
├── config/
│   └── dev.yaml           # Development environment configuration
├── plugins/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py    # Configuration loader
│   └── utils/
│       ├── __init__.py
│       └── logger.py      # Logging utilities
├── test.py               # Test/demo script
└── .gitignore
```

## Configuration

### Environment Variables
- `ENV`: Environment name (default: `dev`)

### Logging Configuration (config/dev.yaml)
```yaml
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
```

## Usage

### Basic Setup
```python
from plugins.utils.logger import setup_logger, get_logger

# Initialize logging
setup_logger()

# Get logger instance
logger = get_logger(__name__)
logger.info('ETL process started')
```

### Configuration Loading
```python
from plugins.config.settings import load_settings

# Load environment-specific settings
settings = load_settings()
```

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install python-dotenv pyyaml
   ```

2. **Set Environment Variables**
   ```bash
   export ENV=dev
   ```

3. **Run Test**
   ```bash
   python test.py
   ```

## Development

- Add new plugins to the `plugins/` directory
- Create environment-specific configurations in `config/`
- Use the logging system for consistent output formatting
- Follow the plugin architecture for extensible components

## License

This project is licensed under the MIT License.