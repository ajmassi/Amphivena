import warnings
from unittest import mock

from cryptography.utils import CryptographyDeprecationWarning

# Suppresses warning from cryptography package (imported by scapy for tls support)
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from netfilterqueue import Packet as test_packet
from scapy.layers.inet import IP, TCP

client_hello = IP(
    bytes.fromhex(
        "450000ac1c184000400620327f0000017f000001973a01bb787c608f78bc736680187ffffea000000101080a1f537c981f537c9816030000730100006f03000034011e673afaced951bae4fc64950382630fe3396bc7bd2be5513723485bfb20a3caad46955d64bb33ecb5129121a350d2c0c5f667c3cc9ec04a711b92dc585500280039003800350033003200040005002f00160013feff000a00150012fefe000900640062000300060100"
    )
)


def test_tcp_sport_change(packet_processor):
    # Change TCP.sport from 38714 to 12345
    with mock.patch(
        "amphivena.packet_processor.PacketProcessor._finalize"
    ) as mock_accept:
        pkt = test_packet()
        pkt.set_payload(client_hello.__bytes__())

        assert client_hello.getlayer(TCP).sport == 38714
        packet_processor._process(pkt)

        assert (
            IP(mock_accept.call_args[0][0].get_payload()).getlayer(TCP).sport == 12345
        )
