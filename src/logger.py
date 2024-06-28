import logging

# Configuración del logger
logging.basicConfig(filename='taximeter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#esta funcion guarda mensaje de informaciòn
def log_info(message):
    logging.info(message)

##esta funcion guarda mensaje de advertencia
def log_warning(message):
    logging.warning(message)


#esta funcion guarda mensaje de error
def log_error(message):
    logging.error(message)
