from opensearchpy import OpenSearch

host = "localhost"
port = 9200

# Create the client with SSL/TLS and hostname verification disabled.
client = OpenSearch(
    hosts=[{"host": host, "port": port}],
    http_compress=True,  # enables gzip compression for request bodies
    use_ssl=False,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

index_name = "documents"
index_body = {
    "settings": {"index": {"number_of_shards": 1, "number_of_replicas": 1}},
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "standard",
            },
            "content": {
                "type": "text",
                "analyzer": "standard",
            },
            "content_type": {"type": "keyword"},
        }
    },
}


def create_index():
    """Создает индекс если он не существует"""
    if not client.indices.exists(index=index_name):
        response = client.indices.create(index=index_name, body=index_body)
        print("Индекс создан:", response)
        return True
    else:
        print("Индекс уже существует")
        return False


def load_documents():
    """Загружает документы в индекс"""
    documents = [
        {
            "title": "The Great Gatsby",
            "content": "The Great Gatsby is a novel by F. Scott Fitzgerald.",
            "content_type": "book",
        },
        {
            "title": "To Kill a Mockingbird",
            "content": "To Kill a Mockingbird is a novel by Harper Lee.",
            "content_type": "book",
        },
        {
            "title": "1984",
            "content": "1984 is a novel by George Orwell.",
            "content_type": "book",
        },
        {
            "title": "The Catcher in the Rye",
            "content": "The Catcher in the Rye is a novel by J.D. Salinger.",
            "content_type": "book",
        },
        {
            "title": "The Lord of the Rings",
            "content": "The Lord of the Rings is a novel by J.R.R. Tolkien.",
            "content_type": "film",
        },
        {
            "title": "The Hobbit",
            "content": "The Hobbit is a novel by J.R.R. Tolkien.",
            "content_type": "film",
        },
    ]

    bulk_data = ""
    for i, doc in enumerate(documents):
        bulk_data += f'{{ "index" : {{ "_index" : "{index_name}", "_id" : "{i+1}" }} }}\n'
        bulk_data += (
            f'{{ "title" : "{doc["title"]}", "content" : "{doc["content"]}", '
            f'"content_type" : "{doc["content_type"]}" }}\n'
        )

    client.bulk(body=bulk_data)
    print("Документы загружены через bulk операцию")


def search_documents(query: str, content_type: str | None = None):
    """Поиск документов по запросу с опциональной фильтрацией по типу"""
    if content_type is None:
        body = {
            "size": 5,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^2", "content"],
                }
            },
        }
    else:
        body = {
            "size": 5,
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["title^2", "content"],
                            }
                        }
                    ],
                    "filter": [{"term": {"content_type": content_type}}],
                }
            },
        }

    response = client.search(index=index_name, body=body)
    return response
