import requests
import json
from datetime import datetime


class AvitoClient:
    def __init__(self, url: str):
        self.url = url

    def __user_get_status(self, user_id: int) -> dict:
        """
            Get the status of user
        @param user_id: ID of the user
        @return: dict of statuses
        """
        global response_json, response
        try:
            response = requests.get(f'{self.url}/web/user/get-status/{user_id}')
            response_json = json.loads(response.content)
        except Exception as err:
            print(f'Couldn"t get response of the user {err}')

        return response_json if response.status_code == 200 else None

    def get_user_last_action_time(self, user_id: int) -> datetime:
        """
            Get the user's last action time' in datetime format
        @param user_id: ID of the user
        @return: datetime
        """
        global user_action_time, user_time_diff
        try:
            user_status = self.__user_get_status(user_id)
            user_action_time = user_status['lastActionTime']
            user_time_diff = user_status['timeDiff']
        except Exception as err:
            print(f'Error getting user status {err}')

        return datetime.fromtimestamp(user_action_time - user_time_diff)


# avito_client = AvitoClient(url='http://www.avito.ru')
# print(avito_client.get_user_last_action_time(177068588))
