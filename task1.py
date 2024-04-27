from queue import Queue
import time
import uuid
import random


class Request:
    def __init__(self) -> None:
        self.id = uuid.uuid4()


class ServiceCenter:
    def __init__(self) -> None:
        self.requests = Queue()

    def generate_request(self) -> None:
        request = Request()
        self.requests.put(Request())
        print(f'Створена нова заявка з id {request.id}')

    def process_request(self) -> None:
        if not self.requests.empty():
            cur_request = self.requests.get()
            print(f'Оброблено заявку з id {cur_request.id}')
        else:
            print('Черга пуста')


if __name__ == "__main__":

    serviceCenter = ServiceCenter()

    while True:
        serviceCenter.generate_request()
        time.sleep(random.uniform(0.5, 1.5))
        serviceCenter.process_request()
        time.sleep(random.uniform(0.5, 1.5))
