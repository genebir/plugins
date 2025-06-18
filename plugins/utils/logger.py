import logging
from plugins.config.settings import load_settings
from pathlib import Path
import os

def setup_logger() -> None:
    settings = load_settings()
    log_config = settings.get("logging", {})

    level = getattr(logging, log_config.get("level", "INFO").upper(), logging.INFO)
    log_format = log_format = log_config.get("format", "[%(asctime)s] %(levelname)s %(name)s : %(message)s")

    handlers = []

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)

    if log_config.get("to_file", False):
        rotate_config = log_config.get("rotate", {})
        log_dir = Path(log_config.get("log_dir", "./logs"))
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"{os.environ.get("ENV", "dev")}.log"

        if rotate_config.get("enabled", True):
            print('rotate')
            from logging.handlers import TimedRotatingFileHandler
            file_handler = TimedRotatingFileHandler(
                filename=log_file,
                when=rotate_config.get("when", "midnight"),
                interval=rotate_config.get("interval", 1),
                backupCount=rotate_config.get("backupCount", 7),
                encoding="utf-8",
                utc=False
            )

            suffix = rotate_config.get("suffix", "%Y%m%d")
            file_handler.suffix = suffix
        else:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
        
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)

    logging.basicConfig(level=level, handlers=handlers)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)