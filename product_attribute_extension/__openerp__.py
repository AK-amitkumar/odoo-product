# -*- coding: utf-8 -*-
##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones (<http://www.trey.es>).
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
##############################################################################

{
    'name': 'Product attribute extension',
    'category': 'Product',
    'summary': 'Product attribute extension',
    'version': '0.1',
    'description': """
        Add form view and menu for product attribute value and product attribute objects.
    """,
    'author': 'Trey',
    'depends': ['base', 'product'],
    'data': [
        'views/product_view.xml',
        'menu.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'css': [
    ],
    'installable': True,
}