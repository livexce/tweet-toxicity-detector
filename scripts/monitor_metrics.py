from prometheus_client import start_http_server, Summary, Gauge
import time

REQUEST_TIME = Summary("request_processing_seconds", "Temps de réponse")
MODEL_SIZE = Gauge("model_size_bytes", "Taille du modèle")


@REQUEST_TIME.time()
def process_request():
    time.sleep(0.5)


if __name__ == "__main__":
    MODEL_SIZE.set(2048000)  # Ex: 2 Mo
    start_http_server(8001)
    while True:
        process_request()
