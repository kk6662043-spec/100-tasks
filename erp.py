class ERPSystem:
    def __init__(self):
        self.employees = []
        self.products = []
        self.sales = []

    # Employee Module
    def add_employee(self, name):
        self.employees.append(name)
        print(f"Employee '{name}' added.")

    # Inventory Module
    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})
        print(f"Product '{name}' added.")

    # Sales Module
    def create_sale(self, product_name, quantity):
        for product in self.products:
            if product["name"] == product_name:
                total = product["price"] * quantity
                self.sales.append({
                    "product": product_name,
                    "quantity": quantity,
                    "total": total
                })
                print(f"Sale created. Total: ₹{total}")
                return
        print("Product not found!")

    # Reports
    def show_report(self):
        print("\n--- ERP REPORT ---")

        print("\nEmployees:")
        for emp in self.employees:
            print("-", emp)

        print("\nProducts:")
        for product in self.products:
            print(f"- {product['name']} : ₹{product['price']}")

        print("\nSales:")
        for sale in self.sales:
            print(
                f"- {sale['product']} | Qty: {sale['quantity']} | Total: ₹{sale['total']}"
            )


# Main Program
erp = ERPSystem()

erp.add_employee("Kavin")
erp.add_employee("Rahul")

erp.add_product("Laptop", 50000)
erp.add_product("Mouse", 500)

erp.create_sale("Laptop", 2)
erp.create_sale("Mouse", 5)

erp.show_report()