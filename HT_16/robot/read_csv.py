# Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
# Увага! Файл має бути прочитаний з сервера кожного разу
# при запускі скрипта, не зберігайте файл локально.
import csv
import requests


class CSV:
    URL = 'https://robotsparebinindustries.com/orders.csv'

    def __create_response(self):
        try:
            response = requests.get(self.URL)
            return response
        except requests.RequestException as e:
            print(e)
            return None

    def read_csv_file(self):
        response = self.__create_response()
        if response is not None:
            try:
                data = []
                reader = list(csv.reader(response.text.splitlines()))
                for row in reader[1::]:
                    data.append(row)
                return data
            except csv.Error as e:
                print(e)
                return None


if __name__ == '__main__':
    csv_obj = CSV()
    print(csv_obj.read_csv_file())
