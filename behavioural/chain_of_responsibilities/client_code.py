from authentication_handler import AuthHandler
from authorization_handler import AuthorizationHandler
from data_validation_handler import ValidationHandler
from core_logic_handler import BusinessLogicHandler
from rate_limiter_handler import RateLimitHandler
from request import Request

class ClientCode:
    @staticmethod
    def main():
        # Initailize handlers
        auth = AuthHandler()
        authorization = AuthorizationHandler()
        data_validator = ValidationHandler()
        core_logic = BusinessLogicHandler()
        rate_limiter = RateLimitHandler()

        # Chain handlers
        auth.set_successor(authorization)
        authorization.set_successor(rate_limiter)
        rate_limiter.set_successor(data_validator)
        data_validator.set_successor(core_logic)

        request = Request("john", "ADMIN", 10, "{ \"data\": \"valid\" }")
        auth.handle(request)

        print("\n--- Trying an invalid request ---")
        bad_request = Request(None, "USER", 150, "")
        auth.handle(bad_request)

if __name__ == "__main__":
    ClientCode.main()
