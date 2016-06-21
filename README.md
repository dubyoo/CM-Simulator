# CM-Simulator

### Usage:
```
$ ./senddte.py 
USAGE : ./senddte.py [IP] [Port] [SGID] [MAC] [group_ip] [leave_or_join]
SAMPLE: ./senddte.py 10.90.242.246 22408 100 00-1C-26-C8-5C-50 238.1.1.1 join
```

### Single Execution:
```
$ ./senddte.py 10.90.242.246 22408 100 00-1C-26-C8-5C-50 238.1.1.1 join 
[DEBUG] send to 10.90.242.246(22408):
SETUP rtsp://hlit.net RTSP/1.0\r\nCSeq: 313\r\nRequire: com.harmonic.d2e.ccp\r\nHeader: protocolDescriminator=17;dsmcc_type=4;message_id=1;transaction_id=393;\r\nContent-Length: 252\r\n\r\nmessage_payload: session_id=0; client_destination=192.26.14.1; client_cablemodem_mac_address=00-1C-26-C8-5C-50; source_ip=238.1.1.1;retry_count=2;rc_index=1;rc_chan_freq=480000000; client_cpe_destination=10.90.242.82;cm_vednor=name;cm_type=1;sgid=100\r\n
```

### Batch Excution:
```
$ cat config.dat 
[IP] [Port] [SGID] [MAC] [group_ip] [leave_or_join]
10.90.242.244 22408 100 00-1C-26-C8-5C-50 238.1.1.1 join
10.90.242.244 22408 100 00-1C-26-C8-5C-50 238.1.1.1 leave
10.90.242.244 22408 100 00-1C-26-C8-5C-50 238.1.1.1 join
```
```
$ ./run.py
[DEBUG] send to 10.90.242.244(22408):
SETUP rtsp://hlit.net RTSP/1.0\r\nCSeq: 313\r\nRequire: com.harmonic.d2e.ccp\r\nHeader: protocolDescriminator=17;dsmcc_type=4;message_id=1;transaction_id=393;\r\nContent-Length: 252\r\n\r\nmessage_payload: session_id=0; client_destination=192.26.14.1; client_cablemodem_mac_address=00-1C-26-C8-5C-50; source_ip=238.1.1.1;retry_count=2;rc_index=1;rc_chan_freq=480000000; client_cpe_destination=10.90.242.82;cm_vednor=name;cm_type=1;sgid=100\r\n

[DEBUG] send to 10.90.242.244(22408):
SETUP rtsp://hlit.net RTSP/1.0\r\nCSeq: 313\r\nRequire: com.harmonic.d2e.ccp\r\nHeader: protocolDescriminator=17;dsmcc_type=4;message_id=1;transaction_id=393;\r\nContent-Length: 252\r\n\r\nmessage_payload: session_id=1; client_destination=192.26.14.1; client_cablemodem_mac_address=00-1C-26-C8-5C-50; source_ip=238.1.1.1;retry_count=2;rc_index=1;rc_chan_freq=480000000; client_cpe_destination=10.90.242.82;cm_vednor=name;cm_type=1;sgid=100\r\n

[DEBUG] send to 10.90.242.244(22408):
SETUP rtsp://hlit.net RTSP/1.0\r\nCSeq: 313\r\nRequire: com.harmonic.d2e.ccp\r\nHeader: protocolDescriminator=17;dsmcc_type=4;message_id=1;transaction_id=393;\r\nContent-Length: 252\r\n\r\nmessage_payload: session_id=0; client_destination=192.26.14.1; client_cablemodem_mac_address=00-1C-26-C8-5C-50; source_ip=238.1.1.1;retry_count=2;rc_index=1;rc_chan_freq=480000000; client_cpe_destination=10.90.242.82;cm_vednor=name;cm_type=1;sgid=100\r\n
```
