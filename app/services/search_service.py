from ddgs import DDGS


class SearchService:

    def search(self, query, max_results=5):

        results = []

        try:
            with DDGS() as ddgs:

                response = ddgs.text(
                    query,
                    max_results=max_results
                )

                for item in response:

                    results.append({
                        "title": item.get("title", ""),
                        "body": item.get("body", ""),
                        "url": item.get("href", "")
                    })

        except Exception as e:

            print("Search Error:", e)

        return results