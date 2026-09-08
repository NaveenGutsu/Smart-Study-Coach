print("=== Welcome to Your Smart Study Coach! ===")

hours_slept = float(input("How many hours did you sleep last night? "))
tasks_left = int(input("How many tasks do you have on your to-do list? "))

print("\nAnalyzing your day...")

if hours_slept < 5:
    print("Decision: Low battery mode! Take a 20-minute power nap before starting.")
elif hours_slept >= 8 and tasks_left > 5:
    print("Decision: High energy detected! Tackle your hardest 2 tasks first.")
elif hours_slept >= 6 and tasks_left <= 3:
    print("Decision: Smooth sailing! Finish tasks in 25-minute focus sprints.")
else:
    print("Decision: Balanced mode! Pace yourself and take a 5-minute break every hour.")
