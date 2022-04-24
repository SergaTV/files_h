(cd ~/$((ls ~/ | grep friendly-telegram)||(ls ~/ | grep Hikka)) && echo "[Service]
WorkingDirectory=$(pwd)/
ExecStart=/usr/bin/python3 -m $((ls ~/ | grep friendly-telegram)||((ls ~/ | grep Hikka) &>/dev/null)&&echo hikka)
Type=simple
Restart=always
RestartSec=1
User=$(whoami)
[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/ftg.service && systemctl start ftg && systemctl enable ftg) || echo "error occured."