from beeswax.openrtb.openrtb_pb2 import BidRequest
bid_request = BidRequest()
bid_request.id = "id_0" 
bid_request.test = False
bid_request.user.CopyFrom(BidRequest.User())
bid_request.user.data.add()
print(bid_request)
print(bid_request.SerializeToString())
