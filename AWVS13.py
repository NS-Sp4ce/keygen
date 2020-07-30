'''
@Author         : Sp4ce
@Date           : 2020-02-19 16:01:14
@LastEditors    : Sp4ce
@LastEditTime   : 2020-07-30 15:07:26
@Description    : Challenge Everything.
'''
from hashlib import md5
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--license_key", type=str, help="license_key")
parser.add_argument("-p",
                    "--product_code",
                    type=str,
                    default='AOPENT',
                    help="product_code")
parser.add_argument("-mt",
                    "--max_targets",
                    type=str,
                    default=9999999,
                    help="max_targets")
parser.add_argument("-me",
                    "--max_engines",
                    type=str,
                    default=9999999,
                    help="max_engines")
parser.add_argument("-mav",
                    "--major_version",
                    type=str,
                    default=13,
                    help="major_version")
parser.add_argument("-miv",
                    "--minor_version",
                    type=str,
                    default=0,
                    help="minor_version")
parser.add_argument("-bn",
                    "--build_number",
                    type=str,
                    default=200625101,
                    help="minor_version")
#配置
args = parser.parse_args()
license_key = args.license_key
product_code = args.product_code
max_targets = args.max_targets
max_engines = args.max_engines
major_version = args.major_version
minor_version = args.minor_version
build_number = args.build_number
activated = 'true'
scan = 'true'
update = 'true'
access = 'true'
expired = 'false'
maintenance_expired = 'false'
offline = 'false'
bxss_user_id = ''
bxss_api_key = ''
secret = '25128b0a92d51e6bf4ea7a40b91b33be911144f7'
#示例
'''
        activation_error = license_data.get('activation_error', 0)
        if isinstance(activation_error, str):
            activation_error = int(activation_error)
        secret = '25128b0a92d51e6bf4ea7a40b91b33be911144f7'
        canonical_form = ''.join((
         secret,
         license_data.get('license_key', ''),
         license_data.get('product_code', ''),
         '%06d' % (license_data.get('max_targets', 0),),
         '%06d' % (license_data.get('max_engines', 0),),
         license_data.get('bxss_user_id', ''),
         license_data.get('bxss_api_key', ''),
         'true' if license_data.get('offline', False) else 'false',
         '%06d' % (license_data.get('major_version', 0),),
         '%06d' % (license_data.get('minor_version', 0),),
         '%06d' % (license_data.get('build_number', 0),),
         'true' if license_data.get('expired') else 'false',
         'true' if license_data.get('maintenance_expired') else 'false',
         '%06d' % (activation_error,),
         'true' if license_data.get('activated') else 'false',
         'true' if license_data.get('scan') else 'false',
         'true' if license_data.get('update') else 'false',
         'true' if license_data.get('access') else 'false',
         '%d' % (license_data.get('grace', 0),)))
        checksum = md5(canonical_form)
        if checksum != license_data.get('checksum'):
            raise LicenseChecksumException()
'''

canonical_form = ''.join((
    secret,
    license_key,  #license_data.get('license_key', ''),
    product_code,  #license_data.get('product_code', ''),
    '%06d' % max_targets,  #'%06d' % (license_data.get('max_targets', 0),),
    '%06d' % max_engines,  #'%06d' % (license_data.get('max_engines', 0),),
    bxss_user_id,  #license_data.get('bxss_user_id', ''),
    bxss_api_key,  #license_data.get('bxss_api_key', ''),
    offline,  #'true' if license_data.get('offline', False) else 'false',
    '%06d' % major_version,  #'%06d' % (license_data.get('major_version', 0),),
    '%06d' % minor_version,  #'%06d' % (license_data.get('minor_version', 0),),
    '%06d' % build_number,  #'%06d' % (license_data.get('build_number', 0),),
    expired,  #true' if license_data.get('expired') else 'false',
    maintenance_expired,  #'true' if license_data.get('maintenance_expired') else 'false',
    '%06d' % 0,  #'%06d' % (activation_error,),
    activated,  #'true' if license_data.get('activated') else 'false',
    scan,  #'true' if license_data.get('scan') else 'false',
    update,  #'true' if license_data.get('update') else 'false',
    access,  #'true' if license_data.get('access') else 'false',
    '%d' % -1))
checksum = md5(canonical_form.encode('utf-8'))

license_text = r'''{
    "info": {
        "license_key": "''' + license_key + '''",
        "company": "Test.com",
        "name": "Sp4ce",
        "phone": "00111111111111",
        "email": "test@test.com",
        "country": "US",
        "first_activated": "2020-6-29",
        "expires": "2099-10-01",
        "maintenance_expires": "2099-10-01",
        "max_engines": ''' + str(max_engines) + ''',
        "max_targets": ''' + str(max_targets) + ''',
        "product_code": "''' + product_code + '''",
        "bxss_user_id": "",
        "bxss_api_key": "",
        "is_offline": false,
        "is_worker": false
    },
    "major_version": ''' + str(major_version) + ''',
    "minor_version": ''' + str(minor_version) + ''',
    "build_number": ''' + str(build_number) + ''',
    "expired": false,
    "maintenance_expired": false,
    "scan": true,
    "update": true,
    "access": true,
    "activation_error": 0,
    "activated": true,
    "checksum": "''' + str(checksum.hexdigest()) + '''",
    "grace": -1,
    "last_reactivated": "2020-6-29"
}
'''

with open('license_info.json', 'w+') as f:
    f.write(license_text)
print(
    '\n\nlicense generate success for ' + license_key +
    '\n COPY license_info.json TO FOLLOWING FOLDER: \nC:\ProgramData\Acunetix\shared\license\ \nAND ENJOY!'
)
