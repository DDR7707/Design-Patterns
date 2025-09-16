from handler import RequestHandler

class AuthorizationHandler(RequestHandler):
   def handle(self, request):
       if request.user_role != "ADMIN":
           print("AuthorizationHandler: ❌ Access denied.")
           return
       print("AuthorizationHandler: ✅ Authorized.")
       self.pass_next_handler(request)
