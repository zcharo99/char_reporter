def title(style: str):
    styles = ["slanted_figlet", "normal"]
    if style not in styles:
        raise KeyError(f"Invalid style '{style}'. Valid styles are 'slanted_figlet' and 'normal'")
        return
    
    if style == styles[1]:
        print("char_reporter")