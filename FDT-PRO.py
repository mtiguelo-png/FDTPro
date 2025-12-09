from tabulate import tabulate
import math as m
import pyfiglet
from colorama import Fore, Style

##########################################
## Grouped Frequency Distribution Table ##
##########################################

# Gets input for raw data of Grouped FDT
def get_input1():
    try:
        print("\nEnter the raw data separated by spaces. Must be integers.")
        data1 = input(": ")
        array1 = [float(x) for x in data1.split()]
        array1.sort()
        if len(array1) == 0:
            print("You \033[31mDID NOT\033[0m enter any data. Try again.")
            return get_input1()
        num_of_class = num_of_class_func(array1)
        return array1, num_of_class
    except ValueError:
        print("\033[31mINVALID\033[0m input. Try again.")
        return get_input1()

def num_of_class_func(array1):
    try:
        print("\nDo you wish to enter the number of classes or have it computed using Sturges' Formula?")
        print(" Enter (1) for manual input.")
        print(" Otherwise for Sturges' Formula.")
        choice = input(": ")
        if choice == "1":
            num = int(input("\nEnter the number of classes. Must be a positive integer: "))
            if num <= 0:
                print("\nNumber of classes \033[31mMUST\033[0m be a \033[31mPOSITIVE INTEGER\033[0m. Try again.")

                return num_of_class_func(array1)
            else:
                return num
        else:
            n = len(array1)
            suggested = round(1+3.322*m.log10(n))
            print(f"\nSuggested number of classes (Sturges' Formula): {suggested}")
            return suggested
    except ValueError:
        print("\n\033[31mINVALID\033[0m input. Must be a \033[31mPOSITIVE INTEGER\033[0m. Try again.")
        return num_of_class_func(array1)

# Solves intervals for Grouped FDT
def get_interval1(lowest, width, k):
    interval = []
    lower_lim = lowest
    for i in range(k):
        upper_lim = lower_lim+width-1
        interval.append((lower_lim, upper_lim))
        lower_lim = upper_lim + 1
    return interval

# Solves class mark of each data for Grouped FDT
def get_CM1(inter):
    class_mark = []
    for low, up in inter:
        CM = (low + up) / 2
        class_mark.append(CM)
    return class_mark

# Solves frequency of each data for Grouped FDT
def get_freq1(data2, inter):
    freqs = []
    for low, up in inter:
        freq = sum(1 for x in data2 if up>=x>=low)
        freqs.append(freq)
    return freqs

# Solves relative frequency of each data for Grouped FDT
def get_RF1(frequ, n):
    RF1 = []
    RFP1 = []
    for i in frequ:
        rf = i/n
        rfp = rf*100
        RF1.append(round(rf, 2))
        RFP1.append(round(rfp, 2))
    return RF1, RFP1

# Solves cumulative frequency of each data for Grouped FDT
def get_CF1(freque):
    GCF = []
    LCF = []
    gcf = 0
    lcf = 0
    for i in freque:
        lcf += i
        LCF.append(lcf)
    for k in reversed(freque):
        gcf += k
        GCF.append(gcf)
    GCF.reverse()
    return LCF, GCF

def grouped_fdt(data, num_of_class):
    data = edit_data(data)
    data.sort()

    n = len(data)
    if n == 0:
        print("\033[31mNO\033[0m data \033[31mREMAINING\033[0m. Try again.")
        return data

    lowest_val = (data[0])
    highest_val = (data[-1])
    rangee = highest_val-lowest_val
    if rangee == 0:
        print("All data values are \033[31mEQUAL\033[0m. Grouped table \033[31mCANNOT\033[0m be formed. Try again.")
        return data

    class_width = m.ceil(rangee/num_of_class)

    if class_width <= 0:
        print("\033[31mINVALID\033[0m class width. Data range \033[31mTOO SMALL\033[0m to form group classes.")
        return data

    interval = get_interval1(lowest_val, class_width, num_of_class)

    CM = get_CM1(interval)

    frequency = get_freq1(data, interval)

    RF1, RFP1 = get_RF1(frequency, n)

    LCF, GCF = get_CF1(frequency)

    print("\033[3;35m GROUPED FREQUENCY DISTRIBUTION TABLE\033[0m")

    table = []
    headers = ["Class Intervals", "Frequency", "CM", "RF", "RFP", "<CF", ">CF"]
    for i in range(len(frequency)):
        low = round(interval[i][0], 2)
        up = round(interval[i][1], 2)
        cm = round(CM[i], 2)
        table.append([(low, up), frequency[i], cm, RF1[i], RFP1[i], LCF[i], GCF[i]])
    print(tabulate(table, headers=headers, tablefmt="pretty"))

    return data


############################################
## Ungrouped Frequency Distribution Table ##
############################################

# Gets input for raw data of Ungrouped FDT
def get_input2():
    try:
        print("\nEnter the raw data separated by spaces. Must be integers.")
        data2 = input(": ")
        array2 = [float(x) for x in data2.split()]
        if len(array2) == 0:
            print("You \033[31mDID NOT\033[0m enter any data. Try again.")
            return get_input2()
        return array2
    except ValueError:
        print("\033[31mINVALID\033[0m input. Try again.")
        return get_input2()

# Displays values on the table for Ungrouped FDT
def get_values2(data3):
    X = []
    for i in data3:
        if i not in X:
            X.append(i)
        else:
            continue
    return sorted(X)

# Solves frequency of each data for Ungrouped FDT
def get_freq2(data4, x):
    F = []
    for i in x:
        F.append(data4.count(i))
    return F

# Solves cumulative frequency of each data for Ungrouped FDT
def get_CF2(frequ):
    GCF2 = []
    LCF2 = []
    gcf2 = 0
    lcf2 = 0
    for i in frequ:
        lcf2 += i
        LCF2.append(lcf2)
    for k in reversed(frequ):
        gcf2 += k
        GCF2.append(gcf2)
    GCF2.reverse()
    return LCF2, GCF2

# Solves relative frequency of each data for Ungrouped FDT
def get_RF2(freq, n):
    RF2 = []
    RFP2 = []
    for i in freq:
        rf = i/n
        rfp = rf*100
        RF2.append(round(rf, 2))
        RFP2.append(round(rfp, 2))
    return RF2, RFP2

def ungrouped_fdt(data):
    data = edit_data(data)
    data.sort()

    n = len(data)
    if n == 0:
        print("\033[31mNO\033[0m data \033[31mREMAINING\033[0m. Try again.")
        return

    X = get_values2(data)

    F = get_freq2(data, X)

    RF2, RFP2 = get_RF2(F, n)

    LCF2, GCF2 = get_CF2(F)

    print("\033[3;35m UNGROUPED FREQUENCY DISTRIBUTION TABLE\033[0m")

    table2 = []
    headers = ["X", "Frequency", "RF", "RFP", "<CF", ">CF"]
    for i in range(len(F)):
        table2.append([X[i], F[i], RF2[i], RFP2[i], LCF2[i], GCF2[i]])
    print(tabulate(table2, headers=headers, tablefmt="pretty"))

    return data

##########################
## OPTIONS TO EDIT DATA ##
##########################

def edit_data(data5):
    while True:
        print("\nYour current data list (indexed):")
        for i, val in enumerate(data5):
            print(f"[{i}] {val}")

        print("\nWould you like to modify your data?")
        print(" Enter (1) to \033[33mADD\033[0m data")
        print(" Enter (2) to \033[33mREPLACE\033[0m data")
        print(" Enter (3) to \033[33mDELETE\033[0m data")
        print(" Otherwise to \033[33mCONTINUE\033[0m")
        choice = input(": ")

        if choice == "1":
            values = (input("\nEnter data to ADD (separate with spaces): "))
            try:
                new_values = [float(x) for x in values.split()]
                data5.extend(new_values)
                print("\n\033[32mData added successfully.\033[0m")
            except ValueError:
                print("\n\033[31mINVALID\033[0m input, please try again.")

        elif choice == "2":
            try:
                index = int(input("\nEnter the INDEX of the data to REPLACE: "))
                if index < 0 or index >= len(data5):
                    print("\n\033[31mINVALID\033[0m index, try again.")
                    continue
                else:
                    new_value = float(input(f"Enter new value for index {index}: "))
                    data5[index] = new_value
                    print("\n\033[32mData updated successfully.\033[0m")
            except ValueError:
                print("\n\033[31mINVALID\033[0m input, please try again.")

        elif choice == "3":
            try:
                index = int(input("\nEnter the INDEX of the data to DELETE: "))
                if index < 0 or index >= len(data5):
                    print("\n\033[31mINVALID\033[0m index, try again.")
                    continue
                else:
                    data5.pop(index)
                    print("\n\033[32mData deleted successfully.\033[0m")
            except ValueError:
                print("\n\033[31mINVALID\033[0m input, please try again.")

        else:
            break

    data5.sort()

    if len(data5) == 0:
        print("Dataset \033[31mCANNOT\033[0m be \033[31mEMPTY\033[0m. Please add at least one value.")
        return edit_data(data5)

    return data5


###################
## MAIN FUNCTION ##
###################

def main_function():
    while True:
        print("\nDo you want to generate \033[34mGROUPED\033[0m or \033[34mUNGROUPED\033[0m Frequency Distribution Table?")
        print(" Enter (1) for Grouped FDT")
        print(" Otherwise for Ungrouped FDT.")
        choice = input(": ")
        if choice == "1":
            while True:
                data, num_of_class = get_input1()

                while True:
                    data = grouped_fdt(data, num_of_class)

                    print("\nOPTIONS:")
                    print(" Enter (1) to \033[33mGENERATE NEW\033[0m table.")
                    print(" Enter (2) to \033[33mEDIT\033[0m data of the current table.")
                    print(" Otherwise to \033[33mEXIT\033[0m")
                    decision = input(": ")

                    if decision == "1":
                        break
                    elif decision == "2":
                        continue
                    else:
                        return
                break

        else:
            while True:
                data = get_input2()

                while True:
                    data = ungrouped_fdt(data)

                    print("\nOPTIONS:")
                    print(" Enter (1) to \033[33mGENERATE NEW\033[0m table.")
                    print(" Enter (2) to \033[33mEDIT\033[0m data of the current table.")
                    print(" Otherwise to \033[33mEXIT\033[0m")
                    decision = input(": ")

                    if decision == "1":
                        break
                    elif decision == "2":
                        continue
                    else:
                        return
                break

ascii_banner = pyfiglet.figlet_format("WELCOME TO FDT PRO", font="slant")
print(Fore.BLUE + Style.BRIGHT + ascii_banner + Style.RESET_ALL)

main_function()
