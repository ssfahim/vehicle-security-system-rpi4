# vehicle-security-system-rpi4


vehicle-security-system-rpi4/<break>
├── README.md                  # Complete documentation and setup guide<break>
├── main.py                   # Main loop to run the system<break>
├── config.py                 # Configuration: GPIO pins, email/Twilio options<break>
├── sensor_handlers.py        # Handles HC-SR04, vibration & reed switch logic<break>
├── notifications.py          # Email alert logic<break>
├── requirements.txt          # Python dependencies<break>
└── vehicle_security.service  # Optional systemd auto-start on boot<break>
