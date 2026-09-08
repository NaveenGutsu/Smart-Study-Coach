# Task Managing Adviser (Smart Study Coach)

A lightweight Python script that acts like a personal productivity coach. It takes your daily energy inputs (sleep hours and pending tasks) and uses conditional logic (`if-elif-else`) to recommend the best way to tackle your day.

---

## Features

* **Interactive CLI Input:** Prompts for hours slept and number of remaining tasks.
* **Smart Decision Logic:** Evaluates multiple conditions using logical operators (`and`, `>=`).
* **Tailored Feedback:** Recommends action plans ranging from quick power naps to high-focus deep work sprints.

---

## Logic Breakdown

| Sleep Hours | Tasks Pending | Recommended Strategy |
| :--- | :--- | :--- |
| `< 5` | Any | **Low battery mode:** Take a 20-minute power nap |
| `>= 8` | `> 5` | **High energy mode:** Tackle the 2 hardest tasks first |
| `>= 6` | `<= 3` | **Smooth sailing:** Focus sprints (25-minute Pomodoro) |
| Any other case | Any other case | **Balanced mode:** Steady pacing with regular breaks |

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/task-managing-adviser.git](https://github.com/your-username/task-managing-adviser.git)
