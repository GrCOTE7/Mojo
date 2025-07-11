fn main():
    try:
        # Directly specify the path to n.txt
        # var n_path = "benchmarks/langages1/count/n.txt"   
        var n_path = "langages1/count/n.txt" 
        
        with open(n_path, "r") as file:
            var n = atol(file.read().strip()) + 1
            for i in range(1, n):
                if i < 4:
                    print(i, end=", ")
    except:
        print("Error: Could not read the file 'n.txt'")

fn start_program():
    main()

# Note: The Python script will call `start_program()` using the Mojo environment
