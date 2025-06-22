# **[Demo Simulation available here](https://wokwi.com/projects/434431263713593345)**


vehicle-security-system-rpi4/<br>
├── main.py<br>
├── config.py<br>
├── sensor_handlers.py<br>
├── notifications.py<br>
├── requirements.txt<br>
├── vehicle_security.service<br>
└── README.md<br>

# 🚗 Smart Vehicle Security / Theft Deterrent System

This Raspberry Pi 4 project uses sensors like ultrasonic, reed switch, and vibration detectors to detect unauthorized vehicle access. It sounds a buzzer and sends optional alerts when motion, proximity, or tampering is detected.

---

## 🧰 Hardware Required

| Component                    | Qty |
|-----------------------------|-----|
| Raspberry Pi 4 Model B      | 1   |
| 32GB microSD Card           | 1   |
| Active Buzzer               | 1   |
| Vibration Switch            | 2   |
| Reed Switch (magnetic)      | 2   |
| HC-SR04 Ultrasonic Sensor   | 1   |
| Push Buttons                | 2   |
| LEDs + 330Ω Resistors       | Several |
| Breadboard & Jumper Wires   | -   |
| 5V USB-C Power Supply       | 1   |

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ssfahim/vehicle-security-system-rpi4.git
cd vehicle-security-system-rpi4
```

### Step 2: Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-rpi.gpio
pip3 install -r requirements.txt
```

## ⚙️ **Configuration**
Edit the config.py file to match your wiring and enable/disable features like email or SMS alerts.


## 🚀 **Run the Program**

```bash
python3 main.py
```



## 🔁 **Auto-Start on Boot**
To run the system on boot using systemd:

```bash
sudo cp vehicle_security.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable vehicle_security
sudo systemctl start vehicle_security
```


## ✉️ Notification Features
Optional: Enable in config.py

Email Alerts (via SMTP)

SMS Alerts (via Twilio API)


## 🧠 License & Credits
Made with ❤️ at a hackathon. Feel free to fork and improve!
