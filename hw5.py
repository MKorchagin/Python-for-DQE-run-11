import datetime as t
import random




#Create general class for all publications with 2 main input parameters
class Publication:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def output(self):
        #This variable (in all classes) was added after several errors for correct execution of the file operator
        article = (f"\n",f"\n"," Thank you for using our tool. \n Good luck and see you later!")
        return article


class News (Publication):
    def __init__(self, text, city):
        Publication.__init__(self, input1=text, input2=city)
        self.time = t.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    def output(self):
        article = (f"\n",f"\n","News------------", f"\n",
              f"{self.input1}"f"\n",
              f"{self.input2}, ", f"{self.time}")
        return article


class Advertising (Publication):
    def __init__(self, text, exp_date):
        Publication.__init__(self, input1=text, input2=exp_date)
        self.duration = t.datetime.strptime(self.input2, "%d-%m-%Y") - t.datetime.today()

    def output(self):
        article = (f"\n",f"\n","Privat Advertising------------" , f"\n" ,
              f"{self.input1}"f"\n" ,
              "Actual until ", f"{self.input2}. ", f"{self.duration.days}", " days left", )
        return article


class TrumpsQuote(Publication):
    def __init__(self, text, date = '01-01-2025'):
        Publication.__init__(self, input1=text,input2=date)
        self.rand = random.randint(0,1000000000)

    def output(self):
        article = (f"\n",f"\n","Trump's Quote------------" , f"\n" ,
              f"{self.input1}"f"\n" ,
              f"This phrase outraged {self.rand} people." )
        return article


#Function for checking input date format
def check_date_format(date_format="%d-%m-%Y"):
    da = f"Enter the expiration day in format {date_format}: \n"
    while True:
        input_date = input(da)
        try:
            # Attempt to parse the input date with the given format
            t.datetime.strptime(input_date, date_format)
            return input_date
        except ValueError:
            print(f"Invalid date! '{input_date}' does NOT match the format '{date_format}'. Please try again.")


#Main execution block. It can be refactored, but I can't understand how to do that with saving checks.
choice = None
print(" 1 - news", '\n',
       "2 - advert", "\n",
       "3 - Trump's quote", '\n',
       "q - quite", '\n')

while choice != '1' and choice != '2' and choice != '3' and choice != 'q' and choice != 'Q':
    choice = input("Please, choose what you want to publish: ")
    if choice == '1':
        input1 = input("You choose the News. \nPlease, enter the text of your News: \n")
        input2 = input("Enter the city\n")
        result = News(input1, input2)
    elif choice == '2':
        input1 = input("You choose the Advertising. \nPlease, enter the text of your Adv: \n")
        input2 = check_date_format()
        result = Advertising(input1,input2)
    elif choice == '3':
        input1 = input("You choose the \"Trump's Quote\". \nPlease, enter the quote:\n")
        result = TrumpsQuote (input1)
    elif choice.lower() == 'q':
        result = Publication('1', '1')
    else:
        print ("Please, select one of above")

article = ''.join(result.output())

print (article)
print(type(article))


with open ("HW_News.txt", "a") as file:
      file.write(str(article))

