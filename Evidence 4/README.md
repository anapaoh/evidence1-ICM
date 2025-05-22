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

<pre> **Flow Diagram – Weak Password Detector** +----------------------------+ | Start | +----------------------------+ | v +----------------------------+ | Open file with passwords | +----------------------------+ | v +----------------------------+ | For each password (line): | +----------------------------+ | v +----------------------------+ | Apply regex pattern check | +----------------------------+ | v +------------------+ | Does it match? | +--------+---------+ | +-------+--------+ | | v v +-----------+ +-------------+ | Strong | | Weak | +-----------+ +-------------+ | | +--------+-------+ | v +------------------------+ | Print result | +------------------------+ </pre>
