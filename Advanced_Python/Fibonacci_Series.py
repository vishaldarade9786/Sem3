# Fibonacci series is a series in which the nubmer is sum of previous two numbers
def Find_Fibonacci(n):
    fibonacci_seq = [0,1]
    if n <= 0:
        return []
    if n == 1:
        return [0]
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(fibonacci_seq[-1]+fibonacci_seq[-2])
    return fibonacci_seq
if __name__ == "__main__":
    while True:
        print("--- Menu ---")
        print("1.Find fibonacci sequence for custom number ")
        print("2.exit")
        try: 
            choice = int(input("Enter your choice :"))
            if choice == 2:
                print(f"Exiting Gracefully")
                break
            elif choice == 1:
                n = int(input("Enter n :"))
                print(Find_Fibonacci(n))
            else:
                print("Enter valid Choice!!!")
        except ValueError:
            print("Please Enter valid values for intergers.")