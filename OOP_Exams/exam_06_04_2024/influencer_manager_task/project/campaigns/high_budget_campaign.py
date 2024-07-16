from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET: float = 5000.0
    MIN_ENGAGEMENT_RATE: float = 1.2    #120%

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        needed_rate = self.MIN_ENGAGEMENT_RATE * self.required_engagement
        return engagement_rate >= needed_rate



