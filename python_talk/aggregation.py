'''
Create a simple Gym has-A Member aggregation relationship and include
a static variable and set all class attributes to private
'''
class Member:

    def __init__(self,member_name, license_id, member_zip_code, number_of_sessions):
        self.__member_name = member_name
        self.__member_id = license_id
        self.__member_zip_code = member_zip_code
        self.__number_of_sessions = number_of_sessions
    
    def get_member_name(self):
        return self.__member_name
    
    def get_member_id(self):
        return self.__member_id
    
    def get_member_zip_code(self):
        return self.__member_zip_code
    def get_number_of_sessions(self):
        return self.__number_of_sessions
    
    def validate_membership(self):
        # if license id starts with the first letter of the member name
        # and has a total of four characters return true
        return self.__member_name == self.__member_name.split()[0] and len(self.__member_id) == 4
        

class Gym:
    local_id_counter =100
    non_local_id_counter =1000
    def __init__(self,location,member):
        self.__location = location
        self.__member =member
        self.__member_id =None
        self.__membership_fee = None
    
    def get_location(self):
        return self.__location
    def get_member(self):
        return self.__member
    def get_non_local_member(self):
        return self.__non_local_member
    
    # validate if the member is local
    # local member's zip code's first 3 digits must match the gym's zip code
    def validate_local(self):
        return str(self.__location)[0:3] == str(self.__member.get_member_zip_code())[0:3]
    
    ## assign gym id number
    def assign_id_num(self):
        if(self.validate_local()):
            Gym.local_id_counter+=1
            self.__member_id = Gym.local_id_counter
        else:
            Gym.non_local_id_counter+=1
            self.__member_id = Gym.non_local_id_counter
        
        return self.__member_id
        
    # if non-local member has more than 3 personal trainer sessions
    # charge local price
    def get_membership_fee(self):
        if(self.validate_local() or self.__member.get_number_of_sessions() >3):
            self.__membership_fee = 75
        else:
            self.__membership_fee = 100
            
        return self.__membership_fee
            
       
member1 = Member('John','J101', 78752, None)
member2 = Member('Marry', 'M199', 81002,4)
member3 = Member('Sammy', 'S855', 42250, 3)
gym1 = Gym(78754, member1)
gym2 = Gym(78754, member2)
gym3 = Gym(78754, member3)

gyms = [gym1,gym2,gym3]

for i in range (len(gyms)):
    print('member', i+1, 'is assigned membership number#',gyms[i].assign_id_num(), end='\n')
    print('member', i+1, 'membership costs', gyms[i].get_membership_fee())

# member 1 is assigned membership number# 101
# member 1 membership costs 75
# member 2 is assigned membership number# 1001
# member 2 membership costs 75
# member 3 is assigned membership number# 1002
# member 3 membership costs 100 

