import logging
import sys
from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler

class EnterpriseLogger:
    """
    Sistema de log profissional com suporte a cores e rotação de arquivos.
    Projetado para ambientes de automação de alto desempenho.
    """
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnterpriseLogger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        self.logger = logging.getLogger("Advanced-Rewards-Bot")
        self.logger.setLevel(logging.DEBUG)
        
        # Formatação
        log_format = logging.Formatter(
            '%(asctime)s | [%(levelname)s] | %(module)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Handler de Console (Standard Out)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_format)
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)

        # Handler de Arquivo Rotativo (Audit Log)
        log_dir = Path("/home/viniciusphdu/WORKSPACE_CORE/Advanced-Rewards-Bot/logs")
        log_dir.mkdir(exist_ok=True)
        
        file_handler = RotatingFileHandler(
            log_dir / "audit.log",
            maxBytes=5*1024*1024,  # 5MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str, exc_info=False):
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str):
        self.logger.debug(message)

    def warning(self, message: str):
        self.logger.warning(message)

# Instância Singleton para uso em todo o projeto
logger = EnterpriseLogger()
