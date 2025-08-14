from opensearch_client import (
    create_index,
    load_documents,
    search_documents,
)
from utils import format_search_results


def main():
    print("1. Создание индекса...")
    create_index()

    print("\n2. Загрузка документов...")
    load_documents()

    print("\n3. Демонстрация поиска:")

    # Поиск по всем типам
    print("\nПоиск 'Kill' (все типы):")
    results = search_documents("Kill")
    formatted_results = format_search_results(results)
    for result in formatted_results:
        print(f"- title:{result['title']}")
        print(f"  snippet:{result['snippet']}")

    # Поиск с фильтром по типу
    print("\nПоиск 'Kill' (только book):")
    results = search_documents("Kill", "book")
    formatted_results = format_search_results(results)
    for result in formatted_results:
        print(f"- title:{result['title']}")
        print(f"  snippet:{result['snippet']}")

    # Поиск с фильтром по типу
    print("\nПоиск 'Great' (только film):")
    results = search_documents("Great", "film")
    formatted_results = format_search_results(results)
    for result in formatted_results:
        print(f"- title:{result['title']}")
        print(f"  snippet:{result['snippet']}")

    # Поиск по всем типам
    print("\nПоиск 'The' (все типы):")
    results = search_documents("The")
    formatted_results = format_search_results(results)
    for result in formatted_results:
        print(f"- title:{result['title']}")
        print(f"  snippet:{result['snippet']}")


if __name__ == "__main__":
    main()
    print("\n")

    print(
        "Если результаты пустые, попробуйте запустить еще раз, возможно документы еще не проиндексированы"
    )
