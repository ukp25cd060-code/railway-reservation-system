import random

# Total seats
TOTAL_SEATS = 10
seats = [0] * TOTAL_SEATS   # 0 = free, 1 = booked

bookings = {}

def check_availability():
    available = seats.count(0)
    print(f"\nAvailable Seats: {available}/{TOTAL_SEATS}")

def book_ticket():
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    if 0 not in seats:
        print("No seats available!")
        return

    seat_no = seats.index(0)
    seats[seat_no] = 1

    booking_id = random.randint(1000, 9999)

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_no + 1
    }

    print(f"\nTicket Booked Successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Seat Number: {seat_no + 1}")

def view_ticket():
    bid = int(input("Enter Booking ID: "))

    if bid in bookings:
        data = bookings[bid]
        print("\n--- Ticket Details ---")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Seat No: {data['seat']}")
    else:
        print("Invalid Booking ID!")

def cancel_ticket():
    bid = int(input("Enter Booking ID: "))

    if bid in bookings:
        seat_no = bookings[bid]['seat'] - 1
        seats[seat_no] = 0
        del bookings[bid]
        print("Ticket Cancelled Successfully!")
    else:
        print("Invalid Booking ID!")

# Main Menu
while True:
    print("\n===== Railway Reservation System =====")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        check_availability()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        view_ticket()
    elif choice == '4':
        cancel_ticket()
    elif choice == '5':
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
