"""
Inventory & Sales Tracker
E-Commerce / Retail Management System
"""

from datetime import datetime
import json
from typing import Dict, List, Tuple, Set, Optional


class InventorySalesTracker:
    """
    A comprehensive inventory and sales tracking system using Python data structures.
    
    Data Structures Used:
    - Dictionary: Maps product IDs to product details
    - Tuple: Immutable product metadata (product_id, name, base_price)
    - List: Stores sales transaction history
    - Set: Tracks distinct product categories
    """
    
    def __init__(self):
        # Dictionary: product_id -> product_details
        self.inventory: Dict[str, dict] = {}
        
        # Set: distinct product categories
        self.categories: Set[str] = set()
        
        # List: sales transaction history
        self.transactions: List[dict] = []
        
        # Tuple: product metadata template (used for creating products)
        self.product_metadata_template: Tuple[str, str, float] = ("", "", 0.0)
    
    def add_product(self, product_id: str, name: str, category: str, 
                   price: float, stock: int, description: str = "") -> bool:
        """
        Add a new product to inventory.
        Prevents duplicate product IDs.
        
        Args:
            product_id: Unique product identifier
            name: Product name
            category: Product category
            price: Product price
            stock: Initial stock quantity
            description: Optional product description
            
        Returns:
            bool: True if product added successfully, False if duplicate
        """
        # Check for duplicate product ID
        if product_id in self.inventory:
            print(f"❌ Error: Product ID '{product_id}' already exists!")
            return False
        
        # Create product metadata as tuple
        metadata: Tuple[str, str, float] = (product_id, name, price)
        
        # Store product details in dictionary
        self.inventory[product_id] = {
            "product_id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
            "description": description,
            "metadata": metadata,  # Store immutable metadata tuple
            "created_at": datetime.now().isoformat()
        }
        
        # Add category to set
        self.categories.add(category)
        
        print(f"✅ Product '{name}' added successfully!")
        return True
    
    def update_stock(self, product_id: str, quantity_change: int) -> bool:
        """
        Update stock quantity for a product.
        Positive quantity_change adds stock, negative reduces stock.
        
        Args:
            product_id: Product identifier
            quantity_change: Amount to change stock by (can be negative)
            
        Returns:
            bool: True if stock updated successfully
        """
        if product_id not in self.inventory:
            print(f"❌ Error: Product ID '{product_id}' not found!")
            return False
        
        product = self.inventory[product_id]
        new_stock = product["stock"] + quantity_change
        
        if new_stock < 0:
            print(f"❌ Error: Insufficient stock! Current stock: {product['stock']}")
            return False
        
        product["stock"] = new_stock
        print(f"✅ Stock updated for '{product['name']}'. New stock: {new_stock}")
        return True
    
    def record_sale(self, product_id: str, quantity: int, 
                   customer_email: str = "") -> bool:
        """
        Record a sales transaction.
        
        Args:
            product_id: Product identifier
            quantity: Quantity sold
            customer_email: Optional customer email
            
        Returns:
            bool: True if sale recorded successfully
        """
        if product_id not in self.inventory:
            print(f"❌ Error: Product ID '{product_id}' not found!")
            return False
        
        product = self.inventory[product_id]
        
        # Check stock availability
        if product["stock"] < quantity:
            print(f"❌ Error: Insufficient stock! Available: {product['stock']}, Requested: {quantity}")
            return False
        
        # Update stock
        product["stock"] -= quantity
        
        # Create transaction record
        transaction = {
            "transaction_id": f"TXN-{len(self.transactions) + 1:04d}",
            "product_id": product_id,
            "product_name": product["name"],
            "quantity": quantity,
            "unit_price": product["price"],
            "total_amount": product["price"] * quantity,
            "timestamp": datetime.now().isoformat(),
            "customer_email": customer_email
        }
        
        # Add to transactions list
        self.transactions.append(transaction)
        
        print(f"✅ Sale recorded! Transaction ID: {transaction['transaction_id']}")
        print(f"   Product: {product['name']}, Quantity: {quantity}, Total: ${transaction['total_amount']:.2f}")
        return True
    
    def get_product_details(self, product_id: str) -> Optional[dict]:
        """
        Get detailed information about a product.
        
        Args:
            product_id: Product identifier
            
        Returns:
            dict: Product details or None if not found
        """
        return self.inventory.get(product_id)
    
    def get_product_metadata(self, product_id: str) -> Optional[Tuple[str, str, float]]:
        """
        Get immutable metadata tuple for a product.
        
        Args:
            product_id: Product identifier
            
        Returns:
            Tuple: (product_id, name, price) or None if not found
        """
        product = self.inventory.get(product_id)
        if product:
            return product.get("metadata")
        return None
    
    def get_products_by_category(self, category: str) -> List[dict]:
        """
        Get all products in a specific category.
        
        Args:
            category: Category name
            
        Returns:
            List[dict]: List of products in the category
        """
        return [product for product in self.inventory.values() 
                if product["category"].lower() == category.lower()]
    
    def get_all_categories(self) -> Set[str]:
        """
        Get all distinct product categories.
        
        Returns:
            Set[str]: Set of all categories
        """
        return self.categories.copy()
    
    def get_low_stock_products(self, threshold: int = 5) -> List[dict]:
        """
        Get products with stock below threshold.
        
        Args:
            threshold: Stock threshold
            
        Returns:
            List[dict]: Products with low stock
        """
        return [product for product in self.inventory.values() 
                if product["stock"] <= threshold]
    
    def get_daily_sales_report(self, date: str = None) -> dict:
        """
        Generate a sales report for a specific date.
        If no date provided, uses today's date.
        
        Args:
            date: Date string in YYYY-MM-DD format
            
        Returns:
            dict: Sales summary for the day
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        daily_transactions = [
            t for t in self.transactions 
            if t["timestamp"].startswith(date)
        ]
        
        total_sales = sum(t["total_amount"] for t in daily_transactions)
        total_items = sum(t["quantity"] for t in daily_transactions)
        
        return {
            "date": date,
            "transaction_count": len(daily_transactions),
            "total_items_sold": total_items,
            "total_sales_amount": total_sales,
            "transactions": daily_transactions
        }
    
    def get_inventory_summary(self) -> dict:
        """
        Get a summary of the entire inventory.
        
        Returns:
            dict: Inventory summary statistics
        """
        total_products = len(self.inventory)
        total_stock = sum(p["stock"] for p in self.inventory.values())
        total_value = sum(p["stock"] * p["price"] for p in self.inventory.values())
        
        return {
            "total_products": total_products,
            "total_categories": len(self.categories),
            "total_stock_items": total_stock,
            "total_inventory_value": total_value,
            "categories": sorted(self.categories)
        }
    
    def get_transaction_history(self, limit: int = None) -> List[dict]:
        """
        Get transaction history with optional limit.
        
        Args:
            limit: Maximum number of transactions to return
            
        Returns:
            List[dict]: List of transactions (most recent first)
        """
        recent_transactions = self.transactions[::-1]  # Reverse order
        if limit:
            return recent_transactions[:limit]
        return recent_transactions
    
    def delete_product(self, product_id: str) -> bool:
        """
        Delete a product from inventory.
        
        Args:
            product_id: Product identifier
            
        Returns:
            bool: True if product deleted successfully
        """
        if product_id not in self.inventory:
            print(f"❌ Error: Product ID '{product_id}' not found!")
            return False
        
        product = self.inventory[product_id]
        category = product["category"]
        
        # Remove product
        del self.inventory[product_id]
        
        # Remove category if no more products in it
        if not any(p["category"] == category for p in self.inventory.values()):
            self.categories.discard(category)
        
        print(f"✅ Product '{product['name']}' deleted successfully!")
        return True
    
    def search_products(self, search_term: str) -> List[dict]:
        """
        Search for products by name or description.
        
        Args:
            search_term: Search query
            
        Returns:
            List[dict]: Matching products
        """
        search_term = search_term.lower()
        matches = []
        
        for product in self.inventory.values():
            if (search_term in product["name"].lower() or 
                search_term in product["description"].lower() or
                search_term in product["product_id"].lower()):
                matches.append(product)
        
        return matches
    
    def export_data(self, filename: str = "inventory_data.json") -> bool:
        """
        Export inventory and transaction data to JSON file.
        
        Args:
            filename: Output filename
            
        Returns:
            bool: True if export successful
        """
        try:
            data = {
                "inventory": self.inventory,
                "categories": list(self.categories),
                "transactions": self.transactions,
                "export_date": datetime.now().isoformat()
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"✅ Data exported to '{filename}'")
            return True
        except Exception as e:
            print(f"❌ Error exporting data: {e}")
            return False
    
    def import_data(self, filename: str = "inventory_data.json") -> bool:
        """
        Import inventory and transaction data from JSON file.
        
        Args:
            filename: Input filename
            
        Returns:
            bool: True if import successful
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.inventory = data.get("inventory", {})
            self.categories = set(data.get("categories", []))
            self.transactions = data.get("transactions", [])
            
            print(f"✅ Data imported from '{filename}'")
            return True
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found!")
            return False
        except Exception as e:
            print(f"❌ Error importing data: {e}")
            return False


def print_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("📦 INVENTORY & SALES TRACKER")
    print("="*50)
    print("1. Add Product")
    print("2. Update Stock")
    print("3. Record Sale")
    print("4. View Product Details")
    print("5. View All Products")
    print("6. View Categories")
    print("7. View Low Stock Items")
    print("8. Daily Sales Report")
    print("9. Inventory Summary")
    print("10. Search Products")
    print("11. Delete Product")
    print("12. Export Data")
    print("13. Import Data")
    print("14. Exit")
    print("="*50)


def main():
    """Main program loop."""
    tracker = InventorySalesTracker()
    
    # Add some sample products
    sample_products = [
        ("P001", "Smartphone X", "Electronics", 699.99, 50, "Latest flagship smartphone"),
        ("P002", "Laptop Pro", "Electronics", 1299.99, 30, "Professional laptop for developers"),
        ("P003", "Running Shoes", "Sports", 89.99, 100, "Comfortable running shoes"),
        ("P004", "Coffee Maker", "Home", 49.99, 25, "Automatic coffee maker"),
        ("P005", "Book: Python Guide", "Books", 39.99, 75, "Complete Python programming guide"),
    ]
    
    for pid, name, cat, price, stock, desc in sample_products:
        tracker.add_product(pid, name, cat, price, stock, desc)
    
    # Record some sample sales
    tracker.record_sale("P001", 2, "customer1@email.com")
    tracker.record_sale("P003", 1, "customer2@email.com")
    tracker.record_sale("P001", 1, "customer3@email.com")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-14): ").strip()
        
        if choice == '1':
            print("\n--- Add Product ---")
            pid = input("Product ID: ").strip()
            name = input("Product Name: ").strip()
            category = input("Category: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
                description = input("Description (optional): ").strip()
                tracker.add_product(pid, name, category, price, stock, description)
            except ValueError:
                print("❌ Invalid input! Price must be a number and stock must be an integer.")
        
        elif choice == '2':
            print("\n--- Update Stock ---")
            pid = input("Product ID: ").strip()
            try:
                change = int(input("Stock change (+ for add, - for remove): "))
                tracker.update_stock(pid, change)
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
        
        elif choice == '3':
            print("\n--- Record Sale ---")
            pid = input("Product ID: ").strip()
            try:
                qty = int(input("Quantity sold: "))
                email = input("Customer email (optional): ").strip()
                tracker.record_sale(pid, qty, email)
            except ValueError:
                print("❌ Invalid input! Quantity must be a number.")
        
        elif choice == '4':
            print("\n--- Product Details ---")
            pid = input("Product ID: ").strip()
            details = tracker.get_product_details(pid)
            if details:
                print("\nProduct Details:")
                for key, value in details.items():
                    if key != "metadata":  # Skip metadata tuple for cleaner display
                        print(f"  {key}: {value}")
            else:
                print("❌ Product not found!")
        
        elif choice == '5':
            print("\n--- All Products ---")
            if tracker.inventory:
                print(f"\nTotal Products: {len(tracker.inventory)}")
                for pid, product in tracker.inventory.items():
                    print(f"\n  ID: {pid}")
                    print(f"  Name: {product['name']}")
                    print(f"  Category: {product['category']}")
                    print(f"  Price: ${product['price']:.2f}")
                    print(f"  Stock: {product['stock']}")
                    print("-" * 30)
            else:
                print("📭 No products in inventory.")
        
        elif choice == '6':
            print("\n--- Categories ---")
            categories = tracker.get_all_categories()
            if categories:
                print(f"\nTotal Categories: {len(categories)}")
                for idx, cat in enumerate(sorted(categories), 1):
                    print(f"  {idx}. {cat}")
                    products = tracker.get_products_by_category(cat)
                    print(f"     Products in category: {len(products)}")
            else:
                print("📭 No categories available.")
        
        elif choice == '7':
            print("\n--- Low Stock Items ---")
            threshold = input("Enter threshold (default 5): ").strip()
            try:
                threshold = int(threshold) if threshold else 5
            except ValueError:
                threshold = 5
                print("⚠️  Invalid input. Using default threshold of 5.")
            
            low_stock = tracker.get_low_stock_products(threshold)
            if low_stock:
                print(f"\nProducts with stock ≤ {threshold}:")
                for product in low_stock:
                    print(f"  {product['name']}: {product['stock']} units remaining")
            else:
                print(f"✅ All products have stock above {threshold}.")
        
        elif choice == '8':
            print("\n--- Daily Sales Report ---")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date:
                date = None
            report = tracker.get_daily_sales_report(date)
            print(f"\n📊 Sales Report for {report['date']}:")
            print(f"  Transactions: {report['transaction_count']}")
            print(f"  Items Sold: {report['total_items_sold']}")
            print(f"  Total Sales: ${report['total_sales_amount']:.2f}")
            if report['transactions']:
                print("\n  Transaction Details:")
                for txn in report['transactions']:
                    print(f"    {txn['transaction_id']}: {txn['product_name']} x{txn['quantity']} = ${txn['total_amount']:.2f}")
        
        elif choice == '9':
            print("\n--- Inventory Summary ---")
            summary = tracker.get_inventory_summary()
            print(f"  Total Products: {summary['total_products']}")
            print(f"  Total Categories: {summary['total_categories']}")
            print(f"  Total Stock Items: {summary['total_stock_items']}")
            print(f"  Total Inventory Value: ${summary['total_inventory_value']:.2f}")
            print(f"  Categories: {', '.join(summary['categories'])}")
        
        elif choice == '10':
            print("\n--- Search Products ---")
            search = input("Enter search term: ").strip()
            results = tracker.search_products(search)
            if results:
                print(f"\nFound {len(results)} product(s):")
                for product in results:
                    print(f"  {product['product_id']}: {product['name']} (${product['price']:.2f}) - Stock: {product['stock']}")
            else:
                print("❌ No matching products found.")
        
        elif choice == '11':
            print("\n--- Delete Product ---")
            pid = input("Product ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete product '{pid}'? (y/n): ").strip().lower()
            if confirm == 'y':
                tracker.delete_product(pid)
            else:
                print("Deletion cancelled.")
        
        elif choice == '12':
            print("\n--- Export Data ---")
            filename = input("Export filename (default: inventory_data.json): ").strip()
            if not filename:
                filename = "inventory_data.json"
            tracker.export_data(filename)
        
        elif choice == '13':
            print("\n--- Import Data ---")
            filename = input("Import filename (default: inventory_data.json): ").strip()
            if not filename:
                filename = "inventory_data.json"
            tracker.import_data(filename)
        
        elif choice == '14':
            print("\n👋 Thank you for using Inventory & Sales Tracker!")
            break
        
        else:
            print("❌ Invalid choice! Please select a valid option (1-14).")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
