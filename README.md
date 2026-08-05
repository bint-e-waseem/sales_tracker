# sales_tracker
```markdown
# 📦 Inventory & Sales Tracker

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive inventory and sales management system built in Python, demonstrating practical applications of fundamental data structures for retail and e-commerce operations.

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Data Structures Used](#-data-structures-used)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

The Inventory & Sales Tracker is a robust command-line application designed to manage retail operations efficiently. It provides a complete solution for product management, stock control, and sales tracking, making it ideal for small to medium-sized businesses transitioning from manual to digital inventory management.

### Key Highlights
- **Zero Dependencies**: Built entirely with Python's standard library
- **Data-Driven**: Leverages Python's built-in data structures for optimal performance
- **User-Friendly**: Interactive CLI with intuitive menu system
- **Production Ready**: Includes data persistence, error handling, and reporting features

## ✨ Features

### Inventory Management
- ✅ Add new products with unique IDs and metadata
- ✅ Update stock quantities with safety checks
- ✅ Delete products with category cleanup
- ✅ Search products by name, description, or ID
- ✅ View detailed product information
- ✅ Prevent duplicate product entries

### Sales Operations
- ✅ Record sales transactions with customer tracking
- ✅ Automatic stock deduction on sales
- ✅ Transaction history with unique IDs
- ✅ Customer email association for order tracking
- ✅ Real-time stock availability verification

### Reporting & Analytics
- 📊 Daily sales reports with transaction details
- 📊 Inventory summary with total value
- 📊 Category-based product filtering
- 📊 Low stock alerts with configurable thresholds
- 📊 Transaction history with date filtering

### Data Management
- 💾 Export inventory and sales data to JSON
- 📥 Import data from JSON files
- 🔄 Persistent storage between sessions
- 📅 Timestamp tracking for all operations

## 🗂️ Data Structures Used

This project demonstrates practical applications of Python's core data structures:

### 1. Dictionary (`dict`)
**Purpose**: Mapping product IDs to complete product details  
**Use Case**: Fast O(1) lookups, easy updates, and deletion  
**Example**:
```python
self.inventory = {
    "P001": {
        "name": "Smartphone X",
        "price": 699.99,
        "stock": 50,
        # ... more details
    }
}
```

### 2. Tuple (`tuple`)
**Purpose**: Immutable product metadata  
**Use Case**: Protecting core product information (ID, name, price) from accidental modification  
**Example**:
```python
metadata: Tuple[str, str, float] = ("P001", "Smartphone X", 699.99)
```

### 3. List (`list`)
**Purpose**: Chronological transaction history  
**Use Case**: Ordered storage, easy iteration, and slicing for reports  
**Example**:
```python
self.transactions = [
    {
        "transaction_id": "TXN-0001",
        "product": "Smartphone X",
        "quantity": 2,
        "timestamp": "2024-01-15T10:30:00"
    }
]
```

### 4. Set (`set`)
**Purpose**: Distinct product categories  
**Use Case**: Automatic deduplication, fast membership testing  
**Example**:
```python
self.categories = {"Electronics", "Sports", "Books", "Home"}
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Git (optional, for cloning)

### Clone Repository
```bash
git clone https://github.com/yourusername/inventory-sales-tracker.git
cd inventory-sales-tracker
```

### Quick Install
No additional packages required! The script uses only Python's standard library.

## 🎮 Quick Start

### Running the Application
```bash
python inventory_tracker.py
```

### First-Time Setup
The application comes pre-loaded with sample products for demonstration:
- Smartphone X (Electronics)
- Laptop Pro (Electronics)
- Running Shoes (Sports)
- Coffee Maker (Home)
- Book: Python Guide (Books)

### Basic Workflow
1. **Add Products**: Use option 1 to add new items
2. **Update Stock**: Option 2 to manage inventory levels
3. **Record Sales**: Option 3 to process transactions
4. **Generate Reports**: Options 7-9 for insights

## 📖 Usage Examples

### Adding a Product
```python
tracker = InventorySalesTracker()
tracker.add_product(
    product_id="P010",
    name="Wireless Headphones",
    category="Electronics",
    price=149.99,
    stock=30,
    description="Premium noise-cancelling headphones"
)
```

### Recording a Sale
```python
tracker.record_sale(
    product_id="P001",
    quantity=2,
    customer_email="customer@example.com"
)
```

### Generating Daily Report
```python
report = tracker.get_daily_sales_report("2024-01-15")
print(f"Total Sales: ${report['total_sales_amount']:.2f}")
```

### Checking Low Stock
```python
low_stock = tracker.get_low_stock_products(threshold=10)
for product in low_stock:
    print(f"{product['name']}: {product['stock']} units left")
```

## 📚 API Documentation

### Core Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `add_product()` | Adds a new product to inventory | `bool` |
| `update_stock()` | Updates product stock quantity | `bool` |
| `record_sale()` | Processes a sales transaction | `bool` |
| `get_product_details()` | Retrieves complete product information | `dict` |
| `get_products_by_category()` | Lists all products in a category | `List[dict]` |
| `get_low_stock_products()` | Identifies products below threshold | `List[dict]` |
| `get_daily_sales_report()` | Generates sales summary for a date | `dict` |
| `get_inventory_summary()` | Returns overall inventory statistics | `dict` |
| `export_data()` | Saves data to JSON file | `bool` |
| `import_data()` | Loads data from JSON file | `bool` |

### Data Models

#### Product Object
```python
{
    "product_id": str,
    "name": str,
    "category": str,
    "price": float,
    "stock": int,
    "description": str,
    "metadata": Tuple[str, str, float],
    "created_at": str  # ISO format timestamp
}
```

#### Transaction Object
```python
{
    "transaction_id": str,  # Format: TXN-XXXX
    "product_id": str,
    "product_name": str,
    "quantity": int,
    "unit_price": float,
    "total_amount": float,
    "timestamp": str,  # ISO format
    "customer_email": str
}
```

## 📁 Project Structure

```
inventory-sales-tracker/
├── inventory_tracker.py   # Main application
├── README.md              # Documentation
├── LICENSE                # MIT License
├── .gitignore            # Git ignore file
├── inventory_data.json   # Exported data (auto-generated)
└── examples/
    └── sample_usage.py   # Usage examples
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Write clear commit messages
- Test your changes thoroughly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Python Software Foundation for the excellent programming language
- Open source community for inspiration and best practices
- All contributors who help improve this project

## 📞 Support

For support, please:
- Open an issue in the GitHub repository
- Contact the maintainer via email
- Check the documentation for common issues

## 🔮 Future Roadmap

- [ ] GUI interface using Tkinter or PyQt
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] REST API for web integration
- [ ] Barcode scanning support
- [ ] Advanced analytics dashboard
- [ ] Multi-store support
- [ ] Email notifications for low stock
- [ ] PDF report generation

---

**Built with ❤️ using Python**

[Report Bug](https://github.com/yourusername/inventory-sales-tracker/issues) · [Request Feature](https://github.com/yourusername/inventory-sales-tracker/issues)
```
