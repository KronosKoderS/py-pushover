from py_pushover import _BaseManager


class VerificationManager(_BaseManager):
    def __init__(self, app_token):
        super().__init__(app_token)
        self._validate_url = self._base_url + "/users/validate.json"
        raise NotImplementedError

    def verify_user(self, user_id, device=None):
        """
        Validates whether a userID is a valid id and returns a Boolean as a result

        :param user_id:
        :return bool:
        """
        return self.verify_group(user_id, device)

    def verify_group(self, group_id, device=None):
        """
        Validates whether a groupID is a valid ID and returns a Boolean as a result

        :param group_id:
        :return bool:
        """
        param_data = {
            'token': self._app_token,
            'user': group_id
        }

        if device:
            param_data['device'] = device

        self._send(self._validate_url, param_data, check_response=False)

        if self.latest_response_dict['status'] == 1:
            return True
        else:
            return False
