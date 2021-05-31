# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    facebook_pixel_key = fields.Char(
        related='website_id.facebook_pixel_key',
        readonly=False,
    )

    facebook_domain_verification_code = fields.Char(
        related='website_id.facebook_domain_verification_code',
        readonly=False,
    )

    @api.depends('website_id')
    def has_facebook_pixel(self):
        self.has_facebook_pixel = bool(self.facebook_pixel_key)

    def inverse_has_facebook_pixel(self):
        if not self.has_facebook_pixel:
            self.facebook_pixel_key = False
            self.facebook_domain_verification_code = False

    has_facebook_pixel = fields.Boolean(
        string='Facebook Pixel',
        compute=has_facebook_pixel,
        inverse=inverse_has_facebook_pixel,
    )
