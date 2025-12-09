**# FDTPro**
FDT Pro is a Python tool that generates frequency distribution tables for ungrouped and grouped data. It calculates frequencies, class intervals, cumulative frequencies, class marks, and percentages, allowing users to efficiently analyze whole-number datasets with interactive editing and clear, formatted outputs.

**#FDT Pro – User Instructions**
1. Prerequisites
  Required Python modules: tabulate, pyfiglet, colorama

  1.a) You can install all required modules via terminal/command prompt using:
      - pip install tabulate pyfiglet colorama
      
  1.b)Alternatively, if you have a requirements.txt file:
      - pip install -r requirements.txt

2. How the Program Works
  When you run FDT Pro, you will be prompted to choose between generating:
    (a) Grouped Frequency Distribution Table (Grouped FDT)
   (b) Ungrouped Frequency Distribution Table (Ungrouped FDT)

Follow the on-screen prompts carefully.

3. Entering Data
  Enter raw data separated by spaces.
  Example:
      10 15 20 20 25 30

  - Only whole numbers are allowed (integers).
  - Decimal values are not supported.

4. Editing Data
  After entering data, you can:
    (a) Add new values
    (b) Replace an existing value at a specific index
    (c) Delete a value by index
    (d) Continue if no changes are needed

5. Grouped FDT Specifics
   You will be asked to either enter the number of classes manually or use Sturges’ formula to compute it automatically.

   The program will calculate:
    - Class intervals
    - Class marks (midpoints)
    - Frequency
    - Relative Frequency
    - Relative Frequency Percentage

    Cumulative frequencies (<CF and >CF)

6. Ungrouped FDT Specifics
  The program calculates:
    - Frequency of each unique value
    - Relative frequency
    - Relative Frequency Percentage
    - Cumulative frequencies (<CF and >CF)

7. Menu Options During Execution
  After a table is displayed, you can choose:
    - Generate a new table (restart the process with new data)
    - Edit the current data (add, replace, or delete)
    - Exit the program

8. Input Rules
  Enter numbers only when numeric values are requested.
    - Menu options must match the numbers displayed on screen.
    - No blank inputs are allowed; every prompt requires an entry.
    - If invalid input is entered, the program will prompt you to try again.

9. Tips for Successful Operation
    - Read all prompts carefully.

Follow instructions for editing or entering data.

If the program rejects input or loops unexpectedly, check your input format and try again.

Restart the program if necessary by running the command again.
