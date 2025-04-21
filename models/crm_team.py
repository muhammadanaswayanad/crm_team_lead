from odoo import models, fields, api

class CrmTeamLead(models.Model):
    _inherit = 'crm.team'

    member_company_ids = fields.Many2many('res.company', string='Member Companies', 
                                        compute='_compute_member_company_ids', store=True)

    @api.depends('member_ids.company_ids')
    def _compute_member_company_ids(self):
        for team in self:
            team.member_company_ids = team.member_ids.mapped('company_ids')

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