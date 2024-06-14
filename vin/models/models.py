from odoo import models, fields, api


class BrandCatalogue(models.Model):
    _name = 'brand.catalogue'
    _description = '品牌目录'

    origin_id = fields.Integer(string='源id', help='数据源id')
    code = fields.Char(string='零件编号', help='零件编号')
    name = fields.Char(string='零件名称', help='零件名称')
    image_url = fields.Char(string='图片URL', help='图片的URL')  # 添加这个字段


class VehicleInfo(models.Model):
    _name = 'vehicle.info'
    _description = '车辆信息'

    vin = fields.Char(string='车架号', help='车架号')
    code = fields.Char(string='车辆编号', help='车辆编号')
    name = fields.Char(string='车型', help='车型')
    brandCode = fields.Char(string='品牌编码', help='品牌编码')
    brandName = fields.Char(string='品牌', help='品牌')
    image_url = fields.Char(string='图片URL', help='图片的URL')  # 添加这个字段
    description = fields.Char(string='描述', help='描述')
    selectorId = fields.Char(string='查询id', help='查询id')
    modelId = fields.Char(string='modelId', help='modelId')
    modelCode = fields.Char(string='modelCode', help='modelCode')
    area = fields.Char(string='区域', help='区域')
    engine = fields.Char(string='引擎', help='引擎')
    sales_code = fields.Char(string='销售代码', help='销售代码')
    power = fields.Char(string='功率', help='车辆的功率')
    interior = fields.Char(string='内饰', help='车辆的内饰')
    chassis_number = fields.Char(string='车架号', help='车辆的车架号')
    series = fields.Char(string='系列', help='车辆的系列')
    chassis = fields.Char(string='底盘', help='车辆的底盘')
    displacement = fields.Char(string='排量', help='车辆的排量')
    drive = fields.Char(string='驱动', help='车辆的驱动类型')
    production_date = fields.Date(string='生产日期', help='车辆的生产日期')
    body_color = fields.Char(string='车身颜色', help='车辆的车身颜色')
    transmission = fields.Char(string='变速箱', help='车辆的变速箱类型')
    body_type = fields.Char(string='车体', help='车辆的车体类型')
    number_of_doors = fields.Integer(string='车门数', help='车辆的车门数量')
    Transmission = fields.Char(string='变速箱', help='车辆的车体类型')

    A0A96 = fields.Char(string='0A96')
    L8AAA = fields.Char(string='L8AAA')
    M416 = fields.Char(string='M416')
    MA = fields.Many2many('vehicle.ma', string='MA')
    MAMU = fields.Char(string='MAMU')
    MU = fields.Many2many('vehicle.mu', string='MU')
    P337A = fields.Char(string='P337A')
    S1CAA = fields.Char(string='S1CAA')
    S22SA = fields.Char(string='S22SA')
    S258A = fields.Char(string='S258A')
    S2PAA = fields.Char(string='S2PAA')
    S2TEA = fields.Char(string='S2TEA')
    S2VBA = fields.Char(string='S2VBA')
    S322A = fields.Many2many('vehicle.s322a', string='S322A')
    S3ATA = fields.Char(string='S3ATA')
    S3MBA = fields.Char(string='S3MBA')
    S431A = fields.Char(string='S431A')
    S481A = fields.Char(string='S481A')
    S494A = fields.Char(string='S494A')
    S4LHA = fields.Char(string='S4LHA')
    S4U0A = fields.Char(string='S4U0A')
    S4URA = fields.Char(string='S4URA')
    S534A = fields.Char(string='S534A')
    S548A = fields.Char(string='S548A')
    S552A = fields.Char(string='S552A')
    S5ACA = fields.Char(string='S5ACA')
    S5ALA = fields.Char(string='S5ALA')
    S5AVA = fields.Char(string='S5AVA')
    S5DMA = fields.Char(string='S5DMA')
    S688A = fields.Char(string='S688A')
    S6ACA = fields.Char(string='S6ACA')
    S6AEA = fields.Char(string='S6AEA')
    S6AKA = fields.Char(string='S6AKA')
    S6C3A = fields.Char(string='S6C3A')
    S6CPA = fields.Char(string='S6CPA')
    S6NSA = fields.Char(string='S6NSA')
    S6U3A = fields.Char(string='S6U3A')
    S710A = fields.Many2many('vehicle.s710a', string='S710A')
    S715A = fields.Char(string='S715A')
    S825A = fields.Char(string='S825A')
    S866A = fields.Char(string='S866A')
    S892A = fields.Many2many('vehicle.s892a', string='S892A')
    S8KMA = fields.Char(string='S8KMA')
    S8R2A = fields.Char(string='S8R2A')
    S8SMA = fields.Char(string='S8SMA')
    S8TNA = fields.Char(string='S8TNA')
    S993A = fields.Char(string='S993A')
    S9AAA = fields.Char(string='S9AAA')

    create_time = fields.Date(string='创建时间', help='记录的创建时间')

    def vin_search(self):
        action = {
            'type': 'ir.actions.act_url',
            'url': '/vehicle/vin_search',
            'target': 'new',
        }
        return action


class VehicleMA(models.Model):
    _name = 'vehicle.ma'
    _description = 'MA'

    name = fields.Char(string='Name', required=True)


class VehicleMU(models.Model):
    _name = 'vehicle.mu'
    _description = 'Some Other Model'

    name = fields.Char(string='Name', required=True)


class VehicleS322A(models.Model):
    _name = 'vehicle.s322a'
    _description = 'Another Model'

    name = fields.Char(string='Name', required=True)


class VehicleS710A(models.Model):
    _name = 'vehicle.s710a'
    _description = 'Yet Another Model'

    name = fields.Char(string='Name', required=True)


class VehicleS892A(models.Model):
    _name = 'vehicle.s892a'
    _description = 'Model Yet Another'

    name = fields.Char(string='Name', required=True)






