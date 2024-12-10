from typing import Dict

from settings import SiteSettings
from site_API.utils.site_api_handler import SiteApiInterface

site = SiteSettings()

url: str = 'https://' + site.host_api

headers: Dict = {
    "accept": "application/json",
    "X-API-KEY": site.api_key.get_secret_value()
}

site_api = SiteApiInterface()

if __name__ == '__main__':
    site_api()
