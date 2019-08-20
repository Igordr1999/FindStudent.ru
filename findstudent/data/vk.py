import requests
from findstudent.settings import VK_URL, VK_LANG, VK_VERSION, VK_TOKEN


class VK:
    api_url = VK_URL
    lang = VK_LANG
    api_version = VK_VERSION
    token = VK_TOKEN

    dynamic_data = {
        'group_members': '/groups.getMembers',
        'groups_info': '/groups.getById',
        'metro_stations': '/database.getMetroStations',
        'users_info': '/users.get',
        'user_photos': '/photos.get',
        'user_subscription': '/users.getSubscriptions',
        'friend_list': '/friends.get'
    }

    def get_metro_stations(self, city_id, offset=0, count=10):
        """!
            @brief Get russians metro stations by city
            @return Time in unix format
            @param city_id VK unique city id
            @param offset offset of top
            @param count number of stations that must be returned
            @return : List of dict: id+name for each station
        """
        extra_params = {
            'city_id': city_id,
            'offset': offset,
            'count': count,
        }
        return self.api_request(method_name="metro_stations", extra_params=extra_params)

    def get_users_info(self, user_ids, fields, name_case="nom"):
        user_ids = self.from_list_to_str(user_ids)
        fields = self.from_list_to_str(fields)
        extra_params = {
            'user_ids': user_ids,
            'fields': fields,
            'name_case': name_case,
        }
        return self.api_request(method_name="users_info", extra_params=extra_params, items=False)

    def get_groups_info(self, group_ids, fields):
        user_ids = self.from_list_to_str(group_ids)
        fields = self.from_list_to_str(fields)
        extra_params = {
            'group_ids': user_ids,
            'fields': fields,
        }
        return self.api_request(method_name="groups_info", extra_params=extra_params, items=False)

    def get_group_members(self, group_id, fields, sort="id_asc", offset=0, count=1000):
        fields = self.from_list_to_str(fields)
        extra_params = {
            'group_id': group_id,
            'fields': fields,
            'sort': sort,
            'offset': offset,
            'count': count,
        }
        return self.api_request(method_name="group_members", extra_params=extra_params,)

    def get_user_photos(self, owner_id, album_id="profile", rev=1, offset=0, count=1000):
        extra_params = {
            'owner_id': owner_id,
            'album_id': album_id,
            'rev': rev,
            'offset': offset,
            'count': count,
        }
        return self.api_request(method_name="user_photos", extra_params=extra_params)

    def get_user_groups(self, user_id, fields, extended=1, offset=0, count=20):
        fields = self.from_list_to_str(fields)
        extra_params = {
            'user_id': user_id,
            'fields': fields,
            'extended': extended,
            'offset': offset,
            'count': count,
        }
        return self.api_request(method_name="user_subscription", extra_params=extra_params)

    def get_friends_list(self, user_id, fields, offset=0, count=20, order="random", name_case="nom"):
        fields = self.from_list_to_str(fields)
        extra_params = {
            'user_id': user_id,
            'fields': fields,
            'offset': offset,
            'count': count,
            'order': order,
            'name_case': name_case,
        }
        return self.api_request(method_name="friend_list", extra_params=extra_params)

    def api_request(self, method_name, extra_params, items=True):
        url = self.api_url + self.dynamic_data[method_name]
        params = {
            'lang': self.lang,
            'access_token': self.token,
            'v': self.api_version,
        }
        params = {**params, **extra_params}
        answer = self.simple_request(url=url, params=params)
        # print(answer["error"]["error_code"], answer["error"]["error_msg"])
        return answer["response"]["items"] if items else answer["response"]

    def simple_request(self, url, params):
        data = requests.get(url=url, params=params)
        data_json = self.check_request(data=data)
        return data_json

    @staticmethod
    def get_request_url(url, params):
        data = requests.get(url=url, params=params)
        return data.url

    @staticmethod
    def check_request(data):
        if data.status_code == 200:
            return data.json()
        else:
            print("Server return request with {} code.".format(data.status_code))
            return 0

    @staticmethod
    def from_list_to_str(data):
        return ",".join(str(x) for x in data)
