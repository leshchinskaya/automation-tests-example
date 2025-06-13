import httpx


class ReqresClient:
    def __init__(self):
        self.base_url = "https://reqres.in/api"

    def get_users(self, page: int = 1):
        """
        Извлекает список пользователей для данной страницы
        """
        response = httpx.get(f"{self.base_url}/users", params={"page": page})
        response.raise_for_status()  # Исключение для ответов 4xx/5xx
        return response 