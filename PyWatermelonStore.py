# Function to print the program banner
def print_banner():
    print(r"""
  ___    __      __    _                     _          ___ _               
 | _ \_  \ \    / /_ _| |_ ___ _ _ _ __  ___| |___ _ _ / __| |_ ___ _ _ ___ 
 |  _/ || \ \/\/ / _` |  _/ -_) '_| '  \/ -_) / _ \ ' \\__ \  _/ _ \ '_/ -_)
 |_|  \_, |\_/\_/\__,_|\__\___|_| |_|_|_\___|_\___/_||_|___/\__\___/_| \___|
  ____|__/             _  __                                                
 |__ / |__ ___  __ _  | |/ /__ _                                            
  |_ \ '_ (_-< / _` | | ' </ _` |                                           
 |___/_.__/__/ \__,_| |_|\_\__, |                                           
                           |___/                                            
""")

SALES_FILE = "sales.csv"
PRICE_PER_KILO = 3  # Fixed price in Bs per kilo

locations = [
    ("La Paz", 28.21, 15.5),
    ("Cochabamba", 25.28, 14.3),
    ("Santa Cruz", 21.7, 12.6),
    ("Oruro", 20.8, 13.2),
    ("Potosi", 22.1, 13.6),
    ("Tarija", 21.5, 13.4)
]

# Function to initialize the sales file
def initialize_file():
    # Open in append mode to create the file if it doesn't exist
    file = open(SALES_FILE, "a")
    file.close()

    # Open in read mode to check content
    file = open(SALES_FILE, "r")
    content = file.read()
    file.close()

    # If empty, write the header
    if content == "":
        file = open(SALES_FILE, "a")
        file.write("weight,price_per_kilo,total\n")
        file.close()

# Function to register a sale
def register_sale():
    weight = input("How many kilos of watermelon were sold? ")

    # Check if weight is an integer number
    if weight.isdigit():
        with open(SALES_FILE, "a") as file:
            weight_int = int(weight)
            total = weight_int * PRICE_PER_KILO
            file.write(f"{weight_int},{PRICE_PER_KILO},{total}\n")
        print(f"✅ Sale recorded: {weight_int} kg at {PRICE_PER_KILO} Bs/kg = {total} Bs")
    else:
        print("❌ Please enter a valid integer number.")

# Function to search stores by department
def search_stores():
    city = input("In which department do you want to search for stores? ")
    found = False

    for location in locations:
        if location[0].lower() == city.lower():
            print(f"✅ Store found: {location}")
            found = True

    if not found:
        print("❌ There are no stores in that department.")

# Function to show sales records
def show_sales_record():
    print("\n📒 SALES RECORD:")
    with open(SALES_FILE, "r") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        print("No sales recorded.")
        return

    for i, line in enumerate(lines[1:], 1):  # skip header
        weight, price, total = line.strip().split(",")
        print(f"{i}. Weight: {weight} kg | Price: {price} Bs/kg | Total: {total} Bs")

# Function to show the options menu
def show_menu():
    print("\n--- WATERMELON MENU ---")
    print("1. Register sale")
    print("2. Search stores")
    print("3. View sales record")
    print("4. Exit")

# Main program function
def main():
    print_banner()
    initialize_file()

    while True:
        show_menu()
        option = input("Choose an option (1-4): ")

        if option == "1":
            register_sale()
        elif option == "2":
            search_stores()
        elif option == "3":
            show_sales_record()
        elif option == "4":
            print("Thanks for visiting PySandia Store, see you soon! 🍉")
            break
        else:
            print("❌ Invalid option.")

# Call main function to run the program
main()
