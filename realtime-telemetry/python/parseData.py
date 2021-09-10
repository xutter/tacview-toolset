from socket import *
from struct import unpack,pack
from threading import Thread, Lock
import pyproj

HandShakeData = \
'XtraLib.Stream.0\n' +\
'TacView.RealTimeTelemetry.0\n' +\
'Multirotor\n'
TelFileHeader = "FileType=text/acmi/tacview\nFileVersion=2.2\n"
TelReferenceTimeFormat = '0,ReferenceTime=%Y-%m-%dT%H:%M:%SZ\n'
TelDataFormat = '#%.2f\n3000102,T=%.7f|%.7f|%.7f|%.1f|%.1f|%.1f,Type=Air+Rotorcraft,Color=Red,Coalition=Allies\n'

LOCALPORT = 58008
LOCALIP='127.0.0.1'
# so = socket(AF_INET,SOCK_DGRAM,IPPROTO_UDP)

gps_crs = "EPSG:4326"
gauss_crs = "+proj=tmerc +ellps=krass +lon_0=32.087 +k=0.99999 +units=m +no_defs"
proj = pyproj.Proj(gauss_crs)

# so.bind(('127.0.0.1',58008))
LAT = 32.087
LON = 118.323
x, y = proj(LON, LAT)

class Kinematics:
    def __init__(self):
        self.x,self.y,self.z=0,0,0
        self.vx,self.vy,self.vz=0,0,0
        self.roll,self.pitch,self.yaw = 0,0,0
        self.lock = Lock()

    def parse(self,data):
        global x,y
        with self.lock:
            (self.x,self.y,self.z,self.vx,self.vy,self.vz,_,_,_,self.roll,self.pitch,self.yaw,_,_,_,_,_,_) \
                = unpack('<ffffffffffffffffff',data)
            self.z = self.z * -1 + 100
            self.x = x + self.x
            self.y = y + self.y
            self.x,self.y = proj(self.x,self.y,inverse=True)
            print("%.2f   %.2f   %.2f"%(self.x,self.y,self.z))

    def pack(self,delta_t):
        with self.lock:
            line = format(TelDataFormat%(delta_t,self.x,self.y,self.z,self.roll,self.pitch,self.yaw)).encode('utf-8')
            print(line)
            return line
                          
# while True:
#     da,ad = so.recvfrom(1024)
#     print(len(da),ad)
#     datas = 
#     print(datas)
