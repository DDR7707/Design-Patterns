from handler import RequestHandler

class RateLimitHandler(RequestHandler):
   def handle(self, request):
       if request.request_count >= 100:
           print("RateLimitHandler: ❌ Rate limit exceeded.")
           return
       print("RateLimitHandler: ✅ Within rate limit.")
       self.pass_next_handler(request)
