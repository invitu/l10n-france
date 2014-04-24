# -*- encoding: utf-8 -*-
###############################################################################
#
#   l10n_fr_account_fiscal_position_rule for OpenERP
#   Copyright (C) 2012-TODAY Akretion <http://www.akretion.com>.
#     @author Sébastien BEAU <sebastien.beau@akretion.com>
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


{'name': 'l10n_fr_account_fiscal_position_rule',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'French Localization',
 'description': """French Fiscal rule for the setting automatically the
 fiscal position depending of the address.
 """,
 'depends': [
     'account_fiscal_position_rule',
 ],
 'data': [
     'settings/account.fiscal.position.rule.template.csv',
 ],
 'installable': True,
 'application': True,
}
