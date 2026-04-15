from bot.orders import place_order
from bot.validators import validate_order

def get_valid_input(prompt, valid_options):
    while True:
        value = input(prompt).upper()
        if value in valid_options:
            return value
        print(f"❌ Invalid input! Choose from {valid_options}")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def get_user_input():
    print("\n" + "="*40)
    print("🚀 Binance Futures Trading Bot")
    print("="*40)

    symbol = input("🔹 Enter Symbol (e.g., BTCUSDT): ").upper()
    side = get_valid_input("🔹 Enter Side (BUY/SELL): ", ["BUY", "SELL"])
    order_type = get_valid_input("🔹 Order Type (MARKET/LIMIT): ", ["MARKET", "LIMIT"])
    quantity = get_float_input("🔹 Enter Quantity: ")

    price = None
    if order_type == "LIMIT":
        price = get_float_input("🔹 Enter Price: ")

    return symbol, side, order_type, quantity, price


def main():
    try:
        symbol, side, order_type, quantity, price = get_user_input()

        validate_order(symbol, side, order_type, quantity, price)

        print("\n📌 Order Summary:")
        print("-" * 30)
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")
        print(f"Price       : {price}")
        print("-" * 30)

        order = place_order(symbol, side, order_type, quantity, price)

        print("\n✅ Order Result:")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")

    except Exception as e:
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()