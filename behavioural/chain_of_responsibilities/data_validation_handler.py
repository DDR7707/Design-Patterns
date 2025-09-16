from handler import RequestHandler

class ValidationHandler(RequestHandler):
   def handle(self, request):
       if request.payload is None or request.payload.strip() == "":
           print("ValidationHandler: ❌ Invalid payload.")
           return
       print("ValidationHandler: ✅ Payload valid.")
       self.pass_next_handler(request)
