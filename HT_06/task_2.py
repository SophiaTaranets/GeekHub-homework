# Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a>
# одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%).
# Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок).

def bank(a, years, percent=10):
    for year in range(years):
        a += a * percent / 100
    result_suma = round(a, 2)
    print(f'Balance after {years} years: {result_suma}')


# Test data
initial_deposit = 1000
deposit_years = 5
year_percent = 10

bank(initial_deposit, deposit_years, year_percent)
