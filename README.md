# vehicle-security-system-rpi4


vehicle-security-system-rpi4/
├── README.md                  # Complete documentation and setup guide
├── main.py                   # Main loop to run the system
├── config.py                 # Configuration: GPIO pins, email/Twilio options
├── sensor_handlers.py        # Handles HC-SR04, vibration & reed switch logic
├── notifications.py          # Email alert logic
├── requirements.txt          # Python dependencies
└── vehicle_security.service  # Optional systemd auto-start on boot
