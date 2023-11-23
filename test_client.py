import asyncio
import websockets

async def connect_to_server():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = "Hello, WebSocket Server!"
        print(f"Sending message: {message}")
        await websocket.send(message)

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received response: {response}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_server())

#TODO have a unity (c#) client sending images (find out which format) to bytes for the server
