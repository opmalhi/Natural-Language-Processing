from fastapi import APIRouter, HTTPException
from utils.session_utils import extract_session_id

from handlers.order_handlers import add_to_order, remove_from_order, complete_order, new_order
from handlers.track_order_handlers import track_order

webhook_router = APIRouter()

@webhook_router.post("/")
async def webhook_route(body: dict):
    try:
        # Extract intent information
        query_result = body.get('queryResult')
        intent_name = query_result.get('intent').get('displayName')
        parameters = query_result.get('parameters')
        output_contexts = query_result.get('outputContexts')

        # Extract session ID
        session_id = extract_session_id(output_contexts[0]["name"])

        intent_handler_dict = {
            'new.order': new_order,
            'order.add - context: ongoing-order': add_to_order,
            'order.remove - context: ongoing-order': remove_from_order,
            'order.complete - context: ongoing-order': complete_order,
            'track.order - context: ongoing-tracking': track_order,
        }
        return intent_handler_dict[intent_name](parameters, session_id)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        