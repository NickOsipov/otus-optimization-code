# OTUS. Практика. Оптимизация кода

## План работы

Все примеры кода находятся в папке `examples`.

1. Оптимизация и профилирование - `examples/optimization`
2. Операции ввода/вывода - `examples/io_bound`
3. Операции CPU - `examples/cpu_bound`
4. Еще некоторые примеры библиотек - `examples/other`

## Как скачать данные

1. Запросить id файла у преподавателя
2. Установить зависимости в виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/requirements-dev.txt
invoke download-data
```

## Установка остальных зависимостей
```bash
pip install -r requirements/requirements-lint.txt
pip install -r requirements/requirements.txt
```

## Автор

[Nick Osipov](http://t.me/NickOsipov)