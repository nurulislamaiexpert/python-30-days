# ফাইলের নাম: calculator.py
# উদ্দেশ্য: ইনপুট নেওয়া এবং শর্ত (if-else) ব্যবহার শেখা

print("--- আমার প্রথম ক্যালকুলেটর ---")

# ১. ইউজার থেকে দুটি সংখ্যা নেওয়া (input সবসময় টেক্সট হিসেবে আসে, তাই int() দিয়ে সংখ্যায় রূপান্তর করছি)
num1 = int(input("প্রথম সংখ্যাটি লিখুন: "))
num2 = int(input("দ্বিতীয় সংখ্যাটি লিখুন: "))

# ২. অপারেটর জিজ্ঞেস করা
print("\nকোন কাজটি করতে চান? (+, -, *, /) ")
operator = input("অপারেটর লিখুন: ")

# ৩. if-else দিয়ে সিদ্ধান্ত নেওয়া
if operator == "+":
    result = num1 + num2
    print("যোগফল:", result)
elif operator == "-":
    result = num1 - num2
    print("বিয়োগফল:", result)
elif operator == "*":
    result = num1 * num2
    print("গুণফল:", result)
elif operator == "/":
    if num2 == 0:
        print("ভুল! শূন্য দিয়ে ভাগ করা যায় না।")
    else:
        result = num1 / num2
        print("ভাগফল:", result)
else:
    print("আপনি ভুল অপারেটর দিয়েছেন!")

print("--- প্রোগ্রাম শেষ ---")
