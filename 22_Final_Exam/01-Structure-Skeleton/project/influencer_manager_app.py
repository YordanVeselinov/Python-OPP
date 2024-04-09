from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        try:
            influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == influencer.username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id=campaign_id,brand=brand, required_engagement=required_engagement)
        except ValueError:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(campaign)
        return f'Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}.'

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer: BaseInfluencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign: BaseCampaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment_for_influencer = influencer.calculate_payment(campaign)

        if payment_for_influencer > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment_for_influencer
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign.campaign_id}."

    def calculate_total_reached_followers(self):
        total_followers_dict = {}

        for campaign in self.campaigns:
            if campaign.approved_influencers:
                total_followers_dict[campaign] = sum(i.reached_followers(campaign.__class__.__name__) for i in campaign.approved_influencers)

        return total_followers_dict

    def influencer_campaign_report(self, username: str):
        influencer: BaseInfluencer = next(filter(lambda i: i.username == username, self.influencers))

        if not influencer.campaigns_participated:
            return f'{username} has not participated in any campaigns.'

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns: BaseCampaign = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = "$$ Campaign Statistics $$\n"
        for c in sorted_campaigns:
            result += f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, Total budget: ${c.budget:.2f}, Total reached followers: {sum([i.reached_followers(c.__class__.__name__) for i in c.approved_influencers])}\n"

        return result[:-1]
