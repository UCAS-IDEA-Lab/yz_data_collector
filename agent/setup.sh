record_file_path=/var/lib/yz_agent

./setup.py install && \
  cp yz_agent.service /usr/lib/systemd/system && \
  if [ ! -d "$record_file_path" ]; then mkdir "$record_file_path"; fi \
  cp yz_agent/etc/yz_agent.conf /etc/ && \
  echo "Setup successfully"

