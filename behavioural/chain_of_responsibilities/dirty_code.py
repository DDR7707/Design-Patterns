from request import Request

class RequestHandler:
   def handle(self, request):
       if not self.authenticate(request):
           print("Request Rejected: Authentication failed.")
           return

       if not self.authorize(request):
           print("Request Rejected: Authorization failed.")
           return

       if not self.rate_limit(request):
           print("Request Rejected: Rate limit exceeded.")
           return

       if not self.validate(request):
           print("Request Rejected: Invalid payload.")
           return

       print("Request passed all checks. Executing business logic...")
       # Proceed to business logic

   def authenticate(self, req):
       return req.user is not None

   def authorize(self, req):
       return req.user_role == "ADMIN"

   def rate_limit(self, req):
       return req.request_count < 100

   def validate(self, req):
       return req.payload is not None and req.payload != ""

class App:
   @staticmethod
   def main():
       req = Request("john_doe", "ADMIN", 42, "{ 'data': 123 }")
       handler = RequestHandler()
       handler.handle(req)

if __name__ == "__main__":
    App.main()
