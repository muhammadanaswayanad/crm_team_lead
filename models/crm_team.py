from odoo import models, fields, api

class CrmTeamLead(models.Model):
    _inherit = 'crm.team'

    def _get_leads_for_team_lead(self):
        # This method will return leads assigned to the user's team
        user = self.env.user
        if user.has_group('crm_team_lead.group_team_lead'):
            return self.search([('team_id', '=', user.team_id.id)])
        return super(CrmTeamLead, self)._get_leads_for_team_lead()

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    team_id = fields.Many2one('crm.team', string='Team')

class TeamLeadGroup(models.Model):
    _inherit = 'res.groups'

    @api.model
    def create_team_lead_group(self):
        group = self.create({
            'name': 'Team Lead',
            'category_id': self.env.ref('base.module_category_sales').id,
        })
        return group