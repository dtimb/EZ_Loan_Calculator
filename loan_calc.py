def round_cents(num):

   return float(int(num*100 + .5000001))/100
  
def calculate_payment(amount, apr, num_months):

  
   monthly_interest_rate = apr/1200
   payment = float((amount*monthly_interest_rate)/(1-((1+monthly_interest_rate)**(-num_months))))
  
   return round_cents(payment)
  
def total_loan_cost(amount, apr, num_months):


   return round_cents(calculate_payment(amount, apr, num_months)*num_months)
  
def total_interest_paid(amount, apr, num_months):

  
   return round_cents(total_loan_cost(amount, apr, num_months)-amount)

def apply_payment(payment, balance, apr):
   interest = round_cents(float((balance*apr)/1200))
  
   
   if payment > balance:
      payment = round_cents(balance + interest)
  
   
   principal = round_cents(payment-interest)
   balance = round_cents(balance- payment + interest)
   payment = round_cents(interest+ principal)
       
   return (payment, principal, interest, balance)
