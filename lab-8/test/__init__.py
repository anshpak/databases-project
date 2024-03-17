from connector.Connector import Connector
from tools.DBTools import DBTools
from tools.DBSkydivingTools import DBSkydivingTools

if __name__ == "__main__":
    connector = Connector("localhost", "root", "sic mundus creatus est", "skydiving", 1)
    connector.connect(successful_report=False)
    connector.disconnect()
