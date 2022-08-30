import json

from jsonpath import jsonpath

from insur.api.insure import Insure
from insur.utils.log import log


class TestInsure():
    def setup_class(self):
        self.insure = Insure()

    def setup(self):
        ...


    def teadown(self):
        ...


    def teadown_class(self):
        ...


    def test_search_query_null(self):
        r = self.insure.insure_list('','')
        assert r.status_code == 200
        assert 65 in jsonpath(r.json(), '$..total')

    def test_search_result_null(self):
        r = self.insure.insure_list('5678','')
        assert r.status_code == 200

        ...


    def test_search_result_single(self):
        r = self.insure.insure_list('平安','1')
        assert r.status_code == 200
        #assert r.json()['total'] == 6
        #assert r.json()['records']['adminInfo']['name'] == '平安个意险赠险'
        assert 30 in jsonpath(r.json(), '$..orgId')
        print(r.json())
        # assert r[0].lastName.lower() == 'black'
        # ...


    def test_search_result_multi(self):
        r = self.insure.insure_list('众安','1')
        # log.debug("test_search_result_multi")
        # log.debug(r)
        assert r.status_code == 200
        assert '众安保险' in jsonpath(r.json(), '$..insuName')