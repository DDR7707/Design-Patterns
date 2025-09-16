from handler import RequestHandler

class AuthHandler(RequestHandler):
   def handle(self, request):
       if request.user is None:
           print("AuthHandler: ❌ User not authenticated.")
           return  # Stop the chain
       print("AuthHandler: ✅ Authenticated.")
       self.pass_next_handler(request)
