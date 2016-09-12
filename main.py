from bicycle_industry import Bicycle, Bicycle_store, Customer

def main(): 
    
#add data to name the bicycles
    ladies = Bicycle(name = "Trek Chelsea 9", weight = 4, cost = 150000)
    urban = Bicycle(name = "Breezer Uptown", weight = 3.5, cost = 20000)
    hipster = Bicycle(name = "Felt York", weight = 5, cost = 70000)
    retro = Bicycle(name = "Brooklyn Bicycle Co. Wythe", weight = 7, cost = 99000)
    ebike = Bicycle(name = "Faraday Porteur", weight = 4, cost = 25000)
    city = Bicycle(name = "Marin Fairfax SC6 DLX", weight = 7, cost = 17000)
    
#instances of bicycles in a list
    bicycles = [ladies, urban, hipster, retro, ebike, city]
    
#name store & add its margin & its inventory
    shop = Bicycle_store(name = "Holler4aBike!")
    shop.markup = 20
    shop.inventory = {'ladies': 10, 'urban': 30, 'hipster': 5, 'retro': 5, 'ebike': 10, 'city': 30}
    
#set the retail price for the bicycles in the store        
    for bicycle in bicycles:
        price = shop.set_retail_price(bicycle)

#add data for: customer name, budget
    holly = Customer(name = "Holly Marshall", budget = 200)
    moya = Customer(name = "Moya Vandeleur", budget = 500)
    caitlin = Customer(name = "Caitlin Cooper", budget = 1000)

#instances of customers in a list
    customers = [holly, moya, caitlin]

#print customers and list of bikes that they can afford, given their budget
    for customer in customers: 
        for bicycle in bicycles: 
            shop.create_suggestion_list(bicycle, customer)
        shop.make_suggestions(customer)
    

#print the shop's initial inventory
    shop.current_inventory()
		
if __name__ == "__main__": 
    main()