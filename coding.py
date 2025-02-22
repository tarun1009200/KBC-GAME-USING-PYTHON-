question = [
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ],
    [
        "Which language was used to create WhatsApp?",
        "Hindi", "Java", "C++", "Python", "None", 4
    ]
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(question)):
    q = question[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {q[1]}             b. {q[2]}")
    print(f"c. {q[3]}             d. {q[4]}")
    jawab = int(input("Enter your answer (1-4) or 0 to quit: "))
    if (jawab == 0):
        money= levels[i-1]
        break
    if jawab == q[-1]:
        print(f"Congratulations, Computer ji ne kaha hain ki aap ka jawab ek dam sahi hain! Rs. {levels[i]}")
        if i == 4:
            money = 1000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Computer ji ne kaha hain ki aap ka jawab galat hain.")
        break

print(f"You have won Rs. {money}")




