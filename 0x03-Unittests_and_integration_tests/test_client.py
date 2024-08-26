#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload
from fixtures import expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """Test the publc repo ur property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)

        # Check that the result is as expected
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test integration github org client class"""
    @classmethod
    def setUpClass(cls):
        # Start patching requests.get
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            """Get json side effect funtion"""
            org_url = f"https://api.github.com/orgs/{cls.org_payload['login']}"
            if url == org_url:
                return cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return None
        mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to test license"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called

    def test_public_repos_with_license(self):
        """test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()
