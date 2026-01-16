import logging
import os

class LogGen:
    """Gestionnaire de logs personnalisé"""
    
    def __init__(self, logfile_path):
        # Créer le dossier Logs s'il n'existe pas
        log_dir = os.path.dirname(logfile_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Configuration du logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Supprimer les handlers existants
        self.logger.handlers.clear()
        
        # Handler pour fichier
        file_handler = logging.FileHandler(logfile_path, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Handler pour console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', 
                                      datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_info(self, message):
        self.logger.info(message)
    
    def log_warning(self, message):
        self.logger.warning(message)
    
    def log_error(self, message):
        self.logger.error(message)
    
    def log_debug(self, message):
        self.logger.debug(message)
