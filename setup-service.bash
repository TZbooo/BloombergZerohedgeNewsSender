service_name=$"python-auto-sender.service"

if [ $(systemctl is-active ${service_name}) == "active" ]; then
    echo "service is active"
    echo "restarting"
    systemctl restart ${service_name}
    echo "service restarted"
else
    echo "creating service file"
    cat > /etc/systemd/system/${service_name} << EOF
[Unit]
Description=auto sender bloomberg and zerohedge news
After=network.target

[Service]
ExecStart=/home/helloworld/Documents/Projects/IliyaLeto/BloombergZerohedgeNewsSender/env/bin/python /home/helloworld/Documents/Projects/IliyaLeto/BloombergZerohedgeNewsSender/run.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
    echo "enabling $service_name service"
    systemctl enable ${service_name}
    systemctl start ${service_name}
    echo "service started"
fi
exit 0