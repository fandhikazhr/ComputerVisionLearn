# droneAutomation
Learn about programming automatic drone 

- Step 1

  ```
  dronekit-sitl copter --home=-7.833720493928131,110.38309035134006,0,0
  ```
  
  `--home=x,y,0,0` for set home location
  
  `--speedup 5` for set speed throtle to 5, default speed is 1
  

- Step 2

  On Windows

  ```
  MAVProxy --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551 --out 127.0.0.1:14552
  ```
  
  On Linux
  
  ```
  mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551 --out 127.0.0.1:14552
  ```
  
- Step 3
  
  Simulation without python script.
  1. Open Tab Action.
  
  ![Screenshot from 2022-03-23 20-43-33](https://user-images.githubusercontent.com/99522867/159713637-5348b25f-24e9-4b46-842e-ce49c56b5e59.png)

  
# Preview

![Screenshot (331)](https://user-images.githubusercontent.com/99522867/157839813-b3aafee6-134a-4289-8f95-f01d42cf4c26.png)

