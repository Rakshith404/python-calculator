import math

last_result = 0
history = []

allowed_functions = {
    "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error",
    "pow": pow,
    "abs": abs,
    "round": round,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log,
    "log10": math.log10
}

def calculator():
    global last_result, history

    calculation = input("Enter your calculation: ").strip().lower()
    calculation = calculation.replace("ans", str(last_result))

    exit_commands = ["exit", "quit", "q", "bye"]
    if calculation in exit_commands:
        print("Exiting calculator. Bye boss 👋")
        return "exit"

    if calculation == "history":
        if not history:
            print("No history yet.")
        else:
            print("---- History ----")
            for i, item in enumerate(history, start=1):
                print(f"{i}) {item}")
        return

    if calculation and calculation[0] in "+-*/":
        calculation = str(last_result) + calculation

    allowed_chars = "0123456789+-*/(). ,abcdefghijklmnopqrstuvwxyz"
    for char in calculation:
        if char not in allowed_chars:
            print("Invalid character detected:", char)
            return

    try:
        result = eval(
            calculation,
            {"__builtins__": None},
            allowed_functions
        )
    except:
        print("Invalid operation")
        return

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print("The result is:", result)
    history.append(f"{calculation} = {result}")
    last_result = result

    clear_memory = input("r or c: ").strip().lower()
    if clear_memory == "c":
        last_result = 0


choice = "y"
while choice == "y":
    status = calculator()
    if status == "exit":
        break
    choice = input("Do you want to continue? (y/n): ").strip().lower()