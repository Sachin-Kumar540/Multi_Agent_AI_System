import os
from dotenv import load_dotenv

load_dotenv()

# Try to import TavilyClient; if unavailable, provide a fallback implementation
try:
    from tavily import TavilyClient

    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    _HAS_TAVILY = True
except Exception:
    client = None
    _HAS_TAVILY = False

# test it
#################################
# response = client.search(
    # query="Best hotels in Dubai"
# )

# print(response)

####################################



def tavily_search(query):
    if not _HAS_TAVILY or client is None:
        # Fallback: return a placeholder message so the app can run without Tavily
        return "(Tavily not available in this environment; hotel results skipped)"

    response = client.search(query=query, max_results=5)
    results = []
    for i, r in enumerate(response.get("results", []), 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)
    
    
    
    
