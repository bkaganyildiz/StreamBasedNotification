from channels.routing import route
from capture.consumer import ws_connect


channel_routing = [
    route('websocket.connect', ws_connect),
]
