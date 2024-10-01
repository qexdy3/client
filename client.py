import socket
import time

# Настройки клиента (используйте адрес и порт из ngrok)
HOST = '7.tcp.eu.ngrok.io'  # Публичный адрес, который дал ngrok
PORT = 11566             # Публичный порт, который дал ngrok

while True:
    try:
        # Создаем сокет (IPv4, TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))  # Подключаемся к серверу
            print(f"Подключен к серверу {HOST}:{PORT}")

            while True:
                # Отправляем сообщение о подключении каждую секунду
                s.sendall('Клиент подключен'.encode('utf-8'))  # Отправляем сообщение
                time.sleep(1)  # Ждем 1 секунду перед следующим сообщением
    except ConnectionRefusedError:
        print(f"Не удалось подключиться к серверу {HOST}:{PORT}. Ожидание подключения...")
        time.sleep(2)  # Ждем перед повторной попыткой
    except KeyboardInterrupt:
        print("Клиент завершил работу.")
        break
