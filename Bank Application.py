import sys
from abc import ABC,abstractmethod
import random
import datetime
import string

class Util:
    
    
    @staticmethod
    def accnum():
        s=''
        for i in range(12):
            s+=str(random.randint(0,9))
        return s
    @staticmethod
    def randusername():
        
        alp =list(string.ascii_lowercase)
        ALP=list(string.ascii_uppercase)
        num =str(random.randint(0,9))
        l=[random.choice(alp),random.choice(ALP),random.choice(num)]
        random.shuffle(l)
        r=''.join(l)
        return r
    @staticmethod
    def setter(obj_ref,acctyp):
        obj_ref.set_name(acctyp)
        obj_ref.set_dob(acctyp)
        obj_ref.set_username()
        obj_ref.set_password()
        obj_ref.set_balance()
        obj_ref.set_cust_list(acctyp)
        obj_ref.set_tranlist('{} Account created on {}'.format(acctyp,datetime.datetime.now()))
        print('*'*40)
        print('Your {} Account created successfully'.format(acctyp))
        print('-'*40)
        obj_ref.get_accdtl()
        print('-'*40)
        print('Please Save your {} Account user name "{}" and password is "{}" for future Use'.format(acctyp,obj_ref.get_username(),obj_ref.get_password()))
        print('*'*40)
    @staticmethod    
    def validator(): ##validator to validate{name ::[dob,accnum,username,password,object refrence]}
        a= input('Type \'Y\' for Yes and \'N\' for No if you have an Account in {}  ::'.format(Account.BANKNAME)).upper()
        count=0
        while a not in ['Y','N']:
            
            a= input('You are left with {} chances\nPlease choose correct option as displayed\nDo You have an Account in {} Type [Y|N] :: '.format((3-count),Account.BANKNAME)).upper()
            count+=1
            if count>3:
                sys.exit('You are not aware about your Account')
        if a=="N" :
            return (None,None)
        else:
            count=0
            while count!=3:
                count+=1
                us_nm=input('Please enter your username :').strip()
                us_pass=input('Please enter your password :').strip()
                for dict in Account.cust_list:
                    for key in dict:
                        
                            
                        
                        if us_nm==dict[key][2] and us_pass==dict[key][3]:
                            print('You have been validated successfully\n')
                            return dict[key][5],dict[key][4]
                            
                        
                if (3-count)!=0:
                    print('Wrong Credentials\nPlease enter correct credentials Remaining attempts {}'.format(3-count))
                else:
                    print('All attempts exhausted')
                        
                            
            sys.exit('You are not validated Successfully')        
    @staticmethod
    def havingaccount():
        
        obj_ref,typ=Util.validator()
        if obj_ref==None:
            count=0
            inp=input('Please create Your Account to continue with some Transaction\nHit -1 To open an Account ::')
            while inp not in ['1']:
                count+=1
                inp=input('You are available with {} attempts\nPlease create Your Account to continue with some Transaction\nHit -1 To open an Account ::'.format((3-count)))
                if count >3:
                    sys.exit('You are not willing to create account\nSytem exit')
            return False
        else:
            return obj_ref,typ
class Account(ABC):
    BANKNAME = 'State Bank Of India'
    METCHRG=10
    NONMETCHRG=5
    cust_list=[]
    name_list=[]
    no_of_obj=0
    
    def __init__(self,name='',dob='',balance=0,withdrl_count_nonmetro=0,metro_count=0,nonmetro_count=0,city='',username='',password='',tranlist=[],withdrl_count_metro=0):
        self.name=name#{name ::[dob,accnum,username,password,object refrence]}
        self.dob=dob
        self.accnum=Util.accnum()
        self.balance=balance
        self.city=city                  
        self.__username=username
        self.__password=password
        self.metro_count=metro_count
        self.nonmetro_count=nonmetro_count
        self.tranlist= list() ########## to save the transaction details with respect to individual account 'Not creating copies'
        self.withdrl_count_metro=withdrl_count_metro
        self.withdrl_count_nonmetro=withdrl_count_nonmetro
    def set_tranlist(self,trandtl):
        self.tranlist.append(trandtl)
    def get_tranlist(self):
        return self.tranlist
    def set_cust_list(self,acctyp):
        Account.cust_list.append({})
        Account.cust_list[Account.no_of_obj][self.name]=[self.get_dob(),self.accnum,self.__username,self.get_password(),'{} Account'.format(acctyp),self]
        Account.no_of_obj+=1
    def get_cust_list(self):
        return Account.cust_list
    def set_username(self):
        self.__username=self.name[:2]+Util.randusername()+'@xyz.com'
    def set_password(self):
        self.__password=Util.randusername()+self.name[-2:].strip()
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def set_city(self):
        count=0
        ip=input('enter city as "metro" or "non-metro" city :: ').strip().lower()
        while ip not in ['metro','non-metro']:
            if count>3:
                sys.exit('All attempts Exhausted\nSystem Exit')
            
            ip =input('{} Attempts remaining\nEnter city as "metro" or "non-metro" city :: '.format(2-count)).strip().lower()
            count+=1
        self.city=ip
    def get_city(self):
        return self.city
    def set_name(self,acctyp):
        count=0
        while count<3:
            if acctyp=='Savings':
                nm=input('enter full name :: ').strip().split()
            else:
                nm=input('enter Company name :: ').strip().split()
            if len(nm)==0:
                count+=1
                if count!=3:
                    
                    print('Name can\'t be an empty field\nYou are left with {} Attempts'.format(3-count))
                
                continue
            count+=1
            cc=''
            for i in nm:
                if i.isalpha():
                    cc+=i+' '
                else :
                    print('Incorrect Name')
                    print('Please enter correct alphabetical name according to naming standards\n You have {} attempts remaining'.format((3-count)))
                    break
            if len(nm)==len(cc.split()):
                self.name=cc
                Account.name_list.append(cc)
                break
        if len(nm)==0:
            sys.exit('Exhausted all Attempts\nSystem Exit')
        
    def get_name(self):
        return self.name
    def set_dob(self,acctyp):
        
        count=0
        
        while True:    
            if count>2:
                print('All 3 Attempts Exhausted')
                sys.exit('System Exit')
            try:
                
                if acctyp == 'Savings':
                    birthday = input("Enter your date of birth:in %d/%m/%cY format :: ")
                else:
                    birthday = input("Enter Company Foundation Date:in %d/%m/%cY format :: ")
                bday = datetime.datetime.strptime(birthday, '%d/%m/%Y').date()
                break
            except:
                print('You are remaining with {} attempts'.format(2-count))
                count+=1
                print('Please enter in Correct Format')
                
               
                    
            
        self.dob=str(bday)
    def get_dob(self):
        return self.dob
    def set_balance(self):
        count=0
        while True:
            
            while True:
                if count>2:
                    sys.exit()
                try:
                    bal=eval(input('Enter the Opening Balance Amount greater than equal to Zero :: '))
                    break
                except:
                    if count==2:
                        print('All Attempts Exhausted\nSystem Exit')
                    else:
                        print('Please enter the value in integral form\nYou are left with {} Attempts'.format(2-count)) 
                    count+=1
            if bal>=0:
                self.balance=bal
                break
            else:
                if count==2:
                    print('All Attempts Exhausted\nSystem Exit')
                else:
                    print('enter the amount greater than zero\nYou are left with {} Attempts'.format(2-count))
                count+=1
    def get_balance(self):
        return self.balance
        
    def withdrl(self,amt,minimun_balance): ### withdrawl:
        

        if amt>self.balance:
            print('Insufficient balance , balance amount{}'.format(self.balance))
            sys.exit()
        elif self.balance-amt<minimun_balance:
            print('Can\'t perform transaction Minimum Balance criteria exploiting' )
            sys.exit()
        else:
            self.balance-=amt
            
            self.set_city()
            ct=self.get_city()
            print('-'*40)
            if ct == 'metro':
                print('Beware!!!\nYou are in metro city , For more than 3 Transactions extra charges are {}'.format(Account.METCHRG))
            else :
                print('Beware!!!\nYou are in non-metro city , For more than 5 Transactions extra charges are {}'.format(Account.NONMETCHRG))
            print('-'*40)
            if self.get_city() =='metro':
                self.withdrl_count_metro+=1
                if self.withdrl_count_metro>3:
                    print('Extra charges of',Account.METCHRG,'Rupees for',self.withdrl_count_metro,'th transaction in metro city')
                    self.balance-=Account.METCHRG
                    print(self.balance, 'is the remaining account balance after performing {} no\'s of Transaction in {} city'.format(self.withdrl_count_metro,ct))
                    self.set_tranlist('You were in {} city ,Debited amount {} , remaining balance {} on timestamp{} '.format(ct,amt,self.balance,datetime.datetime.now()))
                
                else:
                    print(self.balance, 'is the remaining account balance after performing {} no\'s of Transaction in {} city'.format(self.withdrl_count_metro,ct))
                    self.set_tranlist('You were in {} city ,Debited amount {} , remaining balance {} on timestamp{}'.format(ct,amt,self.balance,datetime.datetime.now()))
            else:
                self.withdrl_count_nonmetro+=1
                if self.withdrl_count_nonmetro>5:
                    self.balance-=Account.NONMETCHRG
                    print('Extra charges of',Account.NONMETCHRG,'Rupees for',self.withdrl_count,'th transaction in non-metro city')
                    print(self.balance, 'is the remaining account balance after performing {} no\'s of Transaction in {} city'.format(self.withdrl_count_nonmetro,ct))
                    self.set_tranlist('You were in {} city ,Debited amount {} , remaining balance {} on timestamp{}'.format(ct,amt,self.balance,datetime.datetime.now()))
                else:
                    print(self.balance, 'is the remaining account balance after performing {} no\'s of Transaction in {} city'.format(self.withdrl_count_nonmetro,ct))
                    self.set_tranlist('You were in {} city ,Debited amount {} , remaining balance {} on timestamp{}'.format(ct,amt,self.balance,datetime.datetime.now()))
            
    def deposit(self,amt):                      ## credit amount
        self.balance+=amt
        self.set_tranlist('Amount Credited {} updated balance {} on timestamp {}'.format(amt,self.balance,datetime.datetime.now()))
        print('Your Account credited with {} rupees updated balance {}'.format(amt,self.balance))
    def ministmt(self):                     # all individual transaction data
        print('*'*30)
        print('Your account number ending with xxxx xxxx {}'.format(self.accnum.strip()[-4:]))
        l=len(self.get_tranlist())
        if l>=5:
            print('Your Last 5 transaction are ::')
            for i in self.get_tranlist()[-5:]:
                print(i)
        else:
            print('You have only performed {} transactions with deatils as follows :: '.format(l-1))
            for i in self.get_tranlist():
                print(i)
    @abstractmethod
    def get_accdtl(self):
        pass
class Saving(Account):              ## Savings Account
    MIN_BALANCE=0
    def __init__(self):
        super().__init__()
        # print(id(self.name))
        
    
    def get_accdtl(self):
        print('Account Holder Name:{}'.format(self.name))
        print('Savings Account Number:{}'.format(self.accnum))
        print('Account holder Date of birth:{}'.format(self.dob))
        print('Your Saving account balance is {}'.format(self.balance))

class Current(Account):                 ##current account
    MIN_BALANCE=-10000
    def __init__(self):
        super().__init__()
        # print(id(self.get_tranlist()))
        # print(id(self.get_name))
        
    def get_accdtl(self):
        
        print('Brand Name:{} since {}'.format(self.name,self.dob))
        print('Current Account Number:{}'.format(self.accnum))
        print('Your Current Account balance is {}'.format(self.balance))
    
print(' '*30,end='')
print('Considering Yourself as a Banker ,Perform the operations based on customer requirments \n')
print(' '*50,end='')
print('Hello!!!, Welcome to {}.'.format(Account.BANKNAME))
print('-'*5,'please choose the desired option','-'*5,'\n')
inp = ''
count=0

while True:
    
    while inp not in ['1','2','3','0']:
        if count > 2:
            sys.exit('All Attempts exhausted\nSystem Exit')
        if count==0:
            print('You are provided with {} attempts to start Application\n'.format(3) )
        else:
            print('You are left with {} attempts\nChoose the correct option\n'.format(3-count))
        count+=1
        inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress- "3" to check Customers\nPress-"0" to Exit\n')
        
    if inp =='1':                      #Creating customer object
        count=0
        l_count=0
        while True:
            print('*'*30)
            ip=input('Press ->"1" for SAVINGS ACCOUNT\nPress ->"2" for CURRENT ACCOUNT\npress ->"3" for Main Menu\n')
            if ip=='1':
                l_count=0
                s=Saving()
                Util.setter(s,'Savings')
                
            elif ip=='2':
                l_count=0
                c=Current()
                Util.setter(c,'Current')
                
            elif ip =='3':
                l_count=0
                print('*'*40)
                print('you choose to go back to the main menu')
                inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress-"0" to Exit\nPress-"3" to check Customers\n')
                print('*'*40)
                while inp not in ['1','2','0','3']:
                    if l_count>=2:
                        sys.exit('You entered the wrong input\nSystem Exit')
                    l_count+=1
                    print('You are left with {} attempts'.format(3-l_count))
                    inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress-"0" to Exit\nPress-"3" to check Customers\n')
                    
                break
            
            else:
                if l_count>1:
                    sys.exit('System Exit')
                l_count+=1
                print('*'*50)
                print('You entered the wrong input\nRemaining number of attempts left {}'.format (3-l_count))
                
                
    if inp=='2':
        having_account=Util.havingaccount()
        if not having_account:
            inp='1'
            continue
            
        else:
            print('*'*40)
            obj_ref,typ=having_account[0],having_account[1]
            count=0
            while True:
                trn = input('Hit -1 For Withdrawl\nHit -2 For Deposit\nHit -3 For Ministatement\nHit -4 For Account Details\nHit -5 For Available Balance\nHit -6 For MainMenu')
                while trn not in ['1','2','3','4','5','6'] and count<3:
                    print('You entered the wrong input')
                    count+=1
                    if count==3:
                        sys.exit()
                    trn = input('Hit -1 For Withdrawl\nHit -2 For Deposit\nHit -3 For Ministatement\nHit -4 For Account Details\nHit -5 For Available Balance\nHit -6 For MainMenu')
                if trn=='1':
                    print('*'*40)
                    count=0
                    amt=eval(input('enter the withdrawl amount :: '))
                    
                    if typ.strip().split()[0]=='Savings':
                        obj_ref.withdrl(amt,Saving.MIN_BALANCE)
                    else:
                        obj_ref.withdrl(amt,Current.MIN_BALANCE)
                    print('*'*40)
                elif trn=='2':
                    print('*'*40)
                    count=0
                    amt=eval(input('enter the amount to de deposited :: '))
                    obj_ref.deposit(amt)    
                    print('*'*40)
                elif trn =='3':
                    print('*'*40)
                    count=0
                    obj_ref.ministmt()
                    print('*'*40)
                elif trn =='4':
                    print('*'*40)
                    count=0
                    obj_ref.get_accdtl()
                    print('*'*40)
                elif trn =='6':
                    print('*'*40)
                    count=0
                    print('You choose to go to Main Menu')
                    inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress- "3" to check Customers\nPress-"0" to Exit\n')
                    while inp not in ['1','2','0','3']:
                        if  count>=2:
                                sys.exit('You entered the wrong input\nSystem Exit')
                        count+=1
                        print('*'*40)
                        print('You are left with {} attempts'.format(3-l_count))
                        inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress- "3" to check Customers\nPress-"0" to Exit\n')
                    break
                elif trn == '5':
                    count=0
                    print(obj_ref.get_balance())
                else:
                    count+=1
                    print('*'*50)
                    print('You entered the wrong input\nRemaining number of attempts left {}'.format (3-count))
                    print('*'*50)
                    if count==3:
                        sys.exit('System Exit')    
    if inp=='0':
        count=0
        print('Thankyou! you choose to exit')
        sys.exit('System Exit Please visit again')
        
    if inp=='3':
        print('*'*30)
        print('For accessing list of customers\nPlease validate yourself\nUsing any one of your customer login credential\'s')
        having_account=Util.havingaccount()
        if not having_account:
            inp='1'
            continue
        else:
            count=0
            print('#'*30)
            for dict in Account.cust_list:
                for key in dict:
                    print(key,dict[key][:5])
            print('#'*30)
            print('*'*40)
            print('Please choose further actions to be taken')
            inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress-"0" to Exit\nPress- "3" to check Customers\n')
            while inp not in ['1','2','0','3']:
                inp = input('Press-"1" to Open the bank account\npress-"2" to perform some transaction\nPress-"0" to Exit\nPress- "3" to check Customers\n')
