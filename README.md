# SocialMediaAccSearch
Google Dork search for social media profiles using Serpi API

# Social Media Account Searcher

A simple Python script that automates searching for social media profiles and content related to specific keywords across multiple platforms using the [SerpAPI](https://serpapi.com/) Google Search API. The results are exported to a CSV file for further analysis or reporting.

## Features

- Queries multiple social media platforms in one run:
  - Twitter, Facebook, LinkedIn, YouTube, TikTok, Pinterest, Medium, Twitch, Vimeo, Instagram
- Uses Google search with advanced queries (keywords + `site:` filters)
- Saves results to a `results.csv` file with:
  - Platform name  
  - Result title  
  - URL  
  - Snippet/preview text
- Easy to customize:
  - Add/remove platforms
  - Change or localize keywords

## How it works

The script builds a set of Google search queries (one per platform) and sends them to SerpAPI.  
For each platform:

1. It calls the `https://serpapi.com/search` endpoint with the configured query.
2. It parses the `organic_results` from the JSON response.
3. It appends each result as a row in `results.csv`.

:contentReference[oaicite:0]{index=0}

## Requirements

- Python 3.8+
- A valid [SerpAPI](https://serpapi.com/) API key
- The following Python packages:
  - `requests`
  - `json` (standard library)
  - `csv` (standard library)

You can install `requests` with:

```bash
pip install requests
```

## Configuration
1. Open the script file (e.g. Social Media account searcher.py).
2. Set your SerpAPI API key in the base_params section:
```bash
python

base_params = {
    "api_key": "<YOUR_SERPAPI_KEY>",
    "output": "json"
}
```

Adjust the queries dictionary to match your use case:

```python

queries = {
    "Twitter": "Keyword 1 OR Keyword 2 OR Keyword 3 site:twitter.com",
    "Facebook": "Keyword 1 OR Keyword 2 OR Keyword 3 site:facebook.com",
    ...
}
```
You can:

Change Keyword 1, Keyword 2, Keyword 3 to your brand, person, campaign or project names.

Add or remove platforms by editing the dictionary keys and queries.

## Usage
From the project directory, run:

```bash
python "Social Media account searcher.py"
```
After execution, you will get a file:
```
results.csv
```
with columns:
-`Platform`
-`Title`
-`Link`
-`Snippet`

You can open it in Excel, LibreOffice, Google Sheets, or use it as input for other tooling.

## Customization
- ### Adding new platforms
Just add a new entry in the `queries` dictionary:

```python

"Reddit": "Keyword 1 2024 OR Keyword 2 OR Keyword 3 site:reddit.com",
```
- ### Changing languages or regions
You can extend params with additional SerpAPI options such as:
  - `hl` – language (e.g. `"hl": "pl"`)
  - `gl` – country (e.g. `"gl": "pl"`)
- ### Error handling / robustness
For production use, you can add:
- Try/except around the `requests.get` call
- Rate limiting / sleep between requests
- Logging instead of plain script output

## Use cases
- Brand or executive exposure monitoring
- Basic OSINT / footprint discovery
- Collecting links for manual review
- Supporting CTI / DRPS workflows with quick social media queries

Disclaimer
This script is provided for educational and research purposes.
Make sure your use of SerpAPI, Google Search and social media platforms complies with their Terms of Service and with applicable law.
