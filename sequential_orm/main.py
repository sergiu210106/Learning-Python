import os 
from dotenv import load_dotenv, find_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select, text

load_dotenv(find_dotenv())

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not found in .env file")

engine = create_engine(DATABASE_URL)

class Item (SQLModel, table = True):
    id: int = Field (default = None, primary_key = True)
    name: str = Field (index = True)
    description: str | None = None
    
    def __str__(self):
        return f"Item: name = {self.name}, id = {self.id}, description = {self.description}\n"
    
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_item(name : str, description : str | None = None):
    """Create a new item and return it"""
    with Session(engine) as session:
        item = Item(name = name, description = description)
        session.add(item)
        session.commit()
        session.refresh(item)
        
        print (f"created {item}")
        return item

if __name__ == '__main__':
    create_db_and_tables()
    
    # Electronics
    create_item("Smartphone", "iPhone 15 Pro")
    create_item("Laptop", "Dell XPS 15")
    create_item("Headphones", "Sony WH-1000XM5")
    create_item("Mouse")  # Testing the optional description

    # Groceries
    create_item("Milk", "Whole Milk, 1 Gallon")
    create_item("Bread", "Sourdough loaf")
    create_item("Eggs", "Free-range, 12 count")
    create_item("Coffee Beans", "Arabic, Dark Roast")

    # Office Supplies
    create_item("Notebook", "A4, Ruled")
    create_item("Pen", "Black ink, Ballpoint")
    create_item("Stapler")
    create_item("Monitor Stand", "Adjustable aluminum")

    # Miscellaneous
    create_item("Gaming Chair", "Ergonomic, Red")
    create_item("Desk Lamp", "LED, Dimmable")
    
    try:
        with engine.connect() as connection:
            statement = text("SELECT * FROM item")
            results = connection.execute(statement)
            for row in results:
                print(f"ID: {row.id}, Name: {row.name}, Desc: {row.description}")
                
    except Exception as e:
        print(f"Query failed: {e}")
        
    SQLModel.metadata.drop_all(engine)


