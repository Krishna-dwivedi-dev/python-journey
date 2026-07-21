#Day 11 - Error Handling: try, except, finally, raise
#======================================================
#This module demonstrates core exception-handling patterns in Python:
    #1. Catching specific exceptions inside a loop without crashing the whole program
    #2. Using a while-loop + try/except to force valid user input
    #3. Manually raising exceptions for business-logic validation
    #4. Using finally to guarantee cleanup code always runs
    #5. Safely reading and parsing an external file with malformed-data handling



# ============================================================
# Q1: Parse a list of strings into integers, skipping invalid entries
# ============================================================
def parse_int_list(data):
    # Convert strings to integers, skipping any invalid (non-numeric) entries.
    result = []
    for element in data:
        try:
            number = int(element)
            result.append(number)
        except ValueError:
            print(f"Skipped invalid entry: {element}")
    return result


# ============================================================
# Q2: Repeatedly prompt the user until a valid age is entered
# ============================================================
def get_user_age():
    #Keep prompting until the user enters a valid age (0-150).
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                raise ValueError("Invalid age! Must be between 0 and 150.")
            return age
        except ValueError as e:
            print(f"Error: {e}")


# ============================================================
# Q3: Read a key=value config file, skipping malformed lines
# ============================================================
def create_test_config():
    #Create a sample config.txt (with one bad line) to test read_config_file().
    content = """username=krishna
timeout=30
randomtext
debug=true"""
    with open("config.txt", "w") as f:
        f.write(content)


def read_config_file(filename):
    #Read key=value pairs from a file into a dict. Skips bad lines, handles missing file.
    config = {}
    try:
        with open(filename, "r") as f:
            data = f.read()
            lines = data.split("\n")
            for line in lines:
                if line == "":
                    continue
                parts = line.split("=")
                if len(parts) != 2:
                    print(f"Skipped malformed line: {line}")
                    continue
                key, value = parts[0], parts[1]
                config[key] = value
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    finally:
        print("Config read attempt finished.")
    return config


# ============================================================
# Testing all three functions
# ============================================================
if __name__ == "__main__":
    # --- Q1 ---
    print("--- Q1: parse_int_list ---")
    data = ["10", "dfj", "39", "3.9", "934", "abc"]
    output = parse_int_list(data)
    print("Final output:", output)

    # --- Q2 ---
    print("\n--- Q2: get_user_age ---")
    age = get_user_age()
    print(f"Your age is: {age}")

    # --- Q3 ---
    print("\n--- Q3: read_config_file ---")
    create_test_config()
    config = read_config_file("config.txt")
    print("Final config:", config)
    