mathematician_filenames = {
    "Fibonacci": "dialogue/fibonacci_dialogue.txt",  
}

def mathematician_filepath_find(mathematician_name: str) -> str:
    # f: Helper function that takes care of fetching the path to a given mathematician's image
    # Input(s): Name of the mathematician (mathematician_name)
    # Output(s): Path to a given mathematician's image
    return mathematician_filenames.get(mathematician_name, "Mathematician's image not found")

def read_image_from_file(filepath: str) -> str:
    # f: ...
    # Input(s): Path to a mathematician's image
    # Output(s): Mathematician's image (in dialogue) 
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

def dialogue_image_show(character_image: str) -> None:
    # f: Prints out the mathematician's image (to be improved)
    # Input(s): Mathematician's image
    # Output(s): None 
    print(character_image)

# Testing call for the function
dialogue_image_show(read_image_from_file(mathematician_filepath_find("Fibonacci")))