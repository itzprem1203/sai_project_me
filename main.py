from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import serial.tools.list_ports
import serial
import threading
import asyncio

app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Global variables for serial port and threading
ser = None
serial_thread = None
clients = set()

# Function to get available COM ports
def get_available_com_ports():
    return [port.device for port in serial.tools.list_ports.comports()]

# Function to configure and open serial port
def configure_serial_port(com_port, baud_rate, parity, stopbits, bytesize):
    global ser
    try:
        ser = serial.Serial(
            port=com_port, 
            baudrate=int(baud_rate), 
            bytesize=int(bytesize), 
            timeout=None, 
            stopbits=float(stopbits), 
            parity=parity[0].upper()
        )
    except Exception as e:
        raise RuntimeError(f"Error configuring serial port: {str(e)}")

# Function to handle serial reading
def serial_read_thread():
    global ser
    try:
        while True:
            if ser and ser.is_open and ser.in_waiting > 0:
                receive = ser.read().decode('ASCII')
                asyncio.run(broadcast(receive))  # Use asyncio.run to call async function from sync context
    except serial.SerialException as e:
        print(f"Serial port error: {str(e)}")
    except Exception as e:
        print(f"Error in serial read thread: {str(e)}")
    finally:
        if ser and ser.is_open:
            ser.close()

# Function to broadcast messages to all connected clients
async def broadcast(message):
    for websocket in clients:
        try:
            await websocket.send_text(message)
        except Exception as e:
            print(f"Error broadcasting message: {str(e)}")

# WebSocket endpoint for handling client connections
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(0.1)  # Keep the connection open and yield to other tasks
    except WebSocketDisconnect:
        clients.remove(websocket)

# Endpoint to serve the HTML page
@app.get("/comport", response_class=HTMLResponse)
async def get_comport_page(request: Request):
    # Get available COM ports and baud rates
    com_ports = get_available_com_ports()
    baud_rates = ["4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000"]
    return templates.TemplateResponse("app/comport.html", {"request": request, "com_ports": com_ports, "baud_rates": baud_rates})

# Endpoint to start the serial reading based on client's selection
@app.post("/start")
async def start_serial(com_port: str = Form(...), baud_rate: str = Form(...), parity: str = Form(...), stopbit: str = Form(...), databit: str = Form(...)):
    global serial_thread
    try:
        # Configure serial port
        configure_serial_port(com_port, baud_rate, parity, stopbit, databit)

        # Send command to start data transmission
        if ser and ser.is_open:
            ser.write(b"MMMMMMMMMM")  # Replace with your actual command

        # Start serial read thread if not already running
        if serial_thread is None or not serial_thread.is_alive():
            serial_thread = threading.Thread(target=serial_read_thread)
            serial_thread.start()
        return JSONResponse({"message": "Serial port configured and reading started"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
