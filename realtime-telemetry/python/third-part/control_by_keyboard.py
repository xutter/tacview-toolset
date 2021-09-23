import keyboard
import airsim

name ="MR-"
number = '0'
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True,name + number)
client.armDisarm(True,name + number)
#client.takeoffAsync(5).join();
# client.moveByVelocityBodyFrameAsync(0, 0, 0, 10).join()

def abc(x):
    global name, number
    w = keyboard.KeyboardEvent('down', 28, 'w')
    s = keyboard.KeyboardEvent('down', 28, 's')
    a = keyboard.KeyboardEvent('down', 28, 'a')
    d = keyboard.KeyboardEvent('down', 28, 'd')
    up = keyboard.KeyboardEvent('down', 28, 'up')
    down = keyboard.KeyboardEvent('down', 28, 'down')
    left = keyboard.KeyboardEvent('down', 28, 'left')
    right = keyboard.KeyboardEvent('down', 28, 'right')
    enter = keyboard.KeyboardEvent('down', 28, 'enter')
    k = keyboard.KeyboardEvent('down', 28, 'k')
    l = keyboard.KeyboardEvent('down', 28, 'l')
    k_1 = keyboard.KeyboardEvent('down', 28, '1')
    k_2 = keyboard.KeyboardEvent('down', 28, '2')
    k_3 = keyboard.KeyboardEvent('down', 28, '3')
    print(x.name)

    if x.event_type == 'down' and x.name == w.name:
        #前进
        #print(name+number)
        client.moveByVelocityBodyFrameAsync(-30, 0, -15, 10,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == s.name:
        #后退
        client.moveByVelocityBodyFrameAsync(30, 0, -15, 0.07,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == a.name:
        #左移
        client.moveByVelocityBodyFrameAsync(0, -30, -15, 0.07,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == d.name:
        #右移
        client.moveByVelocityBodyFrameAsync(0, 30, -15, 0.07,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == up.name:
        #上
        client.moveByVelocityBodyFrameAsync(0, 0, -50, 0.07,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == down.name:
        #下
        client.moveByVelocityBodyFrameAsync(0, 0, 50, 0.07,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == left.name:
        #左转
        client.rotateByYawRateAsync(-20, 0.07,name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == right.name:
        #右转
        client.rotateByYawRateAsync(20, 0.07,name+number)
        print(x.name)
    elif x.event_type == 'down' and x.name == enter.name:
        #enter
        print(x.name)
    elif x.event_type == 'down' and x.name == k.name:
        # get control
        client.enableApiControl(True)
        print("get control")
        # unlock
        client.armDisarm(True)
        print("unlock")
        # Async methods returns Future. Call join() to wait for task to complete.
        client.takeoffAsync(name+number).join()
        print("takeoff")
        print("你按下了 " + x.name + " 键")
    elif x.event_type == 'down' and x.name == l.name:
        #降落
        client.landAsync().join()
        print("land")
        # lock
        client.armDisarm(False,name+number)
        print("lock")
        # release control
        client.enableApiControl(False)
        print("release control")

        print("你按下了 " + x.name + " 键")
    elif x.event_type == 'down' and x.name == k_1.name:
        number = '0'
        print('Change control to Multirotor 1')
    elif x.event_type == 'down' and x.name == k_2.name:
        number = '1'
        print('Change control to Multirotor 2')
    elif x.event_type == 'down' and x.name == k_3.name:
        number = '2'
        print('Change control to Multirotor 3')
    else:#没有按下按键
        pass
        # client.moveByVelocityBodyFrameAsync(0, 0, 0, 0.5,airsim.DrivetrainType.MaxDegreeOfFreedom,airsim.YawMode(),name+number).join()
        # client.hoverAsync(name+number).join()  # 第四阶段：悬停6秒钟
        # print("stop 悬停")


    #当监听的事件为enter键，且是按下的时候
keyboard.hook(abc)
keyboard.wait()
