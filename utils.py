def convert_factor(value: str) -> float:
    """Convert a string with a numerical factor to a numerical value.
    
    Examples:
    100k is converted to 100,000.
    100m is converted to 1,000,000.
    If the string does not have a factor, return it as a numerical value.
    
    Args:
        value (str): The string to convert.
        
    Returns:
        float: The numerical value.
        
    Raises:
        ValueError: If the string is not a valid numerical value.
    """

    conversions = {
        'k' : 1000,
        'm' : 1000000,
        'b' : 1000000000,
    }

    try:
        for symbol, factor in conversions.items():
            if symbol in value:
                return float(value.replace(symbol, '')) * factor
        return float(value)
    except ValueError:
        raise ValueError(f'Invalid value for: {value}')
    
def map_category(value: str, keywords: dict) -> str:
    """Return a category name based on the keyword that was found within the value.
    If none of the keywords are found within the value, return 'Other'
    """
    for keyword, keyword_value in keywords.items():
        if keyword in value.lower():
            return keyword_value
    return "Other"

def detailed_labels(pct, allvals):
    """Return a string with the absolute value and percentage of the total.
    """
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{absolute}\n({pct:.1f}%)"