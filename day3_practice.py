def greet (name : str) -> None:
    print("Hello, ", name)




greet("Rocky")


def total_spend(spends : list [float]) -> float:
     total = 0
     for amount in spends:
          total += amount

     return total 



print(total_spend([100.0, 200.0, 50.5])) 


class Campaign:
  def __init__(self,name: str, spend : float, clicks:int, conversions :int) -> None:
      self.name = name
      self.spend = spend
      self.clicks = clicks
      self.conversions = conversions 

  def cpa(self) -> float:
   if self.conversions == 0 :
      raise ZeroDivisionError("no conversions")
   return self.spend / self.conversions

  def __repr__(self) -> str:
    return f"Campaign(name={self.name!r}, spend ={self.spend},clicks ={self.clicks}, conversions ={self.conversions})"

    
c1 = Campaign("Meta_Black_Friday", 1200.00, clicks=450, conversions=23)
c2 = Campaign("Google_Search_Q4", 2100.50, clicks=320, conversions=18)
c3 = Campaign("Meta_Lead_Gen", 800.00, clicks=200, conversions = 0 )

# Print each — should trigger __repr__
print(c1)
print(c2)
print(c3)

print(f"CPA c1: ${c1.cpa():.2f}")
print(f"CPA c2: ${c2.cpa():.2f}")

try:
    print(c3.cpa())
except ZeroDivisionError as e:
    print(f"Caught error: {e}")

# def info(self):
#     print (f'Campaign {self.name} spent ${self.spend}')


# c1 = Campaign("fb", 650.55)
# c2 = Campaign("Google", 1200.75)

# c1.info()
# c2.info()


# def average_spend(campaigns: list):
#     total = 0

#     for campaign in campaigns:
#         total += campaign.spend

#     if len(campaigns) == 0:
#         return 0
    
#     return total / len(campaigns)

# campaigns = [ c1,c2]

# print(f' average spends is {average_spend(campaigns)}')