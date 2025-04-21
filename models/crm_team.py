from odoo import models, fields, api

class CrmTeamLead(models.Model):
    _inherit = 'crm.team'

    def _get_leads_for_team_lead(self):
        user = self.env.user
        if user.has_group('crm_team_lead.group_crm_team_lead'):
            return self.search([('team_id', '=', user.team_id.id)])
        return super(CrmTeamLead, self)._get_leads_for_team_lead()

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    team_id = fields.Many2one('crm.team', string='Team')
    team_ids = fields.Many2many('crm.team', string='Teams', compute='_compute_team_ids', store=True)
    
    @api.depends('team_id')
    def _compute_team_ids(self):
        for user in self:
            user.team_ids = user.team_id