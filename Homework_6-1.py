"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
import time


class TrafficLight:
    __trafficlight_color = 'red', 'yellow', 'green'  # Атрибут

    def running(self):  # Метод класса
        x = round(time.time())
        n = 0
        while True:
            print(TrafficLight.__trafficlight_color[n])
            time.sleep(1)
            t = round(time.time()) - x
            if TrafficLight.__trafficlight_color[n] == 'red' and t == 7:
                n = 1
                x = round(time.time())
            elif TrafficLight.__trafficlight_color[n] == 'yellow' and t == 2:
                n = 2
                x = round(time.time())
            elif TrafficLight.__trafficlight_color[n] == 'green' and t == 7:
                n = 0
                x = round(time.time())



        # pass


traffic_lights = TrafficLight()
traffic_lights.running()
