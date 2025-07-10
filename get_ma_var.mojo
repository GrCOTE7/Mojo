fn main():
    
    # Open the file for reading
    try:
        with open("apps/count/n.txt", "r") as file:
            # Read the entire content of the file
            content = file.read()
            print("Content of input.txt:")
            print(content)
            
    except:
        print("Error: Could not read the file 'input.txt'")
