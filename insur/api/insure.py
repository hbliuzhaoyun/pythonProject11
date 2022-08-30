import requests

from insur.utils.log import log


class Insure:
    def insure_list(self,insuName,pageSize):
        r =requests.post(
            'https://insure-admin-oppo-prj.tenserpay.xyz/prdmc/prdmcProduct/getProductPage',
            headers={'Content-Type':'application/json;charset=utf-8',
                       'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSBpbnN1cmUiLCJwd2RSZXNldFRpbWUiOjE2NDA1NzM1OTYwMDAsInVzZXJfbmFtZSI6ImFkbWluIiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTY2MTUyNDcxNCwidXNlcklkIjoxLCJhdXRob3JpdGllcyI6WyJST0xFX0FETUlOIiwiUk9MRV9VU0VSIl0sImp0aSI6ImNlMDdhNjJjLWY0ZWUtNDVmOC1iZmY0LTNhZjlhNGQ1ZmM1MyIsImNsaWVudF9pZCI6IjVlYTBhOTUxYTAwNmFhNDYyNzM2ZWJjNmZhNDU5M2UyMWI2ZTdkNDcifQ.BzlEW0J4CA1VZhkxOIwiCQla32iEiFdU9jg5LvAiuxs'
                       },
            json ={'insuName':insuName,
                   'pageSize':pageSize}
        )
        log.debug(r.status_code)
        log.debug(r.text)
        return r

