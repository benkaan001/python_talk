# Positional arguments

def check_availability1(movie_name,available_seats):
    
    print(f"{movie_name} has only {available_seats} seats left!")

check_availability1("Black Panther", 60) # Black Panther has only 60 seats available
check_availability1(60, "Black Panther") # 60 has only Black Panther seats left!



# Keyword arguments
def check_availability2(movie_name, available_seats):
    
    print(f"{movie_name} has only {available_seats} seats left!")

check_availability2(available_seats=60, movie_name="Black Panther")
# Black Panther has only 60 seats left!


# Default arguments
def check_availability3(movie_name, available_seats = 100, show_time = "7:00pm"):
    
    print(f"{movie_name} that starts at {show_time} has {available_seats} left!")

check_availability3("Black Panther", 10, "9:00am")
# Black Panther that starts at 9:00am has 10 left!
check_availability3("Black Panther", 60)
# Black Panther that starts at 7:00pm has 60 left!
check_availability3("Black Panther")
# Black Panther that starts at 7:00pm has 100 left!


# Variable argument count
def shopping_cart_total(customer_id, *items):
    
    
    total = sum(item for item in items) if len(items)>0 else 'No payment needed'
    print(f"Total payment needed from client {customer_id}: {total} ")

shopping_cart_total("C10001", 100,200,300,50) # Total payment needed from client C10001: 650
shopping_cart_total("C10002") # Total payment needed from client C10002: No payment needed

    