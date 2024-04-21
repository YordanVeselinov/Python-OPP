from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE)

    def reached_followers(self, campaign_type: str):
        result = 0

        if campaign_type == "HighBudgetCampaign":
            result = (self.followers * self.engagement_rate) * 1.50
        elif campaign_type == "LowBudgetCampaign":
            result = (self.followers * self.engagement_rate) * 0.80

        return int(result)

