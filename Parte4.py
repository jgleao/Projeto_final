import logging

logging.basicConfig(
    filename='sistema.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_operacao(msg):
    logging.info(msg)

def log_erro(msg):
    logging.error(msg)

def log_aviso(msg):
    logging.warning(msg)

if __name__ == "__main__":
    log_operacao("Sistema iniciado pelo módulo de logging separado.")
    log_aviso("Aviso de teste.")
    log_erro("Erro de teste.")
