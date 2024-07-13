import pandas as pd

#0 Name,City,Salary
#Аня,Томск,200000
#Боб,Москва,350000
#Чарли,Москва,270000
#Лиза,Томск,70000
#Настя,,35000
#Саша,Томск,23000
#Сергей,Москва,250000
#Максим,Москва,
#Иван,Москва,67000
#Станислав,Москва,120000
#Вика,,47000
#Мария,Томск,72000


# Создаем  DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kathy', 'Leo'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Chicago', 'Chicago', None, 'New York', 'Chicago', 'Los Angeles', None],
    'Salary': [70000, 80000, 75000, 90000, 65000, 85000, 78000, 72000, None, 70000, 60000, 82000]
})

# Удаляем строки, где в столбцах 'City' или 'Salary' содержится значение NaN.
data_clean = data.dropna(subset=['City', 'Salary'])

# Группируем по столбцу 'City' и вычисляем среднее значение в столбце 'Salary'
group = data_clean.groupby('City')['Salary'].mean()

print(group)
