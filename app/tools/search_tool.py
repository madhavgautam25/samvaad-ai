from app.services.search_service import SearchService


class SearchTool:

    def __init__(self):
        self.search_service = SearchService()

    def execute(self, query):

        results = self.search_service.search(query)

        if not results:
            return {
                "success": False,
                "tool": "search",
                "message": "No results found."
            }

        context = ""

        for i, item in enumerate(results, start=1):

            context += (
                f"\nResult {i}\n"
                f"Title: {item['title']}\n"
                f"Content: {item['body']}\n"
                f"Source: {item['url']}\n"
            )

        return {
            "success": True,
            "tool": "search",
            "query": query,
            "context": context,
            "sources": [
                item["url"] for item in results
            ]
        }