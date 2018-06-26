from beeswax.openrtb.openrtb_pb2 import BidRequest
from locust import HttpLocust, TaskSet, task
import logging
import os

secret_value = os.getenv('BEESWAX_AUTH_SECRET', None)

log_dir = os.path.join(os.sep, 'var', 'log', 'loadtester')
log_file_name = 'test-events.log'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.getLogger(__name__)
logging.basicConfig(format='%(message)s', filename=os.path.join(log_dir, log_file_name), level=logging.INFO)

if secret_value is None:
    raise Exception("BEESWAX_AUTH_SECRET was not set in environment")


sample_data = b'\n\xe2\x0c\n)1756de41_5b951a0c65f8aff79dc77c8e582d5a02\x12C\n\x011\x12\x16\x08\xac\x02\x10\xfa\x01 \x05(\x01(\x040\x010\t0\n0\r0\x0e0\x00:\n4041055571AmV}\xae\xb6b\xfa?J\x03USD`\x00p\xac\x02\xc2>\x04\x10\x00\x18\x01"\xa0\x01\n\r1541113971426\x12\x1eiphone_latest_300x250_instream\x1a\x0cthechive.com"\x04IAB1"\x05IAB14B\t448999087Z\x0e\n\n1905359552\x12\x00r9https://itunes.apple.com/us/app/thechive/id448999087?mt=8*\xec\x02\x08\x00\x12\xa5\x01Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 QuantcastSDK/iOS_1.6.0/17015wuu1v2et4hw-0u25mp4sd8axar1c\x1a\x0f174.234.132.138"#\t\xa2\xb47\xf8\xc2LC@\x11\xbf\x0e\x9c3\xa2\x80V\xc0\x1a\x02US"\x02MOB\x0565807H\x02R\x07VERIZONZ\x02enb\x05Applej\x06iPhoner\x03iOSz\x0411_4\x80\x01\x01\x88\x01\x03\x90\x01\x04\xd2\x01$51d7266b-08cd-4fa5-8280-1e279c16e143\xc2>2\x12\x01M\x1a\x06Safari"\x02-1*\x03iOS2\x0211:\x06iPhoneB\x05AppleH\x01R\x07Verizon2\xed\x05\n$ee9b5ee5-3f32-446b-aa4f-dedebcb9f43b\x12\x16ABGNo06uWgkAAGfN6dQw6w:-\x1a\x03USA"\x06USA/MO2\x03619:\x074409896B\x0565807\xc2>\x08\x12\x06USA/MOB\'\n\x07roivant\x1a\x17\n\x15roivant-segmentabsent\xc2>\x02\x08\x01B\'\n\x07bluekai\x1a\x17\n\x15bluekai-segmentabsent\xc2>\x02\x08\x01B\x1f\n\x03ias\x1a\x13\n\x11ias-segmentabsent\xc2>\x02\x08\x01B\xc7\x03\x1a\x0b\n\tias-74572\x1a\x0b\n\tias-74573\x1a\x0b\n\tias-74576\x1a\x0b\n\tias-74577\x1a\x0b\n\tias-74574\x1a\x0b\n\tias-74575\x1a\x0b\n\tias-72009\x1a\x0b\n\tias-72031\x1a\x0b\n\tias-72030\x1a\x0b\n\tias-72033\x1a\x0b\n\tias-72032\x1a\x0b\n\tias-72035\x1a\x0b\n\tias-72034\x1a\x0b\n\tias-72019\x1a\x0b\n\tias-72018\x1a\x0b\n\tias-72017\x1a\x0b\n\tias-72016\x1a\x0b\n\tias-72015\x1a\x0b\n\tias-72014\x1a\x0b\n\tias-72013\x1a\x0b\n\tias-72012\x1a\x0b\n\tias-72011\x1a\x0b\n\tias-72037\x1a\x0b\n\tias-72036\x1a\x0b\n\tias-72038\x1a\x0b\n\tias-74567\x1a\x0b\n\tias-72022\x1a\x0b\n\tias-72023\x1a\x0b\n\tias-72020\x1a\x0b\n\tias-72021\x1a\x0b\n\tias-72026\x1a\x0b\n\tias-72024\x1a\x0b\n\tias-72025\x1a\x0b\n\tias-72028\x1a\x0b\n\tias-72029\xc2>@\n(mid.51D7266B-08CD-4FA5-8280-1E279C16E143\x10\x022\x12ip.174.234.132.1388\x01@}Z\x03USDb\x05IAB25b\x05IAB26b\x07IAB25_3j\x0bplayrix.comr\x07\x08\x00\xc2>\x02\x08\x00\x9a\x01\x1f\x1a\x1d-35d5010d7789b49d:adconductor\xc2>\x94\x01\x08\x18\x12\x12\x08\x8d\xe5\xf4\x88\r\x10\xce6\x18\x9b\xed\xf1\xeb\xbf\xe2\xdb\x02\x1a@\n\x03USA\x12\x06USA/MO\x1a\x074409896"\x0565807*\x036190\x019\xa2\xb47\xf8\xc2LC@A\xbf\x0e\x9c3\xa2\x80V\xc0H\x02R\x06USA/MO \xef&*\x07roivantB(1529506531407515.3508351629.6990.roivantP\x0bX\x00`\x00\x12=\x08\x03\x10\x02\x10\x03\x10\x04\x10\x05\x1a\x1e"\x1a\n\x18roivant_bidding_strategy(\x01"\x02\x08\x00(\x010\x02:\x07roivant@\x01'





class UserBehavior(TaskSet):

    @task
    def bidder_task(self):
        bid_request = BidRequest()
        bid_request.id = "id_0" 
        bid_request.test = False
        bid_request.user.CopyFrom(BidRequest.User())
        bid_request.user.data.add()
        print(bid_request)
        print(bid_request.SerializeToString())

        h = {
            "beeswax-auth-secret": secret_value,
            "content-type": "application/x-protobuf",
            "content-length": str(len(sample_data))
        }
        self.client.post("/bid", sample_data, headers=h)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
