(cd ~/*riendl* && echo "Description=FTG
[Service]
WorkingDirectory=$(pwd)/
ExecStart=/usr/bin/python3 -m friendly-telegram
Type=simple
Restart=always
RestartSec=1
User=$(whoami)
[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/ftg.service && systemctl start ftg && systemctl enable ftg) || echo "friendly-telegram not found."
