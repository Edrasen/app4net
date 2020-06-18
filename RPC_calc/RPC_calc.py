import rpyc
import util
from rpyc.utils.server import ThreadedServer

class RPC_Calculator(rpyc.Service):
    def exposed_prefija(self,pref_exp):
        res  = util.evaluacionPrefija(pref_exp)
        return res
    
    def exposed_infija(self,inf_exp):
        res  = util.evaluacionInfija(inf_exp)
        return res
    
    def exposed_posfija(self,pos_exp):
        res  = util.evaluacionPosfija(pos_exp)
        return res

    def on_connect(self, conn):
        print("New connection")
        return super().on_connect(conn)

    def on_disconnect(self, conn):
        print("Connection closed")
        return super().on_disconnect(conn)

if __name__ == "__main__":
    server = ThreadedServer(RPC_Calculator, port = 12345)
    print("Server started...")
    server.start()
