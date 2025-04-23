<h1>Firewatch</h1>
A YOLO model to detect fire and smoke. 

Created by:
<ul>
  <li>Ethan Edwards</li>
  <li>Felix Desjarlais</li>
  <li>Adam "Alice" Erskine</li>
  <li>Angel Centeno</li>
</ul>

<h2>To Build</h2>
The project has the following dependanices:
<ul>
  <li>PyTorch</li>
  <li>PIL</li>
  <li>Ultralytics YOLO</li>
</ul>

<h2>To Run</h2>
To run the demo, use the following steps:
<ul>
  <li>
    Start the demo server with:
    
    python3 demo_server.py
  </li>
  <li>
    Start the demo controller with:

    python3 demo_controller.py
  </li>
  <li>Ping the server with the controller to ensure the server has port access with the "ping" command.</li>
  <li>
    Start the demo node with:

    python3 demo_node.py
  </li>
  <li>The demo node should send 4 images to the server for recognition, then print their response codes.</li>
  <li>The server can be stopped with the "shutdown" command through the controller.</li>
  <li>The controller can be stopped with the "exit" command.</li>
</ul>

<h2>Known Issues</h2>
<ul>
  <li>If you are on Windows, filepaths in the demo may not work by default. If this is the case, editing the "image_paths" list in the demo_node.py code should resolve the issue.</li>
  <li>The program will not function if python isn't given firewall access. How to go about doing this is system-dependant, but guides can be easily found online.</li>
</ul>

<h2>Credits</h2>

[Ultralytics](https://www.ultralytics.com/) (for YOLOv11)

[D-Fire Dataset](https://github.com/gaiasd/DFireDataset)
