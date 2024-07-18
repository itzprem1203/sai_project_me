# fastapi_app.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import serial.tools.list_ports
import serial
import threading
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

ser = None
serial_thread = None
clients = set()

def get_available_com_ports():
    return [port.device for port in serial.tools.list_ports.comports()]

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

def serial_read_thread():
    global ser
    try:
        while True:
            if ser and ser.is_open and ser.in_waiting > 0:
                receive = ser.read().decode('ASCII')
                asyncio.run(broadcast(receive))
    except serial.SerialException as e:
        print(f"Serial port error: {str(e)}")
    except Exception as e:
        print(f"Error in serial read thread: {str(e)}")
    finally:
        if ser and ser.is_open:
            ser.close()

async def broadcast(message):
    for websocket in clients:
        try:
            await websocket.send_text(message)
        except Exception as e:
            print(f"Error broadcasting message: {str(e)}")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        clients.remove(websocket)

@app.get("/comport", response_class=HTMLResponse)
async def comport(request: Request):
    com_ports = get_available_com_ports()
    baud_rates = ["4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000"]
    return templates.TemplateResponse("app/comport.html", {"request": request, "com_ports": com_ports, "baud_rates": baud_rates})

@app.post("/comport")
async def start_serial(com_port: str = Form(...), baud_rate: str = Form(...), parity: str = Form(...), stopbit: str = Form(...), databit: str = Form(...)):
    global serial_thread
    try:
        configure_serial_port(com_port, baud_rate, parity, stopbit, databit)
        command = "MMMMMMMMMM"
        ser.write(command.encode('ASCII'))

        if serial_thread is None or not serial_thread.is_alive():
            serial_thread = threading.Thread(target=serial_read_thread)
            serial_thread.start()
        return JSONResponse({"message": "Serial port configured and reading started"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
