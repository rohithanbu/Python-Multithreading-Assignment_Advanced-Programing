✅ README.md
markdown
Copy
Edit
# 🧵 Multithreaded Algorithms in Python

This Python script contains multithreaded implementations of three common tasks:

1. **Multi-threaded Merge Sort**
2. **Multi-threaded Quicksort**
3. **Concurrent File Downloader** (using the `requests` library)

---

## 📝 Requirements

- Python 3.x
- `requests` library (for Task 3)

Install dependencies:

```bash
pip install requests
🚀 How to Run
bash
Copy
Edit
python multithreaded_algorithms.py
📋 What You'll See
🔢 Task 1: Merge Sort
Performs and compares single-threaded and multi-threaded merge sort on a list of 100,000 random integers.

🔢 Task 2: Quicksort
Performs and compares single-threaded and multi-threaded quicksort on another list of 100,000 random integers.

🌐 Task 3: Concurrent File Downloader
Downloads four web pages both sequentially and concurrently.

Example Output:

sql
Copy
Edit
=== Task 1: Multi-threaded Merge Sort ===
Single-threaded Merge Sort Time: 0.92
Multi-threaded Merge Sort Time: 0.54

=== Task 2: Multi-threaded Quicksort ===
Single-threaded Quicksort Time: 1.10
Multi-threaded Quicksort Time: 0.62

=== Task 3: Concurrent File Downloader ===
Sequential Download Time: 3.50
Concurrent Download Time: 1.10
📁 Files Included
multithreaded_algorithms.py — Combined implementation of all three tasks

README.md — Project documentation

📚 Optional Exploration
Try using concurrent.futures.ThreadPoolExecutor for easier thread management in all three tasks.

👨‍🎓 Author
Rohith
School of Computing and Data Science, Sai University
Advanced Programming Assignment – April 2025
