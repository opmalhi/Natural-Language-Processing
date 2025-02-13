import re

def extract_session_id(output_contexts: list) -> str:
    """Extracts session ID from the first output context"""
    try:
        match = re.search(r"/sessions/(.*?)/contexts/", output_contexts)

        if match:
            extract_string = match.group(1)
            return extract_string
        
        return ""
    
    except (IndexError, KeyError):
        return None