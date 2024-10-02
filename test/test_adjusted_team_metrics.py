# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.adjusted_team_metrics import AdjustedTeamMetrics  # noqa: E501

class TestAdjustedTeamMetrics(unittest.TestCase):
    """AdjustedTeamMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdjustedTeamMetrics:
        """Test AdjustedTeamMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdjustedTeamMetrics`
        """
        model = AdjustedTeamMetrics()  # noqa: E501
        if include_optional:
            return AdjustedTeamMetrics(
                year = 56,
                team_id = 56,
                team = '',
                conference = '',
                epa = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                    rushing = 1.337, 
                    passing = 1.337, 
                    total = 1.337, ),
                epa_allowed = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                    rushing = 1.337, 
                    passing = 1.337, 
                    total = 1.337, ),
                success_rate = cfbd.models.adjusted_team_metrics_success_rate.AdjustedTeamMetrics_successRate(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    total = 1.337, ),
                success_rate_allowed = cfbd.models.adjusted_team_metrics_success_rate.AdjustedTeamMetrics_successRate(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    total = 1.337, ),
                rushing = cfbd.models.adjusted_team_metrics_rushing.AdjustedTeamMetrics_rushing(
                    highlight_yards = 1.337, 
                    open_field_yards = 1.337, 
                    second_level_yards = 1.337, 
                    line_yards = 1.337, ),
                rushing_allowed = cfbd.models.adjusted_team_metrics_rushing.AdjustedTeamMetrics_rushing(
                    highlight_yards = 1.337, 
                    open_field_yards = 1.337, 
                    second_level_yards = 1.337, 
                    line_yards = 1.337, ),
                explosiveness = 1.337,
                explosiveness_allowed = 1.337
            )
        else:
            return AdjustedTeamMetrics(
                year = 56,
                team_id = 56,
                team = '',
                conference = '',
                epa = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                    rushing = 1.337, 
                    passing = 1.337, 
                    total = 1.337, ),
                epa_allowed = cfbd.models.adjusted_team_metrics_epa.AdjustedTeamMetrics_epa(
                    rushing = 1.337, 
                    passing = 1.337, 
                    total = 1.337, ),
                success_rate = cfbd.models.adjusted_team_metrics_success_rate.AdjustedTeamMetrics_successRate(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    total = 1.337, ),
                success_rate_allowed = cfbd.models.adjusted_team_metrics_success_rate.AdjustedTeamMetrics_successRate(
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    total = 1.337, ),
                rushing = cfbd.models.adjusted_team_metrics_rushing.AdjustedTeamMetrics_rushing(
                    highlight_yards = 1.337, 
                    open_field_yards = 1.337, 
                    second_level_yards = 1.337, 
                    line_yards = 1.337, ),
                rushing_allowed = cfbd.models.adjusted_team_metrics_rushing.AdjustedTeamMetrics_rushing(
                    highlight_yards = 1.337, 
                    open_field_yards = 1.337, 
                    second_level_yards = 1.337, 
                    line_yards = 1.337, ),
                explosiveness = 1.337,
                explosiveness_allowed = 1.337,
        )
        """

    def testAdjustedTeamMetrics(self):
        """Test AdjustedTeamMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
