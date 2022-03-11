# droneAutomation
Learn about programming automatic drone 

- Step 1

  ```
  dronekit-sitl copter --home=
  ```
  
  <p> --home=x,y,0,0 </p>

- Step 2

  ```
  MAVProxy --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551 --out 127.0.0.1:14552
  ```
