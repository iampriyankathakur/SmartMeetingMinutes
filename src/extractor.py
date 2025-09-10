import re
from typing import List

def extract_action_items(text: str) -> List[str]:
    """
    Very light-weight extractor: finds lines with common action keywords.
    Improve later with spaCy / dependency parsing.
    """
    items = []
    keywords = r'\b(action|todo|to do|assign|deadline|due|follow up|will)\b'
    for line in text.splitlines():
        if re.search(keywords, line, re.I):
            items.append(line.strip())
    # also try to find sentences mentioning 'Action:' explicitly
    for match in re.findall(r'Action:\s*(.*)', text, re.I):
        items.append(match.strip())
    # de-duplicate and return
    seen = []
    for it in items:
        if it not in seen:
            seen.append(it)
    return seen
