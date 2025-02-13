from fastapi.responses import JSONResponse
from models.order_model import Order

def track_order(parameters: dict, session_id: str):
    print(f"Handling track.order with params: {parameters}")
    
    order_id = int(parameters.get('number'))
    order_status = Order.get_status(order_id)

    if order_status:
        status = f"The order status for order id: {order_id} is: {order_status}"
    else:
        status = f"No order found with order id: {order_id}"
    
    return JSONResponse(content={
            "fulfillmentText": status
        })

