from utils import moveMouseToSearchBar
from utils import analysis_pixel
def main():
    print("Moving mouse to search bar...")
    moveMouseToSearchBar()
    print("Searching for the input box...")
    coordinates = analysis_pixel()
    if coordinates:
        x, y = coordinates
        print(f"Found the input box at coordinates: ({x}, {y})")
    else:
        print("Could not find the input box.")

if __name__ == "__main__":
    main()