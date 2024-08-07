from typing import List

def title(style: str):
    styles = ["slanted_figlet", "normal"]
    if style not in styles:
        raise KeyError(f"Invalid style '{style}'. Valid styles are 'slanted_figlet' and 'normal'")
        return
    
    if style == styles[1]:
        print("char_reporter\n")

def choices(style: str, choicearray: List[str]) -> None:
    styles = ["square_brackets", "dot"]
    if style not in styles:
        raise KeyError(f"Invalid style '{style}'. Valid styles are 'square_brackets' and 'dot'")
        return
    
    if style == styles[0]:
        square_bracketed_strings = [f"[{i+1}] {string}" for i, string in enumerate(choicearray)]
        result = '\n'.join(square_bracketed_strings)
        print(result)

    if style == styles[1]:
        square_bracketed_strings = [f"{i+1}. {string}" for i, string in enumerate(choicearray)]
        result = '\n'.join(square_bracketed_strings)
        print(result)
    