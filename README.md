# Chat-It
This is a very simple chat box for two machines on the same network.

Python 3.x and socket module is used to create this program.

How it works: The server sided machine opens a port and listens for messages(TCP). In the client script, you are prompted with the IP address of the server machine. Find the IP address using "ipconfig" (for windows) or "ifconfig"(for linux) in the machine terminal. Provide it to the script and start chating.

This program is cross platform. But, you can only input one line at a time in the program. Once you have pressed enter you have to wait for the response from the other side, before you can send another message.
