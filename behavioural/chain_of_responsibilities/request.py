class Request:
   def __init__(self, user, user_role, request_count, payload):
       self.user = user
       self.user_role = user_role
       self.request_count = request_count
       self.payload = payload
