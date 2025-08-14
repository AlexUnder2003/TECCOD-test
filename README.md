# OpenSearch Демо Приложение

Простое приложение для демонстрации работы с OpenSearch, включающее создание индекса, загрузку документов и поиск с фильтрацией.

## Описание

Приложение создает индекс в OpenSearch с тремя полями:
- `title` - заголовок документа (текст)
- `content` - содержимое документа (текст)  
- `content_type` - тип контента (ключевое поле)

## Требования

- Python 3.8+
- OpenSearch (локально или через Docker)
- Библиотека `opensearch-py`

## Установка

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd TECCOD-test
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```

3. **Установите зависимости:**
```bash
pip install opensearch-py
```

## Запуск OpenSearch

### Вариант 1: Docker Compose (рекомендуется)

Создайте `docker-compose.yml`:
```yaml
version: '3.8'
services:
  opensearch:
    image: opensearchproject/opensearch:2.11.0
    container_name: opensearch
    environment:
      - discovery.type=single-node
      - bootstrap.memory_lock=true
      - "OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m"
      - "DISABLE_INSTALL_DEMO_CONFIG=true"
      - "DISABLE_SECURITY_PLUGIN=true"
    ports:
      - "9200:9200"
    volumes:
      - opensearch-data:/usr/share/opensearch/data

volumes:
  opensearch-data:
```

Запустите:
```bash
docker-compose up -d
```
## Использование

1. **Запустите приложение:**
```bash
python opensearch_client.py
```

2. **Что происходит:**
   - Создается индекс `documents` с маппингом
   - Загружаются 6 тестовых документов (книги и фильмы)
   - Демонстрируется поиск по ключевым словам

## Функциональность

### Создание индекса
- Автоматическое создание индекса с правильным маппингом
- Проверка существования индекса перед созданием

### Загрузка документов
- Bulk загрузка документов через OpenSearch API
- Автоматическое назначение ID для каждого документа

### Поиск документов
- **`search_documents(query, content_type=None)`** - основная функция поиска
- Поиск по полям `title` и `content` (с приоритетом для заголовка)
- Фильтрация по `content_type` (book, film, article, news, blog, document)
- Возвращает список словарей с полями:
  - `title` - заголовок документа
  - `snippet` - первые 50 символов содержимого

## Примеры использования

```python
# Поиск по всем типам
results = search_documents("Great")

# Поиск только в книгах
results = search_documents("Great", "book")

# Поиск только в фильмах
results = search_documents("Great", "film")
```

## Автор

Назимов Александр
