from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()




from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime




class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    
class Bid(Base):
    __tablename__="bid"
    id=Column(Integer,primary_key=True)
    price=Column(Float,nullable=False)



class UserAuctionItem(Base):
    __tablename__="user_auction_item"
    
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)    
    item_id=Column(Integer,ForeignKey('items.id'),nullable=False)
    
class UserBidItems(Base):   
    """docstring for UserBidItems"""
    __tablename__="user_bid_items"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)  
    user_auction_item_id=Column(Integer,ForeignKey('user_auction_item.id'),nullable=False)
    bid_id=Column(Integer,ForeignKey('bid.id'),nullable=False)
        
    
Base.metadata.create_all(engine)



if __name__ == '__main__':
    winfred=User(username="winfred",password="123456")
    session.add(winfred)
    baseball=Item(name="baseball",description="a baseball")
    session.add(baseball)
    session.commit()    
    winfred_auction_baseball=UserAuctionItem(user_id=winfred.id,item_id=baseball.id)
    session.add(winfred_auction_baseball)
    
    jeff=User(username="jeff",password="123456")
    session.add(jeff)
    Jack=User(username="jack",password="123456")
    session.add(Jack)
    jeff_bid=Bid(price=120.5)
    session.add(jeff_bid)
    jack_bid=Bid(price=140.4)
    session.add(jack_bid)
    session.commit()    
    jeff_bid_baseball=UserBidItems(user_id=jeff.id,user_auction_item_id=winfred_auction_baseball.id,bid_id=jeff_bid.id)
    jack_bid_baseball=UserBidItems(user_id=Jack.id,user_auction_item_id=winfred_auction_baseball.id,bid_id=jack_bid.id)
    
    session.add(jeff_bid_baseball)
    session.add(jack_bid_baseball)
    
    session.commit() 
    
    
    
    