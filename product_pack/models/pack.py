# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from openerp import models, fields


class ProductPack(models.Model):
    _name = 'product.pack'
    _description = 'Product Pack'

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product template')
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        domain=[('is_pack', '=', False)])
    quantity = fields.Float(
        string='Quantity',
        default=1.0)