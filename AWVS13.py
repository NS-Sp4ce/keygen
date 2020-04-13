'''
@Author         : Sp4ce
@Date           : 2020-02-19 16:01:14
@LastEditors    : Sp4ce
@LastEditTime   : 2020-02-22 22:50:19
@Description    : Challenge Everything.
'''
from hashlib import md5
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--license_key", type=str,
                    help="license_key")
parser.add_argument("-p", "--product_code", type=str, default='AOPENT',
                    help="product_code")
parser.add_argument("-mt", "--max_targets", type=str, default=9999999,
                    help="max_targets")
parser.add_argument("-me", "--max_engines", type=str, default=9999999,
                    help="max_engines")

args = parser.parse_args()
license_key = args.license_key
product_code = args.product_code
max_targets = args.max_targets
max_engines = args.max_engines
major_version = 13
minor_version = 0
build_number = 200205121
activated = 'true'
scan = 'true'
update = 'true'
access = 'true'
activated = 'true'
bxss_user_id = ''
bxss_api_key = ''

secret = '25128b0a92d51e6bf4ea7a40b91b33be911144f7'
canonical_form = ''.join((
    secret,
    license_key,
    product_code,
    '%06d' % max_targets,
    '%06d' % max_engines,
    bxss_user_id,
    bxss_api_key,
    'false',
    '%06d' % major_version,
    '%06d' % minor_version,
    '%06d' % build_number,
    'false',
    'false',
    '%06d' % 0,
    'true',
    'true',
    'true',
    'true',
    '%d' % -1))
checksum = md5(canonical_form.encode('utf-8'))


license_text = r'''
{
    "info": {
     "license_key": "'''+license_key+'''",
     "company": "Test.com",
     "name": "nszy007",
     "phone": "00111111111111",
     "email": "test@test.com",
     "country": "US",
     "first_activated": "2020-02-05T14:17:33.34",
     "expires": "true",
     "maintenance_expires": "2099-10-01T20:17:52",
     "max_engines": '''+str(max_engines)+''',
     "max_targets": '''+str(max_targets)+''',
     "product_code": "'''+product_code+'''",
     "bxss_user_id": "",
     "bxss_api_key": "",
     "is_offline": false,
     "is_worker": false
    },
    "major_version": 13,
    "minor_version": 0,
    "build_number": 200205121,
    "expired": false,
    "maintenance_expired": false,
    "scan": true,
    "update": true,
    "access": true,
    "activated": true,
    "checksum": "'''+str(checksum.hexdigest())+'''",
    "grace": -1,
    "last_reactivated": "2020-02-10T20:17:52"
   }
'''

with open('license_info.json','w+') as f:
    f.write(license_text)
print('\n\nlicense generate success for '+license_key+'\n COPY license_info.json TO FOLLOWING FOLDER: \nC:\ProgramData\Acunetix\shared\license\ \nAND ENJOY!')
