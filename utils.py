def format_search_results(response):
    """Форматирует результаты поиска в требуемом виде"""
    results = []
    for hit in response["hits"]["hits"]:
        source = hit["_source"]
        snippet = (
            source["content"][:50] + "..."
            if len(source["content"]) > 50
            else source["content"]
        )

        results.append({"title": source["title"], "snippet": snippet})

    return results
