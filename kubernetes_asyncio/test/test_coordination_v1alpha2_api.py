# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.32.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.coordination_v1alpha2_api import CoordinationV1alpha2Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestCoordinationV1alpha2Api(unittest.IsolatedAsyncioTestCase):
    """CoordinationV1alpha2Api unit test stubs"""

    async def asyncSetUp(self):
        self.api = kubernetes_asyncio.client.api.coordination_v1alpha2_api.CoordinationV1alpha2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_lease_candidate(self):
        """Test case for create_namespaced_lease_candidate

        """
        pass

    def test_delete_collection_namespaced_lease_candidate(self):
        """Test case for delete_collection_namespaced_lease_candidate

        """
        pass

    def test_delete_namespaced_lease_candidate(self):
        """Test case for delete_namespaced_lease_candidate

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_lease_candidate_for_all_namespaces(self):
        """Test case for list_lease_candidate_for_all_namespaces

        """
        pass

    def test_list_namespaced_lease_candidate(self):
        """Test case for list_namespaced_lease_candidate

        """
        pass

    def test_patch_namespaced_lease_candidate(self):
        """Test case for patch_namespaced_lease_candidate

        """
        pass

    def test_read_namespaced_lease_candidate(self):
        """Test case for read_namespaced_lease_candidate

        """
        pass

    def test_replace_namespaced_lease_candidate(self):
        """Test case for replace_namespaced_lease_candidate

        """
        pass


if __name__ == '__main__':
    unittest.main()
