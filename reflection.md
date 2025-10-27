Thinking Back on the Code Fixes

   1) What was easy to fix and what was tough?

Easy Wins:

Removing the security risk: Deleting the dangerous eval() function was a simple, instant safety upgrade.

Tidying up files: Using the with open(...) command made sure files always close correctly, preventing leaks.

The Hard Part:

Fixing silent failures: Replacing the lazy except: pass block. It was tough because we had to teach the code to check user inputs (like making sure the quantity is a number) before it broke, and then tell the user what went wrong.

2) Did the tools get anything wrong (false positives)?

Kind of. Pylint complained about using global stock_data.

In a big, fancy program, global is bad, but for our tiny, simple inventory script, using one central data spot is the clearest way to run the app. So, for us, that warning was mostly noise.

3) How should we use these tools when building real software?

While Coding: Use a "pre-commit" check that runs quick style tools (like Flake8) every time you try to save changes. This forces developers to clean up small mistakes right away.

When Sharing: Use a CI system (Continuous Integration) to run the full security check (Bandit) and quality check (Pylint) every time code is shared. If the security score is bad, the system should stop the code from being merged.

4)What got better after we fixed the code?

Toughness: The code is much more reliable. We added "rules" (input validation) so if a user tries to enter a bad number or an item that doesn't exist, the program handles it without crashing.

Safety: We eliminated the biggest security hole by removing eval().

Clarity: Switching to snake_case for function names and using modern f-strings made the code look cleaner and easier for any programmer to read quickly.
