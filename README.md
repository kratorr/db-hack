# Взламываем электронный дневник


Этот репозитрий содержит скрипты для правки электроного дневника из репозитория
[e-diary](https://github.com/kratorr/e-diary), позволяет исправить оценки, убрать замечания и добавить похвалу.

# Как установить

Установите проект из [e-diary](https://github.com/kratorr/e-diary)

Поместите файл scripts.py в директорию с проектом рядом с файлом manage.py



# Как использовать


Запустите из директории проекта оболочку:
```bash
$ python3 manage.py shell
```
Далее импортируем функции:

```python
>>> from scripts import fix_marks, remove_chastisements, create_commendation, 
```
Получем учетную запись ученика:
```python
>>> schoolkid = get_schoolkid('Фролов Иван')
```

Меняем оценки:
```python
>>> fix_marks(schoolkid)
```
Убираем замечания:
```python
>>> remove_chastisements(schooldkid)
```
Добавляем похвалу:
```python
>>> create_commendation(schoolkid, 'Математика')
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DVMN.ORG](https://dvmn.org)

