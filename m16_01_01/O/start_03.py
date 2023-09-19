class Discount:
    def apply(self, order_type, price):
        if order_type == "summer":
            return price * 0.9
        elif order_type == "black_friday":
            return price * 0.7
