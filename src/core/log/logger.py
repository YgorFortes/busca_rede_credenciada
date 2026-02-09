import logging
from rich.logging import RichHandler
from enum import Enum
from typing import Literal
from utils.hours_utils import get_current_time




logging.basicConfig(
    level=logging.DEBUG,  
    format="%(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(
            rich_tracebacks=False,
            show_time=False,     
            show_level=False,     
            show_path=False
        )
    ]
)

    
class LogType(str, Enum):
    ERROR = "error"
    WARN = "warn"
    VERBOSE = "verbose"
    DEBUG = "debug"
    NORMAL = "normal"
    

LEVEL_MAP = {
    LogType.ERROR: logging.ERROR,
    LogType.WARN: logging.WARNING,
    LogType.VERBOSE: logging.INFO,
    LogType.DEBUG: logging.DEBUG,
    LogType.NORMAL: logging.INFO,
}



class Logger:
    def __init__(self, class_name):
        self.class_name = class_name
        self.logger = logging.getLogger(class_name)
        self.logger.setLevel(logging.DEBUG)  # Garante que DEBUG seja aceito

        # Adiciona o handler apenas se ainda não tiver
        if not self.logger.handlers:
            handler = RichHandler(
                rich_tracebacks=False,
                show_time=False,
                show_level=False,
                show_path=False
            )
            self.logger.addHandler(handler)
        

    def dispatch(self, log_type: LogType, message: str) -> None:
        now = get_current_time()
        msg = f"{now} [{self.class_name}] {message}"

        level = LEVEL_MAP.get(log_type, logging.INFO)
        self.logger.log(level, msg)  
            
        
        
        





