"""Module: Application page URLs and API endpoint constants"""


class URLS:
    """
    Collection of base URLs for pages and API endpoints used throughout the Stellar Burgers app.
    """

    BASE_URL: str = "https://stellarburgers.nomoreparties.site/"

    # Web page URLs
    REGISTER_PAGE: str = f"{BASE_URL}register"
    LOGIN_PAGE: str = f"{BASE_URL}login"
    FORGOT_PASSWORD_PAGE: str = f"{BASE_URL}forgot-password"
    RESET_PASSWORD_PAGE: str = f"{BASE_URL}reset-password"
    ACCOUNT_PAGE: str = f"{BASE_URL}account"
    PROFILE_PAGE: str = f"{BASE_URL}account/profile"
    ORDER_HISTORY_PAGE: str = f"{BASE_URL}account/order-history"
    ORDERS_FEED_PAGE: str = f"{BASE_URL}feed"

    # API endpoint paths (relative to BASE_URL)
    REGISTRATION_ENDPOINT: str = "api/auth/register"
    LOGIN_ENDPOINT: str = "api/auth/login"
    USER_ENDPOINT: str = "api/auth/user"
    DELETE_ENDPOINT: str = "api/auth/user"
    ORDER_ENDPOINT: str = "api/orders"
