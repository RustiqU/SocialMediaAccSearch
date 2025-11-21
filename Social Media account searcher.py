import requests
import json
import csv

base_params = {
    "api_key": "<SERPIAPI KEY>,
    "output": "json"
}

queries = {
    "Twitter": "Keyword 1 OR Keyword 2 OR Keyword 3 site:twitter.com",
    "Facebook": "Keyword 1 OR Keyword 2 OR Keyword 3 site:facebook.com",
    "LinkedIn": "Keyword 1 OR Keyword 2 OR Keyword 3 site:linkedin.com",
    "YouTube": "Keyword 1 OR Keyword 2 OR Keyword 3 site:youtube.com",
    "TikTok": "Keyword 1 OR Keyword 2 OR Keyword 3 site:tiktok.com",
    "Pinterest": "Keyword 1 OR Keyword 2 OR Keyword 3 site:pinterest.com",
    "Medium": "Keyword 1 OR Keyword 2 OR Keyword 3 site:medium.com",
    "Twitch": "Keyword 1 OR Keyword 2 OR Keyword 3 site:twitch.tv",
    "Vimeo": "Keyword 1 OR Keyword 2 OR Keyword 3 site:vimeo.com",
    "Instagram": "Keyword 1 OR Keyword 2 OR Keyword 3 site:instagram.com"
}

# Otwórz plik CSV i zapisz nagłówki kolumn
with open('results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Platform", "Title", "Link", "Snippet"])

    for platform, query in queries.items():
        params = {
            **base_params,
            "engine": "google",
            "q": query,
        }
        response = requests.get("https://serpapi.com/search", params=params)
        results = json.loads(response.text)

        if "organic_results" in results:
            # Zapisz każdy wynik w pliku csv jako nowy wiersz
            for result in results['organic_results']:
                writer.writerow([platform, result['title'], result['link'], result['snippet']])
        else:
            writer.writerow([platform, "No results found", "", ""])

