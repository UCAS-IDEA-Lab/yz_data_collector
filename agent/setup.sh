record_file_path=/var/lib/yz_agent
conf_file_path=/etc/yz_agent.conf

./setup.py install && \
  cp yz_agent.service /usr/lib/systemd/system && \
  if [ ! -d "$record_file_path" ]; then mkdir "$record_file_path"; fi && \
  if [ ! -f "$conf_file_path" ]; then cp yz_agent/etc/yz_agent.conf /etc/; fi && \
  echo "Setup successfully"

