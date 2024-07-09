mathematician_filenames = {
    "Fibonacci": "dialogue/fibonacci_dialogue.txt",  
}

def mathematician_filename_find(dialogue_name: str) -> str:
    # Helper function that takes care of fetching the image of a given mathematician
    # Input(s): Name of the mathematician (dialogue_name)
    # Output(s): Image of the mathematician
    return mathematician_filenames.get(dialogue_name, "Mathematician's image not found")

def read_dialogue_from_file(filename: str) -> str:
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

def mathematician_image_show(character_image: str) -> None: 
    print(character_image)

# Testing call for the function
mathematician_image_show(read_dialogue_from_file(mathematician_filename_find("Fibonacci")))