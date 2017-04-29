from channels.routing import route
from capture.consumer import ws_connect, ws_capture


channel_routing = [
    route('websocket.connect', ws_connect),
    route('capture-stream',ws_capture),

]
