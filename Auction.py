import time
import datetime

def res():
    l=[]
    secs=0
    def Winner(records):
        maxbid=0
        winner=""
        for bidder_name in records:
            bid_amt=records[bidder_name]
            if bid_amt>maxbid:
                maxbid=bid_amt
                winner=bidder_name
        return winner
 
# I AM TAKING 2 AUCTONS 

    current_auctions={1:'PAINTING',2:'HOUSE'}
    print("Currently ongoing auctions are ",[i for i in current_auctions.items()])

    # SELECTING AUCTION
    choose_auctions=int(input("Enter the Auction ID i.e. '1' for participating in PAINTING auction & '2' for participating in HOUSE auction: "))
    if choose_auctions==1:
        auction_name="PAINTING"
        admin=input("IF YOU ARE AN ADMIN ENTER 'Y' OTHERWISE 'N' : ")
        if admin in ["y","Y"]:
            initial_price=int(input("***ADMIN*** ENTER STARTING PRICE OF PAINTING AUCTION: "))

#   ************IMPORTANT(NO_OF_BIDDERS CAN BE GIVEN BY ADMIN)*****************************

            no_of_bidders=int(input("ADMIN,Enter no of bidders: "))
        else:
            initial_price=30 #if ADMIN DIDN'T GIVE STARTING PRICE INITIAL PRICE WILL BE 30 .
            no_of_bidders=int(input("Enter no of bidders: "))
            print("Item name is: Painting")
            print(f"Starting price is {int(initial_price)}")

#uidl=["uid1","uid2","uid3","uid4","uid5","uid6","uid7","uid8","uid9","uid10"]
        print(f"{auction_name} auction has started")
        now=datetime.datetime.now()
        print("STARTING TIME")
        print(now.strftime("%H:%M:%S"))
        bids={}
        while secs==0:
            for i in range(1,no_of_bidders+1):
                print(secs,end="\r")
                time.sleep(1)
                secs+=1
                print(f"BIDDER {i}")
                name=input("Enter your name: ")
        #UGenerating User ID i.e. UID
                print(f"Your user id is UID {i}")
                bid=int(input("Enter your bidding price: "))
                while bid<initial_price:
                    print(f"You cannot place a bid less than starting price of item i.e.{initial_price}")
                    bid=int(input("Enter your new bidding price: "))
                l.append([bid,name])
                bids[name]=bid
            break
        print(f"{auction_name} auction has ended")
        print(f"Winner of {auction_name} auction is: {Winner(bids)}")
        print(f"All the bidders for {auction_name} auction are {[g for g in bids.items()]}")
        print(f"Winner User Id is UID{l.index(max(l))+1}")
        
        
#print(bids)


    elif choose_auctions==2:
        auction_name="HOUSE"

        admin=input("IF YOU ARE AN ADMIN ENTER 'Y' OTHERWISE 'N': ")
        if admin in ["y","Y"]:
            initial_price=int(input("***ADMIN*** ENTER STARTING PRICE OF HOUSE AUCTION: "))

#   ************IMPORTANT(NO_OF_BIDDERS CAN BE GIVEN BY ADMIN)*****************************

            no_of_bidders=int(input("ADMIN,Enter no of bidders: "))
        else:
            initial_price=30 #if ADMIN DIDN'T GIVE STARTING PRICE INITIAL PRICE WILL BE 30 .
            no_of_bidders=int(input("Enter no of bidders: "))
            print("Item name is: painting")
            print(f"Starting price is {initial_price}")
            
#uidl=["uid1","uid2","uid3","uid4","uid5","uid6","uid7","uid8","uid9","uid10"]
        print(f"{auction_name} auction has started")
        now=datetime.datetime.now()
        print("STARTING TIME")
        print(now.strftime("%H:%M:%S"))
        bids={}
        while secs==0:
            for i in range(1,no_of_bidders+1):
                print(secs,end="\r")
                time.sleep(1)
                secs+=1
                print(f"BIDDER {i}")
                name=input("Enter your name: ")
                #Generating User ID i.e. UID
                print(f"Your user id is UID{i}")
                bid=int(input("Enter your bidding price: "))
                while bid<initial_price:
                    print(f"You cannot place a bid less than starting price of item i.e.{initial_price}")
                    bid=int(input("Enter your new bidding price: "))
                l.append([bid,name])
                bids[name]=bid
            break
        print(f"{auction_name} auction has ended"  )
        print(f"Winner of {auction_name} auction is: {Winner(bids)}")
        print(f"All the bidders participated in {auction_name} Auction and their bids for  are {[g for g in bids.items()]}")
        print(f"Winner User Id is UID{l.index(max(l))+1}")
    else:
        print("***  Please,Enter correct input i.e. either 1 or 2   ***")
        res()

    # print(bids)
    print("ENDING TIME")
    now=datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))

res()





