# Fibonacci series is a series in which the nubmer is sum of previous two numbers
def Tabulation_Fibonacci(n):
    fibonacci_seq = [0,1]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    while len(fibonacci_seq) <= n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq

def Memoization_Fibonacci(n ,memo=None)-> int:
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        ans = Memoization_Fibonacci(n-1,memo) + Memoization_Fibonacci(n-2,memo)
        memo[n] = ans
        return memo[n]
    
if __name__ == "__main__":
    while True:
        print("--- Menu ---")
        print("1.Find Fibonacci sequence through Tabulation")
        print("2.Find Fibonacci sequence through Memoization")
        print("3.exit")
        try: 
            choice = int(input("Enter your choice :"))
            if choice == 3:
                print(f"Exiting Gracefully")
                break
            elif choice == 2:
                n = int(input("Enter n :"))
                print(Memoization_Fibonacci(n))
            elif choice == 1:
                n = int(input("Enter n :"))
                print(Tabulation_Fibonacci(n))
            else:
                print("Enter valid Choice!!!")
        except ValueError:
            print("Please Enter valid values for intergers.")