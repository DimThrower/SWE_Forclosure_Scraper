def innerHTML_Drill (current_tag):
    """
    Recursively drills down into the DOM until a non-blank inner HTML is found.
    Args:
        current_tag: The current BeautifulSoup tag being processed.
    Returns:
        The inner HTML of the first non-blank tag found, or None if no inner HTML is found.
    """
    if current_tag.string and current_tag.string.strip():
            return current_tag.string.strip()
    else:
            if current_tag.find():
                return innerHTML_Drill(current_tag.find())
            else: 
                    # print('No innerHTML found')
                    return None