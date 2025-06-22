# vehicle-security-system-rpi4


vehicle-security-system-rpi4/<br>
├── README.md                  # Complete documentation and setup guide<br>
├── main.py                   # Main loop to run the system<br>
├── config.py                 # Configuration: GPIO pins, email/Twilio options<br>
├── sensor_handlers.py        # Handles HC-SR04, vibration & reed switch logic<br>
├── notifications.py          # Email alert logic<br>
├── requirements.txt          # Python dependencies<br>
└── vehicle_security.service  # Optional systemd auto-start on boot<br>
