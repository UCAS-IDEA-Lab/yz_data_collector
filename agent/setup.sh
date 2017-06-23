# mkdir /var/lib/yz_agent/ && touch /var/lib/yz_agent/offset.rec
./setup.py install && cp yz_agent.service /usr/lib/systemd/system && echo "Setup successfully"

