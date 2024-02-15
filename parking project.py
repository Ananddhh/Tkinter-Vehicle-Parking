import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize parking lots
total_parking_lots = 15
occupied_lots = 0

# Dictionary to store parked vehicles' details
parked_vehicles = {}

# Function to handle the vehicle entry
def vehicle_entry():
    global occupied_lots
    if occupied_lots < total_parking_lots:
        entry_window = tk.Toplevel(root)
        entry_window.title("Vehicle Entry")

        def submit_entry():
            vehicle_number = vehicle_number_entry.get()
            vehicle_type = vehicle_type_entry.get()
            vehicle_name = vehicle_name_entry.get()
            owner_name = owner_name_entry.get()
            date = date_entry.get()
            time = time_entry.get()

            parked_vehicles[vehicle_number] = {
                "Vehicle Type": vehicle_type,
                "Vehicle Name": vehicle_name,
                "Owner Name": owner_name,
                "Entry Time": f"{date} {time}"
            }

            messagebox.showinfo("Success", "Vehicle entry added successfully!")
            entry_window.destroy()

        tk.Label(entry_window, text="Enter Vehicle number (xxxx-xx-xxxx):").pack()
        vehicle_number_entry = tk.Entry(entry_window)
        vehicle_number_entry.pack()

        tk.Label(entry_window, text="Enter vehicle type (bicycle=A/Bike=B/car=C):").pack()
        vehicle_type_entry = tk.Entry(entry_window)
        vehicle_type_entry.pack()

        tk.Label(entry_window, text="Enter Vehicle name:").pack()
        vehicle_name_entry = tk.Entry(entry_window)
        vehicle_name_entry.pack()

        tk.Label(entry_window, text="Enter owner name:").pack()
        owner_name_entry = tk.Entry(entry_window)
        owner_name_entry.pack()

        tk.Label(entry_window, text="Enter Date (dd-mm-yyyy):").pack()
        date_entry = tk.Entry(entry_window)
        date_entry.pack()

        tk.Label(entry_window, text="Enter time (HH:MM:SS):").pack()
        time_entry = tk.Entry(entry_window)
        time_entry.pack()

        tk.Button(entry_window, text="Submit", command=submit_entry).pack()
        occupied_lots += 1
    else:
        messagebox.showwarning("Parking Full", "Sorry, parking is full!")

# Function to handle the Remove Entry option
def remove_entry():
    global occupied_lots
    # global total_parking_lots
    entry_window = tk.Toplevel(root)
    entry_window.title("Remove Entry")
    count=0

    def submit_remove():
        global occupied_lots
        vehicle_number = vehicle_number_entry.get()
        if vehicle_number in parked_vehicles:
            del parked_vehicles[vehicle_number]
            messagebox.showinfo("Success", f"Vehicle removed from parking!")
            occupied_lots -= 1
        
        else:
            messagebox.showwarning("Not Found", "Vehicle not found in parking!")
        entry_window.destroy()

    # if count==1:
    #     occupied_lots = occupied_lots - 1
    #     print (occupied_lots)
    #     count=0
    tk.Label(entry_window, text="Enter Vehicle number (xxxx-xx-xxxx):").pack()
    vehicle_number_entry = tk.Entry(entry_window)
    vehicle_number_entry.pack()

    tk.Button(entry_window, text="Submit", command=submit_remove).pack()

# Function to handle the View parked Vehicle option
def view_parked_vehicle():
    vehicle_list_window = tk.Toplevel(root)
    vehicle_list_window.title("Parked Vehicles")

    if parked_vehicles:
        for vehicle_number, details in parked_vehicles.items():
            tk.Label(vehicle_list_window, text=f"Vehicle Number: {vehicle_number}").pack()
            for key, value in details.items():
                tk.Label(vehicle_list_window, text=f"{key}: {value}").pack()
            tk.Label(vehicle_list_window, text="---------------------------").pack()
    else:
        tk.Label(vehicle_list_window, text="No vehicles parked currently").pack()



def calculate_bill():
    entry_window = tk.Toplevel(root)
    entry_window.title("Calculate Bill")

    def submit_bill():
        vehicle_number = vehicle_number_entry.get()
        exit_time = exit_time_entry.get()
        
        if vehicle_number in parked_vehicles:
            vehicle_type = parked_vehicles[vehicle_number]["Vehicle Type"]
            if vehicle_type == "A" or vehicle_type == "bicycle":
                bill_amount = 20  # 20 rupees per minute for bicycle
            elif vehicle_type == "B" or vehicle_type == "bike":
                bill_amount = 30  # 30 rupees per minute for bike
            elif vehicle_type == "C" or vehicle_type == "car":
                bill_amount = 40  # 40 rupees per minute for car
            else:
                messagebox.showwarning("Invalid Vehicle Type", "Invalid vehicle type entered!")
                entry_window.destroy()
                return

            messagebox.showinfo("Bill", f"Bill amount: {bill_amount} rupees")
        else:
            messagebox.showwarning("Not Found", "Vehicle not found in parking!")
        entry_window.destroy()

    tk.Label(entry_window, text="Enter Vehicle number (xxxx-xx-xxxx):").pack()
    vehicle_number_entry = tk.Entry(entry_window)
    vehicle_number_entry.pack()

    tk.Label(entry_window, text="Exit time (HH:MM:SS):").pack()
    exit_time_entry = tk.Entry(entry_window)
    exit_time_entry.pack()

    tk.Button(entry_window, text="Submit", command=submit_bill).pack()
# Function to handle the View left parking lots option
def view_left_parking_lots():
    messagebox.showinfo("Parking Status", f"Total parking lots: {total_parking_lots}\nOccupied lots: {occupied_lots}\nLeft parking lots: {total_parking_lots - occupied_lots}")

# Create the main window
root = tk.Tk()
root.title("Vehicle Parking Management")

# Create buttons for different options with improved layout
tk.Button(root, text="Vehicle Entry", width=20, command=vehicle_entry).pack(pady=5)
tk.Button(root, text="Remove Entry", width=20, command=remove_entry).pack(pady=5)
tk.Button(root, text="View parked Vehicle", width=20, command=view_parked_vehicle).pack(pady=5)
tk.Button(root, text="Bill", width=20, command=calculate_bill).pack(pady=5)
tk.Button(root, text="View left parking lots", width=20, command=view_left_parking_lots).pack(pady=5)
tk.Button(root, text="Exit Programme", width=20, command=root.destroy).pack(pady=5)

root.mainloop()

