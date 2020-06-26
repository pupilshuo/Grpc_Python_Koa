#coding:utf-8
import time
import grpc
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc
from concurrent import futures
import base64

class Hello(pb2_grpc.HelloServicer):#所有的服务器部署都是pb2_grpc
    def HelloLys(self,request,context):
        str=request.pic
        file_str=open('2.jpg','wb')
        file_str.write(base64.b64decode(str))
        file_str.close()
        result ="已经转码完成"
        return pb2.HelloRes(result=result)#所有的proto的res和req都是在pb2当中

def run():
    server =grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_HelloServicer_to_server(Hello(),server)
    server.add_insecure_port('0.0.0.0:2000')
    print('服务器在2000端口启动')
    server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()