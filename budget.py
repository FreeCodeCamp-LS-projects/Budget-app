#class Category:
#def create_spend_chart(categories):
class Category:


    def __init__(self, category):
        self.category = category
        self.total = 0
        self.ledger = []

    def __str__(self):
        show = ""
        title = self.category.center(30, '*')
        show = title + '\n'
        for a in self.ledger:
            lista = list(a.values())
            front = lista[1]
            front = '{:<30}'.format(front)
            front = front[:23]
            back = lista[0]
            aa = float(back)
            aa = "{:.2f}".format(aa)
            #aa = format(aa, '.2f')
            bb = '{:>7}'.format(aa,'.2f')
            i = front + bb
            show += i + '\n'
        show += 'Total: ' + "{:.2f}".format(self.total)
        return show

    def deposit(self, amount, description = ""):
        self.total += amount
        self.ledger.append({"amount" : amount, "description" : description})

    def withdraw(self, amount, description=""):
      if self.total >= amount:
        if self.check_funds:
            self.total -= amount
            self.ledger.append({"amount" : -amount, "description" : description})    
            return True
      else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, temporal):
      if self.total >= amount:
        if self.check_funds:
            self.total -= amount
            self.ledger.append({"amount" : -amount, "description" : "Transfer to " + temporal.category})
            temporal.total += amount
            temporal.ledger.append({"amount" : amount, "description" : "Transfer from " + self.category})
            return True
      else:
            return False

    def check_funds(self, amount):
        if self.total >= amount:
            return True
        elif self.total < amount:
            return False

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    total_expenses = 0
    amounts = {}

    for categ in categories:
        amount_spent = 0
        for transaction in categ.ledger:                    #runs thru the ledger
            if transaction['amount'] < 0:                   #compares the value of amount < 0
                amount_spent += -(transaction['amount'])    #convert the value to positive
        amounts[categ] = amount_spent                       #actualiza el dictionary amounts (key = categ) 
        total_expenses += amount_spent                      #sum the values (if found)

    percent = {}
    for categ in categories:
        temp_per = (amounts[categ]/total_expenses)*100
        temp_per = int(temp_per)
        percent[categ] = temp_per                           #calculate the porcentage por categoria

                                                            #graph
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for categ in categories:
            if percent[categ] >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    dashes_len = len(categories)*3 + 1
    dash = "-"
    res += f"    {dash*dashes_len}\n"

    max_len = len(categories[0].category)
    for categ in categories:
        if len(categ.category) > max_len:
            max_len = len(categ.category)
    i = 0
    for x in range(max_len):
        res += "     "
        for categ in categories:
            try:
                if categ.category[i]:
                    res += categ.category[i] + "  "
                else:
                    res += " "
            except:
                res += "   "
        if x != max_len-1:
            res += "\n"
        i += 1
    return res