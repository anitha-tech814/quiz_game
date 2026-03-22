score = 0

print("Welcome to Quiz Game 🎮")

# Question 1
answer = input("Q1: What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 2
answer = input("Q2: 2 + 2 = ? ")
if answer == "4":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 3
answer = input("Q3: Which language is used for AI? ")
if answer.lower() == "python":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

print("\nFinal Score:", score)
