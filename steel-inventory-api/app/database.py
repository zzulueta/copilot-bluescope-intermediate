from typing import List, Optional
from app.models import SteelProduct
from datetime import datetime

# Simple in-memory database for the lab
# In production, this would use SQLAlchemy with a real database
class InMemoryDB:
    def __init__(self):
        self.products: List[SteelProduct] = []
        self._next_id = 1
        self._seed_data()
    
    def _seed_data(self):
        """Add some initial data"""
        sample_products = [
            SteelProduct(
                id=1,
                product_code="STL-001",
                grade="A36",
                shape="sheet",
                length_mm=2400,
                width_mm=1200,
                thickness_mm=6.0,
                quantity=150,
                location="Warehouse-A",
                last_updated=datetime.now()
            ),
            SteelProduct(
                id=2,
                product_code="STL-002",
                grade="304",
                shape="coil",
                length_mm=5000,
                width_mm=1500,
                thickness_mm=3.0,
                quantity=75,
                location="Warehouse-B",
                last_updated=datetime.now()
            ),
        ]
        self.products = sample_products
        self._next_id = 3
    
    def get_all(self) -> List[SteelProduct]:
        return self.products
    
    def get_by_id(self, product_id: int) -> Optional[SteelProduct]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def create(self, product_data: dict) -> SteelProduct:
        # BUG: Missing validation for duplicate product codes
        product = SteelProduct(
            id=self._next_id,
            **product_data,
            last_updated=datetime.now()
        )
        self.products.append(product)
        self._next_id += 1
        return product
    
    def update(self, product_id: int, update_data: dict) -> Optional[SteelProduct]:
        product = self.get_by_id(product_id)
        if product:
            # BUG: Not updating last_updated timestamp
            for key, value in update_data.items():
                if value is not None:
                    setattr(product, key, value)
            return product
        return None
    
    def delete(self, product_id: int) -> bool:
        # BUG: Missing proper deletion logic
        product = self.get_by_id(product_id)
        if product:
            self.products.remove(product)
            return True
        return False

# Global database instance
db = InMemoryDB()
