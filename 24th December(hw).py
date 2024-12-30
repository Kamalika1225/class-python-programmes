class Calculator:
    def calculate_final_price(self, base_price, discount_percentage=0, tax_percentage=0):
        if base_price < 0 or discount_percentage < 0 or tax_percentage < 0:
            raise ValueError("Negative values are not allowed for base_price, discount_percentage, or tax_percentage.")
        discount_amount = base_price * (discount_percentage / 100)
        discounted_price = base_price - discount_amount
        tax_amount = discounted_price * (tax_percentage / 100)
        final_price = discounted_price + tax_amount
        
        return round(final_price, 2)

calc = Calculator()

try:
    final_price1 = calc.calculate_final_price(100, 10, 5)
    print(f"Final price for product 1: ${final_price1}")  
except ValueError as e:
    print(e)

