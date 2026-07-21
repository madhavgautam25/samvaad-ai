from app.services.search_service import SearchService

search = SearchService()

results = search.search("Who invented Python?")

for item in results:

    print("=" * 50)
    print("Title :", item["title"])
    print("Body  :", item["body"])
    print("URL   :", item["url"])