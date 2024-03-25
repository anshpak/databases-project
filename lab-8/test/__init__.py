from connector.Connector import Connector
from tools.DBSkydivingTools import DBSkydivingTools
from tools.DBTools import DBTools
import threading

if __name__ == "__main__":
    connector_1 = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    connector_1.connect(successful_report=False)
    # connector_2 = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 2)
    # connector_2.connect(successful_report=False)
    # thread_1 = threading.Thread(target=DBSkydivingTools.give_user, args=(connector_1, 2, 1, 100))
    # thread_2 = threading.Thread(target=DBSkydivingTools.give_user, args=(connector_2, 1, 2, 100))
    # thread_1.start()
    # thread_2.start()
    # thread_1.join()
    # thread_2.join()

    connector_1.disconnect()
    # connector_2.disconnect()
