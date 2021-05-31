# -*- coding: utf-8 -*-

from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    facebook_pixel_key = fields.Char('Facebook Pixel ID')
    facebook_domain_verification_code = fields.Char('Facebook Domain Verification Code')