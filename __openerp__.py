# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Website - Hide 'Add to Cart' button",
    'category': 'Website',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['website_sale'],
    'description': """
Website - Hide 'Add to Cart' button
===================================
 * Hides the Add to Cart button as well as the +/- buttons from website's product pages
""",
    'data': [
        'views/add_to_cart.xml',
    ]
    
}
