import asyncio
import websockets
from image_handler import handle_image

async def handle_websocket(websocket, path):
    # This function will be called whenever a new WebSocket connection is established
    print(f"Client connected to {path}")

    try:
        while True:
            # Wait for messages from the client
            message = await websocket.recv()
            
            await websocket.send(handle_image(message))

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected from {path}")
    except websockets.exceptions.ConnectionClosedOK:
        print(f"Client disconnected from {path}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected from {path}")

# Set up the WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

