import requests
import os
from dotenv import load_dotenv
from datetime import date
import unittest

load_dotenv()

ya_base_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
ya_headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': os.getenv('YA_TOKEN')}
ya_params = {'path': f'{date.today()}'}

FOLDER_NAME = date.today()


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.headers = ya_headers
        self.delete_folder()

    def tearDown(self):
        self.delete_folder()

    def test_create_folder_success(self):
        response = self.create_folder()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(self.check_folder_exists())

    def test_create_existing_folder(self):
        self.create_folder()
        response = self.create_folder()
        self.assertEqual(response.status_code, 409)

    def test_empty_folder_name(self):
        response = requests.get(f'{ya_base_url}/', headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def create_folder(self):
        return requests.put(ya_base_url, headers=ya_headers, params=ya_params)

    def delete_folder(self):
        try:
            requests.delete(ya_base_url, headers=ya_headers, params=ya_params)
        except Exception:
            pass

    def check_folder_exists(self):
        response = requests.get(f'{ya_base_url}?path={FOLDER_NAME}', headers=self.headers
                                )
        return response.status_code == 200


if __name__ == '__main__':
    unittest.main()
