PAGE_LAYOUT = """
# Bible Search App

<|layout|columns=1 1|
<|part|
## Search the Bible
<|{search_query}|input|label=Enter your search term|>
<|Search|button|on_action=search_bible|>

## Results
<|{search_results}|text|height=400px|>
|>

<|part|
## Recent Searches
Coming soon...
|>
|>
"""