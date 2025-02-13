from fastapi.responses import JSONResponse
from models.order_model import Order

#if multiple user are using chatbot then this dic store all user items in this dict until complete order
#this dict will store sessionId: dict of food_item and their quantity (food_item: quantity)
inprogress_orders = {}

def new_order(parameters: dict, session_id: str):
    #Handling if user enter new order during existing order it clears existing cart
    if session_id in inprogress_orders:
        del inprogress_orders[session_id]
        res = "I've cleared your previous order. Let's start fresh! What would you like to order?"
    else:
        res = None
    return JSONResponse(content={
        'fulfillmentText': res
    })

def add_to_order(parameters: dict, session_id: str):
    """Handler for order.add - context: ongoing-order intent"""
    # print(f"Handling order.add with params: {parameters} for session: {session_id}")

    food_items = parameters.get('food-item')
    quantities = parameters.get('number')

    if len(food_items) != len(quantities):
        res = "Sorry I didn't understand. Can you please specify food items and quantities clearly?"
    else:
        food_dict = dict(zip(food_items, quantities))

        if session_id in inprogress_orders:
            cur_food_dict = inprogress_orders[session_id]
            cur_food_dict.update(food_dict)
            inprogress_orders[session_id] = cur_food_dict
        else:
            inprogress_orders[session_id] = food_dict

        order_str = get_string_from_food_dict(inprogress_orders[session_id])

        res = f"You have this food item(s) in your cart {order_str}. Do you need anything else?"
   
    return JSONResponse(content={
        "fulfillmentText": res
    })


def complete_order(parameters: dict, session_id: str):
    """Handler for order.complete - context: ongoing-order intent"""
    # print(f"Handling order.complete with params: {parameters} for session: {session_id}")
    
    if session_id not in inprogress_orders:
        res = "I’m having trouble finding your order. Apologies! Could you please place a new order?"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
      
        if order_id == -1:
            res = "Sorry, I couldn't process your order due to a backend error. Please place a new order again."
        else:
            order_total = Order.get_total_order_price(order_id)
            res = f"Awesome. We have placed your order. Here is your order id # {order_id}. Your order total is {order_total} Which you can pay at the time of delivery!"

        # delete the session_id from inprogress_orders once it complete or got error during placing order
        del inprogress_orders[session_id]

    return JSONResponse(content={
        "fulfillmentText": res
    })
    
def save_to_db(order: dict):
    next_order_id = Order.get_next_order_id()

    # Insert individual items along with quantity in orders table
    for food_item, quantity in order.items():
        rcode = Order.insert_order_item(
            food_item,
            quantity,
            next_order_id
        )

        if rcode == -1:
            return -1
    
    # Now insert order tracking status
    Order.insert_order_tracking(next_order_id, "in progress")

    return next_order_id

def get_string_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


def remove_from_order(parameters: dict, session_id: str):
    """Handler for order.remove intent"""
    # print(f"Handling order.remove with params: {parameters} for session: {session_id}")
    if session_id not in inprogress_orders:
        return JSONResponse(content={
            "fulfillmentText" : "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
        })
    
    food_items = parameters.get("food-item")
    curr_order = inprogress_orders[session_id]
    
    removed_food_items = []
    food_item_not_exist = []

    for item in food_items:
        if item not in curr_order:
            food_item_not_exist.append(item)
        else:
            removed_food_items.append(item)
            del curr_order[item]

    if len(removed_food_items) > 0:
        res = f"Removed {",".join(removed_food_items)} from your order!"

    if len(food_item_not_exist) > 0:
        res = f" Your current order does not have {",".join(food_item_not_exist)}"

    if len(curr_order.keys()) == 0:
        res += " Your order cart is empty!"
    else:
        order_str = get_string_from_food_dict(curr_order)
        res += f" Here is what's left in your order: {order_str}"

    return JSONResponse(content={
        'fulfillmentText' : res
    })