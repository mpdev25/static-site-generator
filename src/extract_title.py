

def extract_title(markdown):
    
    line_list = markdown.splitlines()
    for line in line_list:
        stripped = line.strip()
        if stripped.startswith("# "):
            header = stripped.strip("# ").strip()
            return header
    raise Exception("No header found.")
        