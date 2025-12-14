# Imperial Database

Проект на Django для хранения информации о персонажах и кораблях из вселенной Star Wars.  
Поддерживается просмотр персонажей, их кораблей, а также редактирование через административную панель.

---

## Установка и запуск 
### инструкция для macos:
1. **Склонировать репозиторий**
- Если есть SSH
```bash
git clone git@github.com:demi-un/imperial_database.git
```
- Если нет SSH (через https://)
```bash
git clone https://github.com/demi-un/imperial_database.git
```
2. **Создать и активировать виртуальное окружение**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. **Установить все зависимости**
```bash
pip install -r requirements.txt
```
4. **Перейти на уровень файла manage.py**
```bash
cd imperial_database
```
5. **Применить миграции**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
6. **Создать суперпользователя для админки**
```bash
python3 manage.py createsuperuser
```
7. **Запустить сервер**
```bash
python3 manage.py runserver
```
8. **Сайт будет доступен по адресам:**
- Главная страница: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/