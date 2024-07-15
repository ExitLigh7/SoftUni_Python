from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class InfluencerManagerApp:

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        pass

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        pass

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        pass

    def calculate_total_reached_followers(self):
        pass

    def influencer_campaign_report(self, username: str):
        pass

    def campaign_statistics(self):
        pass
