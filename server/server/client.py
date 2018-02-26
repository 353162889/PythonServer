import socket
import struct
import protobuf.Msg_pb2

class CustomClient:
    def __init__(self):
        self.socket = socket.socket()

    def connect(self, addr):
        self.socket.connect(addr)
        while True:
            inp = input("请输入:")
            print("发送数据:"+inp)
            info = protobuf.Msg_pb2.Info()
            info.msg = inp
            bs = info.SerializeToString()
            self.socket.sendall(struct.pack("iHH"+str(len(bs))+"s", len(bs) + 8,1,1, bs))
            # self.socket.sendall(struct.pack("i"+str(len(inp))+"s",len(bytes(inp))+4,inp))

            head_bytes = self.socket.recv(8)
            unpack = struct.unpack("iHH",head_bytes)
            length = unpack[0]
            id = unpack[1]
            status = unpack[2]
            data = self.socket.recv(length - 8)
            recvInfo = protobuf.Msg_pb2.Info()
            recvInfo.ParseFromString(data)
            print("receive form server,length:{0} id:{1} status:{2} msg:{3}".format(length,id,status,recvInfo.msg))
            # print(str(length)+str(id) + str(status)+recvInfo.msg)

if __name__ == "__main__":
    client = CustomClient()
    client.connect(("127.0.0.1",8080))
