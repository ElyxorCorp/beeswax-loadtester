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


class UserBehavior(TaskSet):

    @task
    def bidder_task(self):
        bid_request = BidRequest()
        h = {
            "beeswax-auth-secret": secret_value
        }
        self.client.post("/bid", bid_request, headers=h)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
