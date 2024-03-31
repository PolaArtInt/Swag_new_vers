### test-case: 5.1  
## Фильтр::A-Z  
Проверка работоспособности фильтра (a to z)  
#### Test:  
test_5_filter.py::  
test_a_to_z_filter  
#### Предусловие:  
Авторизация standard_user: standard_auth  
Переход на страницу каталога товаров:  
https://www.saucedemo.com/v1/inventory.html  
#### Шаги:  
1. Найти все товары в каталоге  
2. Отсортировать их в порядке a-z  
3. Нажать фильтр 'A to Z' сайта  
4. Проверить, что сортировка фильтром сайта  
соответствует сортировке в алфавитном порядке  
#### Ожидаемый результат:  
Товары сортируются в алфавитном порядке  
#### Постусловие:  
Перезагрузить страницу  

----------------------------------------------------------------

### test-case: 5.2  
## Фильтр::Z-A  
Проверка работоспособности фильтра (z to a)  
#### Test:  
test_5_filter.py::  
test_z_to_a_filter  
#### Предусловие:  
Авторизация standard_user: standard_auth  
Переход на страницу каталога товаров:  
https://www.saucedemo.com/v1/inventory.html  
#### Шаги:  
1. Найти все товары в каталоге  
2. Отсортировать их в порядке z-a  
3. Нажать фильтр 'Z to A' сайта  
4. Проверить, что сортировка фильтром сайта  
соответствует сортировке в обратном алфавитном порядке  
#### Ожидаемый результат:  
Товары сортируются в обратном алфавитном порядке  
#### Постусловие:  
Перезагрузить страницу  

----------------------------------------------------------------

### test-case: 5.3  
## Фильтр::Low to High  
Проверка работоспособности фильтра (low to high)  
#### Test:  
test_5_filter.py::  
test_low_to_high_filter   
#### Предусловие:  
Авторизация standard_user: standard_auth  
Переход на страницу каталога товаров:  
https://www.saucedemo.com/v1/inventory.html  
#### Шаги:  
1. Найти все цены товаров в каталоге  
2. Отсортировать их в порядке возрастания  
3. Нажать фильтр 'Low to High'  
4. Проверить, что сортировка фильтром 'Low to High'  
сайта соответствует сортировке по возрастанию  
#### Ожидаемый результат:  
Товары сортируются по цене в порядке возрастания   
#### Постусловие:  
Перезагрузить страницу  

----------------------------------------------------------------

### test-case: 5.4  
## Фильтр 'High to Low'  
Проверка работоспособности фильтра (high to low)  
#### Test:  
test_5_filter.py::  
test_high_to_low_filter    
#### Предусловие:  
Авторизация standard_user: standard_auth  
Переход на страницу каталога товаров:  
https://www.saucedemo.com/v1/inventory.html   
#### Шаги:  
1. Найти все цены товаров в каталоге  
2. Отсортировать их в порядке убывания  
3. Нажать фильтр 'High to Low'
4. Проверить, что сортировка фильтром 'High to Low'  
сайта соответствует с сортировкой по убыванию
#### Ожидаемый результат:  
Товары сортируются по цене в порядке убывания    
#### Постусловие:  
Перезагрузить страницу  

----------------------------------------------------------------