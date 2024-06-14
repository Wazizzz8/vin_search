from odoo import http
from odoo.http import request


class VehicleController(http.Controller):

    @http.route('/vehicle/vin_search', type='http', auth='user', website=True)
    def vin_search(self, **kwargs):
        vin = kwargs.get('vin')
        vehicle = request.env['vehicle.info'].sudo().search([('chassis_number', '=', vin)])
        if vehicle:
            return request.render('my_module.vehicle_info_template', {
                'vehicle': vehicle
            })
        else:
            return request.render('my_module.no_vehicle_found_template')