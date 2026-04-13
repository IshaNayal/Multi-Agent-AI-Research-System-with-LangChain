from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """search the web for recent and reliable information on a topic. Returns titles, urls, and snippets."""
    
    results = tavily.search(query=query, max_results=1)
    
    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']} \nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    
    return "\n----\n".join(out)

print(web_search.invoke("what are the recent news of war?"))


@tool
def scrape_url(url:str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading.""" 
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/50"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:1000]
    except Exception as e:
        return f"Could not scrape the URL: {str(e)}"
    
print(scrape_url.invoke("https://www.theverge.com/tech/910990/meta-ceo-mark-zuckerberg-ai-clone"))
    
    
    
    

