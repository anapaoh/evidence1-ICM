# Evidence 4
## Weak Password Detector

For this evidence as a paradigm I chose scripting, thus using regex and python (personal preference). I looked up different options and came up with the idea of doing a weak password detectir taking the previous points into count.

These days, we all use passwords for pretty much everything: bank accounts, social media, apps, and more. 
The problem is that a lot of people use simple or weak passwords, we all have at least once used our pet's name as a pasword or something like “123456” or “password,” 
which are really easy to guess or hack. 

Sometimes these passwords are saved in plain text files or lists without checking if they’re secure and if this paswords are for somwthing important and end up being cracked up, it can be a serious problem.
Manually going through each password to see if it’s strong enough would take too much time and effort. 


This proyect checks for basic security rules like having at least 8 characters, a mix of upper and lowercase letters, numbers, and special characters. This is a useful tool because it can help people improve their password security in a quick and simple way, and it shows how scripting and regex can be used to solve real-life problems.

The goal of the script is to check if each password in a file is strong or weak. To do this, the program follows a simple, step-by-step logic:

- Read the file that contains a list of passwords (one per line).

- Use a regular expression to check each password against a pattern.

- The pattern looks for passwords that:

- Are at least 8 characters long

- Include both uppercase and lowercase letters

- Contain at least one number

- Have at least one special character (like !, @, #, etc.)

If a password doesn’t match the pattern, it is considered weak.

The script prints out whether each password is strong or weak.
![Start](https://github.com/user-attachments/assets/db6c8483-ac57-4f2f-84ad-65cf8647af6f)

Applied as regex sytaxis it would look something like this:
```
r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
```

### Explanation of the paradigm:

As said, this project uses scripting because it is ideal for small tasks that need automation, text processing, or interaction with files and the operating system.

The task involves:

- Reading a simple list of passwords from a text file
- Checking each password against a pattern
- Printing whether the password is strong or weak

Since it is a linear, text-processing task with no need for complex data structures or interfaces, scripting is the best option. The reasoning behind this is because:

1. Speed of Development
Scripting languages like Python allow fast implementation with minimal setup. The program was written in a few lines without needing to define classes, compile code, or build interfaces. This made it easy to focus on solving the problem rather than managing infrastructure.

2. Built-in Tools for Text Processing
Python has native support for:
- Regular expressions (via re)
- File handling (via open() and readlines())


3. No Need for Heavy Architecture
Using paradigms like object-oriented or functional programming would require unnecessary complexity:

- Class definitions
- State management
- Abstraction layers

Scripting is straight forward, yet just enough to solve this problem as required.

4. Immediate Execution (No Compilation)


#### Analysis
Time Complexity
This script reads a list of passwords from a file and checks each one using a regular expression. The analysis of time complexity is as follows:

File Reading:
The function file.readlines() reads all lines of the file into memory. This operation has a time complexity of O(n), where n is the number of passwords (lines in the file).

Iteration and Validation:
The script iterates over each password and applies a regular expression using re.match(). Each regular expression match operation has a time complexity of O(m), where m is the length of the password. However, since passwords are typically short and of similar size, this operation can be treated as O(1) in practice.

Overall Time Complexity:
The total time complexity of the script is O(n), where n is the number of passwords. Each password is checked once in a single pass through the file.

Alternative Paradigms and Tradeoffs
1. Scripting Paradigm (used):
This paradigm is ideal for small, linear automation tasks like this one. It is simple, easy to read, and quick to implement. However, it may become less maintainable in larger or more complex systems.

2. Object-Oriented Programming (OOP):
This approach could involve creating a Password class with methods like is_strong(). It would provide better structure and modularity, especially if the system were to expand. However, for a short and focused script like this, OOP would introduce unnecessary complexity. Time complexity would still be O(n).

3. Functional Programming:
Functional constructs like map() and filter() could replace loops for processing passwords. This could lead to more concise code but might reduce readability for beginners. It would not change the overall time complexity, which remains O(n).

4. Concurrent or Parallel Paradigm:
If processing a large dataset (e.g., millions of passwords), parallelizing the regex checks across multiple threads or processes could improve performance. In such a case, time complexity could approach O(n/p), where p is the number of available processing cores. However, for small to medium-sized files, the overhead of concurrency does not justify the added complexity.
