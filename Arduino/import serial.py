import serial
import struct
import time
import csv

PORT = 'COM5'          # Your Arduino port (could be different)
BAUDRATE = 115200
TIMEOUT = 5           

MAX_SAMPLES = 512
BYTES_PER_SAMPLE = 2
MAX_READ_BYTES = MAX_SAMPLES * BYTES_PER_SAMPLE  

ADC_MAX = 1023.0
V_REF = 5.0

OUTPUT_CSV =  r'C:\Users\klipk\Downloads\serial1_data.csv' 

def main():
    with serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT) as ser:
        print(f"Opened serial port: {PORT}")

        time.sleep(3)

        print("Reading up to 1024 bytes from Arduino...")
        raw_data = ser.read(MAX_READ_BYTES)
        num_bytes = len(raw_data)
        print(f"Received {num_bytes} bytes")

        num_samples = num_bytes // BYTES_PER_SAMPLE
        readings = []
        
        offset = 0
        for _ in range(num_samples):
            val = struct.unpack_from('<h', raw_data, offset)[0]
            offset += 2
            readings.append(val)

        with open(OUTPUT_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Sample Index', 'Voltage (V)'])

            for i, adc_value in enumerate(readings):
                voltage = (adc_value / ADC_MAX) * V_REF
                writer.writerow([i, f"{voltage:.6f}"])

        print(f"Done! Wrote {num_samples} samples to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()

