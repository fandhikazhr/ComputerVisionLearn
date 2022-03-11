# droneAutomation
Learn about programming automatic drone 

- Step 1

  ```
  dronekit-sitl copter
  ```
  
  `--home=x,y,0,0` for set home location
  `--speedup 5` for set speed throtle to 5
  

- Step 2

  ```
  MAVProxy --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551 --out 127.0.0.1:14552
  ```
  
# Preview

![Screenshot (331)](https://user-images.githubusercontent.com/99522867/157839813-b3aafee6-134a-4289-8f95-f01d42cf4c26.png)

