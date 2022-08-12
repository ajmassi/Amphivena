import os
import warnings

import pytest
from cryptography.utils import CryptographyDeprecationWarning

# Suppresses warning from cryptography package (imported by scapy for tls support)
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from scapy.layers.inet import IP

from amphivena.packet_processor import PacketProcessor


def pytest_configure():
    pytest.TEST_PLAYBOOKS_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "playbooks/"
    )


@pytest.fixture()
def new_packet_processor():
    class ProcessorFactory:
        def get(self, playbook_file):
            return PacketProcessor(pytest.TEST_PLAYBOOKS_DIR + playbook_file)

    yield ProcessorFactory()


# ---------------------------------------------------------
# ~~Test Packet Fixtures~~
# Test pcap hex data sourced from wireshark examples (https://wiki.wireshark.org/SampleCaptures)


@pytest.fixture()
def new_tls_client_hello():
    yield IP(
        bytes.fromhex(
            "4500009d496e40004006f2ea7f0000017f000001973901bb788c399778c524d980187ffffe9100000101080a1f5371031f5371038067010300004e000000100100800300800700c006004002008004008000003900003800003500003300003200000400000500002f00001600001300feff00000a00001500001200fefe000009000064000062000003000006a8b893bb90e92aa24d6dcc1ce72a8021"
        )
    )


@pytest.fixture()
def new_tls_server_hello():
    yield IP(
        bytes.fromhex(
            "450003d555db40004006e3457f0000017f00000101bb973978c524d9788c3a0080187fff01ca00000101080a1f5371051f537103160300004a020000460300444c948ffe81ed93650288a3f8eb63860e2cf68dd00f2c2ad64fcd2d3c16d7d620a0fb60863d1e76f330fe0b01fd1a01ed95f67b8ec0d427bff06ec756b147ce9800350016030003440b00034000033d00033a308203363082029fa003020102020101300d06092a864886f70d01010405003081a9310b3009060355040613025859311530130603550408130c536e616b6520446573657274311330110603550407130a536e616b6520546f776e31173015060355040a130e536e616b65204f696c2c204c7464311e301c060355040b1315436572746966696361746520417574686f72697479311530130603550403130c536e616b65204f696c204341311e301c06092a864886f70d010901160f636140736e616b656f696c2e646f6d301e170d3033303330353136343734355a170d3038303330333136343734355a3081a7310b3009060355040613025859311530130603550408130c536e616b6520446573657274311330110603550407130a536e616b6520546f776e31173015060355040a130e536e616b65204f696c2c204c746431173015060355040b130e576562736572766572205465616d31193017060355040313107777772e736e616b656f696c2e646f6d311f301d06092a864886f70d010901161077777740736e616b656f696c2e646f6d30819f300d06092a864886f70d010101050003818d0030818902818100a46e53140ade2ce360559af242a6af47122f17cefabadc4e635634b9ba734b78443dc66c69a425b361029d09043f723dd827d3b05a4577b736e42623cc12b8aedea7b63a823c7c24590af896438ba329363f917f5dc72394297f0ace0abd8d9b2f1917aad58eec66a237eb3f57533cf2aabb79194b907ea7a399fe844c89f03d0203010001a36e306c301b0603551d1104143012811077777740736e616b656f696c2e646f6d303a06096086480186f842010d042d162b6d6f645f73736c2067656e65726174656420637573746f6d20736572766572206365727469666963617465301106096086480186f8420101040403020640300d06092a864886f70d010104050003818100ae7979229075fda6d5c4b8c4994e1c057c9159be890d3dc68ca3cff6ba23dfb8ae44688a8fb98bcb12dae6a2caa5a655d9d2a1adba9b2c44951d4a90597f83ae815e3f92e01441824e7f53fd1023eb8aebe992ea61f28e19a1d349c084341e2e6ef698e28753d655d91a8a925caddc1e1c30a7659dc24f60d26fdbe09f9ebc4116030000040e000000"
        )
    )
